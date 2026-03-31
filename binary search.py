myList = [2,3,7,7,11,15,25]
target = 12
def binary_search(arr,targetVal):
    left=0
    right=len(arr)-1#6
    while left <= right:
        mid = (left+right)//2
        #now check if middlemost element is target item
        if myList[mid]==targetVal:
            return(mid)
        #compare the list's middle value to target and move in left if desired element is smaller else go right
        if myList[mid]<targetVal:
            left = mid+1
        else:
            right = mid-1
    return(-1)
result = binary_search(myList,target) 
if result != -1:
    print("found")
else:
    print("not found")