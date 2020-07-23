'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here

    mx = [0] * (len(nums) - k + 1)

    mx[0] = max(nums[:k])
    for i in range(1, len(nums) - k + 1):
        if nums[i - 1] == mx[i -1]:
            mx[i] = max(nums[i:i + k])
        else:
            mx[i] = max(mx[i - 1], nums[i + k - 1])
    
    return mx


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
