# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr1, arr2):
    # Your code here
    s1 = len(arr1) 
    s2 = len(arr2) 
    elems = s1 + s2 
    new_arr = [0] * elems
    i = 0
    j = 0
    k = 0
    
    while i < s1 and j < s2:
        if arr1[i] < arr2[j]:
            new_arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            new_arr[k] = arr2[j]
            j += 1
            k += 1
            
    while i < s1:
        new_arr[k] = arr1[i]
        k += 1
        i += 1
    while j < s2:
        new_arr[k] = arr2[j]
        k += 1
        j += 1

    return new_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):

    # Your code here
    # TODO:
    # step 1. keep splitting our arr until we have lists of length 1
    # step 2. building those lists make up by using our "merge" function


    return arr


# PLAN: 
# you need the index of the 0th elem in both arrays, i and j
# need the length of each array - we can represent this with s1 and s2 - size of 1st arr and size of 2nd arr
# empty array called merged_arr to filter the ordered elems
# continue the algorithm until all elems in both arrays have been checked - we can do this by using s1 and s2
# compare i and j - i and j are the 0th elem from each array
# if i is less than j then take i and make it equal to the 0th elem in the merged_arr
# increment both i and the merged_arr index - we will use k to represent the merged_arr index
# otherwise, if j is less than i take j and assign it to the 0th index of merged_arr
# j++ and k++ to increment after each check 
# sidenote - the lesser elem will always be shifted to the merged_arr
# when the while loop is broken, we have successfully checked all elems 
# if one arr is shorter than the other the while loop will be broken, what happens then? 
# we can make 2 other while loops after we break out of the first while loop to copy and paste the elems that are left into the merged_arr


















# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# TK Instructions
# def merge_sort( arr ):
#     if len( arr ) > 1:
#         # recursively call merge_sort() on LHS
#         # recursively call merge_sort() on RHS
#         # merge sorted pieces

# def merge_helper( a, b ):
#     merged_arr = []

#     # starting at the beginning of `a` and `b`
#     # compare the next value of each
#     # add smallest to `merged_arr`

#     return merged_arr

