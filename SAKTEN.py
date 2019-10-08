import sys
try:
  t = int(input())
  if t>=1 and t<=300:
    pass
  else:
    raise sys.exit()
except:
  sys.exit()

N,M,Q = 0,0,0  
while(t):
  t -= 1
  try:
    n,m,q = map(int,input().split())
    if n<1 or n>10**5 or m<1 or m>10**5 or q<1 or q>10**5:
      raise sys.exit()
  except:
    sys.exit()
  N += n
  M += m
  Q += q
   
  if N > 3*(10**5) or M > 3*(10**5) or Q > 3*(10**5):
      raise sys.exit() 
    
  row, col = {},{}
  num_odd_row, num_odd_col = 0,0
  
  while q:
    q -= 1
    try:
      r,c = map(int,input().split())
      if r<1 or r>n or c<1 or c>m:
        raise sys.exit()
    except:
      sys.exit()
    
    # checks if the row is already in row or col dictionary 
    rcheck = (r in row.keys())
    ccheck = (c in col.keys())
    
    # if any of row or column is repeated
    if rcheck or ccheck:
      if rcheck and ccheck:
        col[c] += 1
        row[r] += 1
      elif ccheck:
        col[c] += 1
        row[r] = 1
      elif rcheck:
        row[r] += 1
        col[c] = 1
      else:
        pass
   # if both points are new
    else:
      row[r] = 1
      col[c] = 1
  
  # number of odd rows or columns
  for i in row.values():
    if i%2 == 1:
      num_odd_row += 1
  for i in col.values():
    if i%2 == 1:
      num_odd_col += 1
  # total odd points : oddrow * evencol + oddcol * evenrow
  oddpts = (n-num_odd_row)*num_odd_col + (m-num_odd_col)*num_odd_row
  print(oddpts)
