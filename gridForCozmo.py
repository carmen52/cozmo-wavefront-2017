#build wavefront 
def buildWaveFront( x, y, n ):
  val = Matrix[y][x]
  if val == 0 or n+1 < val:
    Matrix[y][x] = n + 1
    
  #if its a corner cell
  if (x == 0 and y == 0):
    if (Matrix[y][x+1] == 0  or n+1 < Matrix[y][x+1]):
       buildWaveFront(x+1, y, n+1)
    if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
       buildWaveFront(x, y+1, n + 1)
  elif (x == 0 and y == len(Matrix) -1):
    if (Matrix[y][x+1] == 0 or n+1 < Matrix[y][x+1]):
       buildWaveFront(x+1, y, n + 1)
    if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
       buildWaveFront(x, y-1, n + 1)   
  elif (x == len(Matrix) - 1 and y == 0) :
    if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
       buildWaveFront(x-1, y, n + 1)
    if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
       buildWaveFront(x, y+1, n + 1)   
  elif (x == len(Matrix) - 1 and y == len(Matrix) - 1) :
    if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
       buildWaveFront(x-1, y, n + 1)
    if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
       buildWaveFront(x, y-1, n + 1)   
  #if its an edge
  else:
    if x == 0: 
      if (Matrix[y][x+1] == 0 or n+1 < Matrix[y][x+1]):
        buildWaveFront(x+1, y, n + 1)
      if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
        buildWaveFront(x, y+1, n + 1)
      if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
        buildWaveFront(x, y-1, n + 1)
    elif y == 0:
      if (Matrix[y][x+1] == 0 or n+1 < Matrix[y][x+1]):
        buildWaveFront(x+1, y, n + 1)
      if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
        buildWaveFront(x, y+1, n + 1)
      if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
        buildWaveFront(x-1, y, n + 1)
    elif x == len(Matrix) -1:
      if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
        buildWaveFront(x-1, y, n + 1)
      if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
        buildWaveFront(x, y+1, n + 1)
      if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
        buildWaveFront(x, y-1, n + 1)
    elif y == len(Matrix) -1:
      if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
        buildWaveFront(x-1, y, n + 1)
      if (Matrix[y][x+1] == 0 or n+1 < Matrix[y][x+1]):
        buildWaveFront(x+1, y, n + 1)
      if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
        buildWaveFront(x, y-1, n + 1)
    #else, not edge or corner
    else:
      if (Matrix[y][x-1] == 0 or n+1 < Matrix[y][x-1]):
        buildWaveFront(x-1, y, n + 1)
      if (Matrix[y][x+1] == 0 or n+1 < Matrix[y][x+1]):
        buildWaveFront(x+1, y, n + 1)
      if (Matrix[y-1][x] == 0 or n+1 < Matrix[y-1][x]):
        buildWaveFront(x, y-1, n + 1)
      if (Matrix[y+1][x] == 0 or n+1 < Matrix[y+1][x]):
        buildWaveFront(x, y+1, n + 1)
  return ''

#create 5x5 matrix
w, h = 5, 5;
Matrix = [[0 for x in range(w)] for y in range(h)] 

#set test values
Matrix[0] = ['s', 0, 0, 0, 0]
Matrix[1] = [0, 0, 1, 0, 0]
Matrix[2] = [0, 0, 1, 0, 0]
Matrix[3] = [0, 0, 1, 'g', 0]
Matrix[4] = [0, 0, 1, 0, 0]

#read from a file
file = open("5x5.txt", "r");
counter_y = -1
counter_x = 0
#read first line
line = file.readline()
size = line[0]
#create matrix
w, h = size, size;
Matrix = [[0 for x in range(w)] for y in range(h)] 
for line in file:
  for c in line:
    if counter_y > -1:
      Matrix[counter_y][counter_x] = c
    counter_x = counter_x + 1
  counter_y = counter_y + 1
  counter_x = 0
    
#initialize blocks to -1
#find goal
goalIndex_x = 0 
goalIndex_y = 0
for idx_y,row in enumerate(Matrix):
  for idx_x,c in enumerate(row):
    if c == 1:
      Matrix[idx_y][idx_x] = -1
    if c == 'g':
      Matrix[idx_y][idx_x] = -500
      goalIndex_x = idx_x
      goalIndex_y = idx_y
    if c == 's':
      Matrix[idx_y][idx_x] = -100
      goalIndex_x = idx_x
      goalIndex_y = idx_y
    print (c)
  print ("\n")

#call buildWaveFront starting at the goal  
buildWaveFront(goalIndex_x, goalIndex_y, -1)

#print out values
for idx_y,row in enumerate(Matrix):
  for idx_x,c in enumerate(row):
    print (c)
  print ("\n")



  
