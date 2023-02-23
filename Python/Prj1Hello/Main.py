from Table import Table

def main():
    table  = Table(3,3)
    table.setChar(0,0,'A')
    table.setChar(0,1,'B')
    table.setChar(0,2,'C')
    table.setChar(1,0,'D')
    table.setChar(1,1,'E')
    table.setChar(1,2,'F')
    table.setChar(2,0,'G')
    table.setChar(2,1,'H')
    table.setChar(2,2,'I')
    

    table1 = Table(2,2)
    print(table.getChar(0,0))
    print(table.__eq__(table1))
    print(table)


main()