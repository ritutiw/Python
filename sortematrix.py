
# Python3 implementation 
# to search an element in a
# sorted matrix
MAX = 100



def binarySearch(mat, i, j_low,
                 j_high, x):
 
    while (j_low <= j_high):
     
        j_mid = (j_low + j_high) // 2
 
        # Element found
        if (mat[i][j_mid] == x):
         
            print("Found at (", i, ", ", j_mid, ")")
            return
 
        elif (mat[i][j_mid] > x):
            j_high = j_mid - 1
 
        else:
            j_low = j_mid + 1
    
    # Element not found
    print ("Element no found")
 
# Function to perform binary 
# search on the mid values of
# row to get the desired pair of rows
# where the element can be found
def sortedMatrixSearch(mat, n, m, x):
 
    # Single row matrix
    if (n == 1):
     
        binarySearch(mat, 0, 0, m - 1, x)
        return
 
    # Do binary search in middle column.
    # Condition to terminate the loop 
    # when the 2 desired rows are found
    i_low = 0
    i_high = n - 1
    j_mid = m // 2
    while ((i_low + 1) < i_high):
     
        i_mid = (i_low + i_high) // 2
 
        # element found
        if (mat[i_mid][j_mid] == x):
         
            print ("Found at (", i_mid, ", ", j_mid, ")")
            return
 
        elif (mat[i_mid][j_mid] > x):
            i_high = i_mid
 
        else:
            i_low = i_mid
 
    # If element is present on the mid of the
    # two rows
    if (mat[i_low][j_mid] == x):
        print ("Found at (" , i_low, ",", j_mid , ")")
    elif (mat[i_low + 1][j_mid] == x):
        print ("Found at (", (i_low + 1), ", ", j_mid, ")")
 
    # Ssearch element on 1st half of 1st row
    elif (x <= mat[i_low][j_mid - 1]):
        binarySearch(mat, i_low, 0, j_mid - 1, x)
 
    # Search element on 2nd half of 1st row
    elif (x >= mat[i_low][j_mid + 1] and
          x <= mat[i_low][m - 1]):
       binarySearch(mat, i_low, j_mid + 1, m - 1, x)
 
    # Search element on 1st half of 2nd row
    elif (x <= mat[i_low + 1][j_mid - 1]):
        binarySearch(mat, i_low + 1, 0, j_mid - 1, x)
  
    # Search element on 2nd half of 2nd row
    else:
        binarySearch(mat, i_low + 1, j_mid + 1, m - 1, x)
 
# Driver program to test above
if __name__ == "__main__":
 
    n = 2
    m = 3
    x = 2
    mat = [[1, 2, 3],
           [4,5,6]]
           
    sortedMatrixSearch(mat, n, m, x)
    
# This code is contributed by Ritu
#
