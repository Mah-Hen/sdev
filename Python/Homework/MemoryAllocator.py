def aMemory(map, bites):
    """
    Allocates a block of memory of the given size.
    Returns True if succesful, False otherwise.
    """
    for i in range(len(map)):
        if map[i] == 'F':
            block = 1
            j = i + 1
            while j < len(map) and map[j] == 'F':
                block += 1
                j += 1
            if block >= bites:
                for k in range(i, i+bites):
                    map[k] = 'A'
            return True
    return False  # supposed to return False only if no block of supposed size was found


def fMemory(map, start):
    """
    Frees the block of memory starting at the given location 
    Returns True if successful, False otherwise.
    """
    if map[start] != 'A':
        return False
    i = start
    while i < len(map[i]) and map[i] == 'F':
        map[i] = 'S'
        i += 1
    return True


def main():
    with open('/Users/mahla/Downloads/alloc1.txt') as file:
        # if you do just read(), it will mess up grabbing the index later down the line. But basically reading the file line by line.
        capacity = int(file.readline().strip())

        ##print(capacity)
        memmap = ['F'] * capacity
        # loop over the remainng lines in the fiel
        for content in file:  # file won't open if not within the file opening indentation
            # breaks list into strings and takes away whitespace at the end
            content = content.strip().split()
        # grabbing the first index out of the strings, which is the letter in this case or allocator
            alc = content[0]
        # grabbing the second index out of the strings, which is the bytes
            bites = int(content[1])
            # print(f"{alc}, {bites}", end=' ')  # print out to
            # Whats wrong with this code is that it needs to keep track of the updated map. All this is doing is just giving it the methods a brand new map of 1000 F's which is why none of the operations are working correctly. For example in aMemory method, once you get to 950, it is a brand new memory map instead of a continuation from the previous allocated lines
            if alc == 'A':  # Find a free block of memory
                if aMemory(memmap, bites):
                    print("{} {} [{}]".format(alc, bites, ','.join(memmap)))
                else:
                    print('{} {} Not enough memory [{}]'.format(
                        alc, bites, ','.join(memmap)))
            else:
                if fMemory(memmap, bites):
                    print('{} {} [{}]'.format(alc, bites, ','.join(memmap)))
                else:
                    print('{} {} Invalid location [{}]'.format(
                        alc, bites, ','.join(memmap)))


# printMemoryMap(memmap)
main()
