import random, time, copy
WIDTH= 60
HEIGHT= 20

""" Create a list of list for cells: """
nextCells = []
for x in range(WIDTH):
    column = [] # Create a column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Create a new column/
		else:
			column.append(' ') # add a dead cell
	nextCells.append(column) # nextCells is a list of column lists
        
while True: # main program loop
    print('\n\n\n\n\n') # separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    
    # Print currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # print the # or space.
        print() # print a new line at the end of the row