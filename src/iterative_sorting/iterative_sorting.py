# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr

# print(selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1] , arr[j]
            j-=1
    return arr


# # STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    if arr == []:
        return []

    if maximum == -1:
        maximum = max(arr)

    newList = [0 for i in range(maximum + 1)]
    returnList = []
    for n in arr:
        if n < 0:
            return "Error, negative numbers not allowed in Count Sort"
        newList[n] += 1
    for x in range(len(newList)):
        if newList[x] != 0:
            returnList += [x for n in range(newList[x])]

    return returnList

