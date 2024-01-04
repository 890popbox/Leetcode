    def rotate(self, nums, k):
        # make sure k is lower than length to avoid unnessary cycles
        count, length = 0, len(nums)
        k = k % length
        # shift from original index until we cycle back to it, counting by k, keep track of prev to add it back
        index = 0
        shift = 0
        prev = nums[0]
        # we only have to go how many items in list
        while count<length:
            # replace current index with previous value and update previous
            tmp = prev
            prev = nums[shift]
            nums[shift] = tmp

            # shift up by k, make sure shift stays in bounds
            shift += k
            if shift>length-1:
                shift-=length

            # if cycle detected move up
            if shift==index:
                nums[index]=prev
                index+=1
                shift=index

            # inc count until we have used all numbers
            count+=1

# cycle way to solve problem
# count how many numbers in the array and shift by k
# only have to subtract once to get back in bounds because we do it instantly
# once cycle is detected we replace the last prev and move up

# alternative way is appending the back of the list to the front
# for example [1,2,3,4,5,6,7] shifted 3 is [5, 6, 7] + [1,2,3,4]
# the last 3 items of array are in the front now
