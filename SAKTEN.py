# to exit the program when the user input is not correct
import sys
try:
    t = int(input())
    # test input in these allowed limits
    if t>=1 and t<=300:
        pass
    else:
        # exit the program if not
        raise sys.exit()
except:
    # exit when no input is given
    # and this catches EOF(end of file) exception
    sys.exit()

# Initialize N,M,Q to keep track of the sum of n,m,q
# (should not exceed 3*10**5)
N,M,Q = 0,0,0
# iterate over test cases
while(t):
    t -= 1
    try:
        n,m,q = map(int,input().split())
        # if values of n,m,q out of constraint then exit.
        if n<1 or n>10**5 or m<1 or m>10**5 or q<1 or q>10**5:
            raise sys.exit()
    # catches EOF exception
    except:
        sys.exit()
      # as explained above
    N += n
    M += m
    Q += q

    # if the sum exceeds 3*10**5, stop execution
    if N > 3*(10**5) or M > 3*(10**5) or Q > 3*(10**5):
        raise sys.exit()

    # dictionary to keep track of which row,col gets repeated
    # and how many times
    row, col = {},{}
    # intialized to zero
    num_odd_row, num_odd_col = 0,0

    # iterate all the operations
    while q:
        q -= 1
        try:
            # r for row and c for column
            r,c = map(int,input().split())
            # if r and c out of matrix dimentions
            # then exit program
            if r<1 or r>n or c<1 or c>m:
                raise sys.exit()
            # catches eof exception
        except:
            sys.exit()

        # checks if the row is already in row or col dictionary
        # rcheck is boolean value true or false
        rcheck = (r in row.keys())
        # similarly ccheck for col
        ccheck = (c in col.keys())

        # if any of row or column is repeated
        if rcheck or ccheck:
            # if both repeated increment both by one
            if rcheck and ccheck:
                col[c] += 1
                row[r] += 1
            # else increment r, is the new row, set it to one
            # and increment c by one
            elif ccheck:
                col[c] += 1
                row[r] = 1
            # else increment c, is the new col, set it to one
            # and increment r by one
            elif rcheck:
                row[r] += 1
                col[c] = 1
            # this will not happen when both r and c are new
            # because the condition doesn't allow
            else:
                pass
        # if both points are new
        else:
            # set r to one
            row[r] = 1
            # set c to one
            col[c] = 1

    # number of odd rows or columns
    for i in row.values():
        # dictionary is (key,value) pair
        # for every value in row check if odd
        # if so, increment by one
        if i%2 == 1:
            # counts all odd rows
            num_odd_row += 1
    # same thing for col
    for i in col.values():
        if i%2 == 1:
            num_odd_col += 1
    # total odd points =
    # oddrow * evencol + oddcol * evenrow
    oddpts = (n-num_odd_row)*num_odd_col + (m-num_odd_col)*num_odd_row
    print(oddpts)
