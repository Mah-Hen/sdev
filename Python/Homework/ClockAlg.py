def clock(pages, capacity):
    clockhand = 0 # keep track of current position of the clock hand. Basically a pointer to step through reference bits of the active pages
    rbits = {} # keep track of r-bits of each page
    cache = [] # list for pages in cache
    


    for page in pages: 
        if page in cache: # Check to see if page accessed in the cache
            rbits[page] = 1 #rbit of page set to 1
        else: # if not, then it is put into the cache
            lencache = len(cache)
            if lencache<capacity: # checks to see if cache is full
                cache.append(page) # accessed page is added to the cache
                rbits[page] = 1 # rbit set to 1
            else: #if the cache is too full gotta kick something out of the cache
                #Clockhand pointing to some page in the cache
                while rbits[cache[clockhand]] == 1: #a loop that continues to execute as long as the reference bit of the element in the cache indexed by hand is equal to 1. Then find the first element in the cache with a rbit of 0 
                    rbits[cache[clockhand]] = 0 #if the R-bit is 1, then it should be set to 0
                    clockhand = (clockhand + 1) % capacity # and the hand moves to the next item
                    #repeats the process with while loop,  continuing  until  finds  something  in  the  cache  whose  R-bit  is  0
                    #r-bit with 0 is then kicked out and repaced with new page
                #new page
                cache[clockhand] = page # replaces the previous page with the new page thanks to the hand
                rbits[page] = 1 # rbit of that page is set to 1
                clockhand = (clockhand + 1) % capacity # if it is 0, it wraps back. resue the memory space that has been freed up rather than allocating new memory
            
        print(cache, end=" ") # new cache
        
        bitstr = "" # empty string to add the rbits to
        for i in cache: # traverse through the cache
            bitstr += str(rbits[i]) # and add the elements, specifcally the rbits of each page
        print(bitstr) # print the rbits next to the cache


clock("ABACDACE", 3) # calling the clock method
clock("CADBED",4)
#Page 75 really helped in making this program, specifically the Clock Replacement Variation
