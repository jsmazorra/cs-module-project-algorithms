'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    start = 0
    end = len(arr) - 1

    # Leave any initial trailing zeros in place.
    while end > start and arr[end] == 0:
        end -= 1

    # Swap non-trailing zeros, if any, with the last non-zero number.
    while start < end:
        if arr[start] == 0:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            start += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")