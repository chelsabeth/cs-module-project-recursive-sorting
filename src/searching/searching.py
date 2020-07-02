# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # TODO:
    # find the length of the array
    # divide the length in half and get the mid
    # if mid is === target, return target
    # if mid is lower, go left
    # if mid is greater, go right
    # repeat steps

    # Recursive Traits:
    # base case = target
    # calls function on itself 
    if len(arr) <= 0:
        return -1
    mid = (len(arr) -1) // 2 

    while start != end:
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
        # go left and eliminate the mid and everything else on the right
            start = mid +1
        elif arr[mid] > target:
        # go right and eliminate the mid and everything else on the left
            end = mid -1
        mid = (end + start) // 2

    if arr[mid] == target:
        return mid
    return -1 # not found


# Iterative Binary Search 
#  # TODO:
#     # find the length of the array
#     # divide that in half and see if the mid is what we are looking for
#     # if the mid is the target, then return it
#     # if the mid is lower than our target, take the left side and divide that in half and compare
#     # if the mid is higher than our target, that the left side and divide that in half and compare
#     # repeat steps each time you divide in half 
#     # length = len(arr) -1
#     if len(arr) <= 0:
#         return -1
#     mid = (len(arr) -1) // 2 
#     low = 0 
#     high = len(arr) -1
#     # index = 0

#     while low != high:
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#         # go left and eliminate the mid and everything else on the right
#             low = mid +1
#         elif arr[mid] > target:
#         # go right and eliminate the mid and everything else on the left
#             high = mid -1
#         mid = (high + low) // 2

#     if arr[mid] == target:
#         return mid
#         # index += 1
#     return -1 # not found
        

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

