
#supermode divide and conquer

def divideAndConquer(list):
    if(len(list)==1):
        return list[0]
    middle = len(list)//2
    left = list[:middle]
    right = list[middle:]
    cLeft = divideAndConquer(left)
    cRight = divideAndConquer(right)
    if cLeft == cRight:
        return cLeft
    if list.count(cLeft)>middle:
        return cLeft
    if list.count(cRight)>middle:
        return cRight
    return "No mode"




arr = [3,2,4,3,4,4,2,4,4]
arr2 = [3,2,4,3,4,4,2,4]
arr4 = [3,2,4,3,4,4,2,4,3,3,3,3,3]
arr5= [1,1,1,1,8,8,8,8,8]
arr6 = [1,1,1,8,8,8,8,8]
arr7 = [4,3,4,2,4,1,4]
arr8 = [4,3,4,2,4,1,4,4]
arr9 = [4,3,4,2,4,1,2]
arr10 = [8, 8, 8, 8, 8, 1, 1, 1, 1]


print(divideAndConquer(arr))
print(divideAndConquer(arr2))
print(divideAndConquer(arr4))
print(divideAndConquer(arr5))
print(divideAndConquer(arr6))
print(divideAndConquer(arr7))
print(divideAndConquer(arr8))
print(divideAndConquer(arr9))
print(divideAndConquer(arr10))
