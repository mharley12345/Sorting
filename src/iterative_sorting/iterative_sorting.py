# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
          # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
        cur_index = i
        smallest_index = cur_index
        for e in range(cur_index+1, len(arr)):
            if arr[cur_index] > arr[e]:
                cur_index = e
                  # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index],arr[smallest_index]
      



      




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    flag = True
    while flag is True:
        flag = False 
        for e in range(len(arr) -1):
            if arr[e] > arr[e+1]:
              flag = True
              arr[e], arr[e+1] = arr[e+1], arr[e]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr