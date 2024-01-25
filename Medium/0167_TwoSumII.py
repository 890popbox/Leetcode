def twoSum(self, numbers, target):
    i, j = 0, len(numbers) - 1
    while numbers[i] + numbers[j] != target and i + 1 < j:
        if numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return [i + 1, j + 1]

    # A solution is guaranteed, the target will always be reached and array is in ascending order already
    # Use a pointer to view both left/right side of the array, move back and forward until left+right==total
