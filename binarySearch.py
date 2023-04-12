def binarySearch(sortedArr, key, lowIndex, highIndex):
    if lowIndex > highIndex:
        return False
    else:
        midIndex = int((highIndex + lowIndex)/2)
        if sortedArr[midIndex] == key:
            return True
        elif sortedArr[midIndex] > key:
            return binarySearch(sortedArr,key,lowIndex,midIndex-1)
        else:
            return binarySearch(sortedArr,key,midIndex+1,highIndex)
