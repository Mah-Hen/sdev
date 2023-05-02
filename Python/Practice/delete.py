def divideArray(nums):
        pairs = []
        temp = 0
        cnt = 0
        temp = nums[0]

        for i in range(len(nums)-1):
            if nums[i+1] == temp:
                pairs.append(temp)
                cnt += 1
                temp = nums[i]
            elif temp in pairs:
                  temp = nums[i]
        if cnt == len(nums)/2:
              return True
        else:
              return False
           

def main():
        print(divideArray([3,2,3,2,2,2]))

main()
