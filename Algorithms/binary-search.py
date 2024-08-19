""" ------------------------------------------------------------- 
    binary search implementation 
 ------------------------------------------------------------- """
def binarySearch(arr, target):
    left, right = 0, len(arr)-1
    return binarySearchHelper(arr, target, left, right)
    
def binarySearchHelper(arr, target, left, right):
    if left > right:
        raise Exception("no match")
    
    mid = (left+right)//2
    
    if arr[mid] == target:
        return print(mid)
    
    if arr[mid] < target:
        binarySearchHelper(arr, target, mid+1, right)
    else:
        binarySearchHelper(arr, target, left, mid-1)

array = [17,26,33,54,89,90,91]
binarySearch(array, 100)
