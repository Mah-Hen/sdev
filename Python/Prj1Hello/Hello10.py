class MemoryBlock:
    def __init__(self, start, size, allocated=False):
        self.start = start
        self.size = size
        self.allocated = allocated
        self.next = None
        
class MemoryAllocator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = MemoryBlock(0, capacity, allocated=False)
        
    def allocate(self, size):
        # Find the best-fit free block
        best_block = None
        current_block = self.head
        while current_block is not None:
            if not current_block.allocated and current_block.size >= size:
                if best_block is None or current_block.size < best_block.size:
                    best_block = current_block
            current_block = current_block.next
        
        if best_block is None:
            print(f"Not enough memory")
            return
        
        # Split the free block and allocate the best-fit part
        if best_block.size > size:
            new_block = MemoryBlock(best_block.start + size, best_block.size - size, allocated=False)
            new_block.next = best_block.next
            best_block.next = new_block
            best_block.size = size
        best_block.allocated = True
        
        self.print_memory()
        
    def free(self, start):
        # Find the block to free
        current_block = self.head
        while current_block is not None:
            if current_block.start == start and current_block.allocated:
                current_block.allocated = False
                break
            current_block = current_block.next
        
        if current_block is None:
            print(f"{start} is not a valid location")
            return
        
        # Coalesce adjacent free blocks
        while current_block.next is not None and not current_block.next.allocated:
            current_block.size += current_block.next.size
            current_block.next = current_block.next.next
        
        self.print_memory()
        
    def print_memory(self):
        # Collect memory blocks
        blocks = []
        current_block = self.head
        while current_block is not None:
            blocks.append(current_block)
            current_block = current_block.next
        
        # Sort by block start
        blocks = sorted(blocks, key=lambda b: b.start)
        
        # Print blocks with allocations and free spaces
        print("  ".join([f"[{b.start}-{b.start+b.size-1}{'A' if b.allocated else 'F'}]" for b in blocks]))
        
if __name__ == "__main__":
    # Parse input file
    with open('/Users/mahla/Downloads/alloc1.txt') as f:
        lines = f.readlines()
        capacity = int(lines[0])
        allocator = MemoryAllocator(capacity)
        for line in lines[1:]:
            parts = line.strip().split()
            #print(parts[1])
            if parts[0] == "A":
                size = int(parts[1])
                allocator.allocate(size)
            elif parts[0] == "F":
                start = int(parts[1])
                allocator.free(start)