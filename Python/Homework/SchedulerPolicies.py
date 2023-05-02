import heapq
import sys

from PyQt6.QtGui import QAction, QIcon, QFont
from PyQt6.QtWidgets import (QWidget,
                             QHBoxLayout, QVBoxLayout, QApplication, QTextEdit, QFileDialog, QMainWindow, QToolBar,
                             QLabel, QRadioButton)
from pathlib import Path


class Scheduling(QMainWindow):

    def __init__(self):
        super().__init__()

        self.jobs = dict()

        self.initUI()

    def initUI(self):
        font = QFont("Monospace")
        font.setStyleHint(QFont.StyleHint.TypeWriter)
        self.jobs_list = QTextEdit()
        self.jobs_list.setFont(font)
        self.jobs_list.setText('Load a list of jobs by using File -> Open.')
        self.jobs_list.setReadOnly(True)
        self.jobs_list.setDisabled(True)

        self.schedule = QTextEdit()
        self.schedule.setFont(font)
        self.schedule.setText('No scheduling results available. Press the "Play" button on the toolbar.')
        self.schedule.setReadOnly(True)
        self.schedule.setDisabled(True)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.jobs_list)
        vbox.addWidget(self.schedule)

        widget = QWidget()
        widget.setLayout(vbox)

        self.setCentralWidget(widget)
        self.statusBar()
        self.policy_label = QLabel()
        self.statusBar().addWidget(self.policy_label)
        self.turn_around_label = QLabel()
        self.statusBar().addWidget(self.turn_around_label)

        openFile = QAction(QIcon('./assets/open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.show_dialog)

        exit = QAction(QIcon('./assets/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Shift+Q')
        exit.setStatusTip('Exit the application')
        exit.triggered.connect(QApplication.instance().quit)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(exit)

        run_action = QAction(QIcon('./assets/play.png'), 'Run', self)
        run_action.setShortcut('Ctrl+R')
        run_action.triggered.connect(self.simulate)

        toolbar = QToolBar('Main toolbar')
        self.addToolBar(toolbar)
        toolbar.addAction(run_action)

        self.policy_button = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        self.policy_button.setLayout(layout)

        self.radio = QRadioButton("FCFS", self)
        self.radio.toggled.connect(self.select_policy)
        layout.addWidget(self.radio)
        self.radio.nextCheckState()

        self.radio = QRadioButton("SJN", self)
        self.radio.toggled.connect(self.select_policy)
        layout.addWidget(self.radio)

        self.radio = QRadioButton("SRT", self)
        self.radio.toggled.connect(self.select_policy)
        layout.addWidget(self.radio)

        toolbar.addWidget(self.policy_button)

        self.setGeometry(300, 300, 950, 450)
        self.setWindowTitle('Scheduling Policies')
        self.show()


    def select_policy(self):
        if self.sender().isChecked():
            if self.sender().text() == 'FCFS':
                self.policy = self.make_FCFS_schedule
            elif self.sender().text() == 'SJN':
                self.policy = self.make_SJN_schedule
            elif self.sender().text() == 'SRT':
                self.policy = self.make_SRT_schedule
            self.policy_label.setText(self.sender().text())


    def show_dialog(self):
        home_dir = str(Path.cwd())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir, 'CSV files (*.csv)')

        if fname[0]:
            with open(fname[0], 'r') as file_handle:
                data = file_handle.read()
                self.jobs_list.setText(data)
            for line in data.strip().split('\n'):
                job, arrivalTimeival, cycles = line.split(',')
                self.jobs[job] = (int(arrivalTimeival), int(cycles))


    def simulate(self):
        if len(self.jobs) == 0:
            return
        schedule = self.policy()
        self.schedule.setText(Scheduling.format_schedule(schedule))
        avgTurnaroundTime = 0
        trnTime = 0
        current = 0
        # Add your code to compute average turnaround
        if self.policy == self.make_FCFS_schedule:
            for i in range(len(schedule)):
                if schedule[i][1] != None:
                    arrivalTime = schedule[i][0]
                    endTime = schedule[i+1][0]
                    trnTime += endTime-arrivalTime
            avgTurnaroundTime = trnTime/len(self.jobs)
        elif self.policy == self.make_SJN_schedule:
            job = None
            for i in range(len(schedule)):
                prevJob = job
                job = schedule[i][1]
                if job != prevJob:
                    arrivalTime, processingTime = self.jobs[job]
                    arrivalTime = i
                    startTime = schedule[i][0]
                    endTime = startTime + processingTime
                    trnTime += endTime - arrivalTime

            avgTurnaroundTime = trnTime / len(self.jobs)
        elif self.policy == self.make_SRT_schedule:
            complete = []
            newJob = None
            currentJob = newJob
            inc = 0
            for i in range(len(schedule)):
                newJob = schedule[i][1]
                for j in range(i+1, len(schedule)):
                    if newJob in complete:
                        break
                    try:
                        if newJob == schedule[j+1][1] : # if there is more than one occurrence
                            anotherJob = j # a job before the current job ends 
                            if newJob != None:
                                prevTT = trnTime
                                currentJob = newJob
                                start = schedule[i][0]
                                while anotherJob < len(schedule):
                                    if trnTime > prevTT:
                                        break
                                    if currentJob == schedule[anotherJob][1]: 
                                        endTime = schedule[anotherJob+1][0]
                                        trnTime += endTime - start
                                        complete.append(currentJob)
                                        inc +=1
                                        break
                                    else:
                                        anotherJob += 1
                                        continue
                            else:
                                break
                    except IndexError:
                        if newJob not in complete:
                            start = schedule[i][0]
                            endTime = schedule[i+1][0]
                            trnTime += endTime - start
                            complete.append(newJob)
                            inc +=1
                            break

                        

            avgTurnaroundTime = trnTime / len(self.jobs)


        self.turn_around_label.setText(f'Average turnaround time: {avgTurnaroundTime:.2f}')
        
    def make_FCFS_schedule(self):
        schedule = []
        queue = []
        time = 0
        for job, props in self.jobs.items():
            heapq.heappush(queue, (props[0], job))
        if len(queue) > 0:
            while len(queue) > 0:
                if queue[0][0] <= time:
                    schedule.append((time, heapq.heappop(queue)[1]))
                    time += self.jobs[schedule[-1][1]][1]
                else:
                    schedule.append((time, '*'))
                    time = queue[0][0]
            schedule.append((time, None))
        return schedule

    def make_SRT_schedule(self):
        schedule = []
        queue = []
        time = 0
        remainingTime = 0
        currentJobId = None

        # enqueue all jobs into the queue
        for jobId, (arrivalTime, processingTime) in self.jobs.items():
            heapq.heappush(queue, (arrivalTime, processingTime, jobId))

        while queue or currentJobId is not None:
            # check for new arrivals
            '''
            while queue and queue[0][0] <= time:
                arrivalTime, processingTime, jobId = heapq.heappop(queue)
                heapq.heappush(queue, (arrivalTime, processingTime, jobId))
                if processingTime > remainingTime:
                    break
            '''
            queue.sort()
            # if no job is currently being processed, start a new one
            if currentJobId is None:
                arrivalTime, processingTime, jobId = heapq.heappop(queue)
                remainingTime = processingTime
                currentJobId = jobId
                schedule.append((time, jobId))

            # if there is a shorter job in the queue, preempt the current job
            elif queue and queue[0][1] < remainingTime:
                newArr = time + remainingTime
                oldRTime = remainingTime
                oldJobId = currentJobId
                arrivalTime, processingTime, jobId = heapq.heappop(queue)
                remainingTime = processingTime
                currentJobId = jobId
                schedule.append((time, jobId))
                heapq.heappush(queue, (newArr, oldRTime, oldJobId))
                queue.sort()


            # process the current job
            remainingTime -= 1
            time += 1


            # finish the current job
            if remainingTime == 0:
                currentJobId = None

        else:
            schedule.append((time, schedule[len(schedule)-1][1]))
        return schedule

    def make_SJN_schedule(self):
        schedule = []
        queue = []
        time = 0
        remainingTime = 0
        currentJobId = None

        # enqueue all jobs into the queue
        for jobId, (arrivalTime, processingTime) in self.jobs.items():
            heapq.heappush(queue, (processingTime, arrivalTime, jobId))
        queue.sort()

        while queue:
            # choose the job with the shortest processingTimeing time
            processingTime, arrivalTime, jobId = heapq.heappop(queue)
            
            # execute the chosen job
            schedule.append((time, jobId))
            remainingTime = processingTime
            currentJobId = jobId
            
            # calculate the remaining time of the current job
            if remainingTime > 0:
                time += 1
                remainingTime -= 1

            # put in queue any jobs that arrive during the execution of the current job
            '''
            added = False
            while queue and queue[0][1] <= time:
                arrivalTime, processingTime, jobId = heapq.heappop(queue)
                heapq.heappush(queue, (arrivalTime, processingTime, jobId))
                if processingTime > remainingTime:
                    added = True
                    break
            '''
            # add the remaining time of the last job to the schedule
            while remainingTime > 0:
                schedule.append((time, currentJobId))
                time += 1
                remainingTime -= 1

        return schedule
    
          

    def format_schedule(schedule):
        schedule_plot = ['', '', '', '']
        for idx in range(len(schedule)):
            elem = schedule[idx]
            if idx != len(schedule) - 1:
                units = 4 * (schedule[idx + 1][0] - elem[0])
                if schedule_plot[0] == '':
                    schedule_plot[0] += '┌' + '─' * units
                    schedule_plot[1] += '│'
                    schedule_plot[2] += '└' + '─' * units
                else:
                    schedule_plot[0] += '┬' + '─' * units
                    schedule_plot[1] += '│'
                    schedule_plot[2] += '┴' + '─' * units
                schedule_plot[1] += f'{elem[1]:^{units}}'
                schedule_plot[3] += f'{elem[0]:<{" "}{units + 1}}'

        schedule_plot[0] += '┐'
        schedule_plot[1] += '│'
        schedule_plot[2] += '┘'
        schedule_plot[3] += f' {schedule[-1][0]}'
        return '\n'.join(schedule_plot)


def main():
    app = QApplication(sys.argv)
    ex = Scheduling()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
