import math

# function to find maximum contiguous sub array
def find_max_sub_array(arr):
    max_ending_here = 0
    max_so_far = -(math.inf)
    start = 0
    end = 0
    s = 0

    # loop for each element in arr[1..n]
    for i in range(0, len(arr)):
        max_ending_here += arr[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return (max_so_far, start, end)


# driver code to test the implementation
a =  [1,2,-3,5] 

sub_sum, sub_start, sub_end = find_max_sub_array(a)

print(a[sub_start:sub_end + 1]) 
print(f'Sub Array sum: {sub_sum}')   
