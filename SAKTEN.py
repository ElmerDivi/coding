import sys   # to exit the program when the user input is not correct 
try:  
  t = int(input())
  if t>=1 and t<=300: # test input in these limits are aloud
    pass
  else:
    raise sys.exit()  # otherwise exit the program
except:
  sys.exit() # exit when user not given any input and enter this catches EOF(end of file) exception 

N,M,Q = 0,0,0  # this is initialize of N,M,Q to keep track the sum of n,m,q not exceed 3*10**5
while(t): # interate over test cases
  t -= 1
  try:
    n,m,q = map(int,input().split())
    if n<1 or n>10**5 or m<1 or m>10**5 or q<1 or q>10**5: # values of n,m,q if out of constraint then exit.
      raise sys.exit()
  except: # catches EOF exception
    sys.exit()
  N += n  # as explained above 
  M += m
  Q += q
   
  if N > 3*(10**5) or M > 3*(10**5) or Q > 3*(10**5): # if the sum exceeds the 3*10**5 it stops execution
      raise sys.exit() 
    
  row, col = {},{}  # the dictionary to keep track of which row,col get repeated and how many times 
  num_odd_row, num_odd_col = 0,0 # intialized to zero
  
  while q:  # iterate for all the operations
    q -= 1
    try:
      r,c = map(int,input().split()) # r for row and c for column
      if r<1 or r>n or c<1 or c>m: # if r and c out of matrix dimentions then exit program
        raise sys.exit()
    except: # catches eof exception
      sys.exit()
    
    # checks if the row is already in row or col dictionary 
    rcheck = (r in row.keys()) # rcheck is boolean value true or false
    ccheck = (c in col.keys()) # similarly ccheck for col
    
    # if any of row or column is repeated
    if rcheck or ccheck: # if any of row or column is repeated
      if rcheck and ccheck: # if both repeated increment both by one 
        col[c] += 1
        row[r] += 1
      elif ccheck: # else increment r is new row set it to one and increment c by one 
        col[c] += 1
        row[r] = 1
      elif rcheck: # else increment c is new col set it to one and increment r by one 
        row[r] += 1
        col[c] = 1
      else: # this never gone come in it when both r and c are new  becouse very condtion to enter this doesn't allow
        pass
   # if both points are new
    else:
      row[r] = 1 # set r to one
      col[c] = 1 # set c to one
  
  # number of odd rows or columns
  for i in row.values():
    if i%2 == 1: # dictionary is (key,value) pair , for every value in row check if odd increment by one 
      num_odd_row += 1 # counts all odd rows
  for i in col.values(): # same thing for col
    if i%2 == 1:
      num_odd_col += 1
  # total odd points : oddrow * evencol + oddcol * evenrow
  oddpts = (n-num_odd_row)*num_odd_col + (m-num_odd_col)*num_odd_row
  print(oddpts)
