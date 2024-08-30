def max_subarray_sum(arr):
    large = arr[0]
    sec_l = arr[0]
    maxsum = 0
    for i in arr:
        if i > large:
            large = i
        for j in arr:
            if j > sec_l:
                sec_l = arr[-2]

    maxsum = large + sec_l
    return maxsum

    # Initialize variables to keep track of the maximum sum
    # Iterate through the list, updating the maximum sum as you go
    # Return the maximum sum found

num = [2,3,4,5,2,8,-1,6,5]
print(max_subarray_sum(num))

# print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Expected: 6 (The subarray [4, -1, 2, 1] has the largest sum)

