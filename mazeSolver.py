# File: proj2.py
# Author: Sanaa Mironov
# Date: Nov 2, 2016
# Section: 04
# Description:
#  My program  is a maze soler. A maze is imported with user's desire starting point. Using recursivation search algorithm to find a path to finishing.
# Collaboration:
#   Collaboration was not allowed on this assignment. I did not collaborated with anyone.



OPEN = "0" 	# No wall blocking a side of the sqaure.
WALL = "1" 	# wall blocking a side of the sqaure

RIGHT = 0 	# Right side of the sqaure
BOTTOM = 1 	# Bottom of the sqaure
LEFT = 2 	# Left side of the sqaure
TOP = 3 	# Top of the sqaure

#def extract_file():	extract text file to create a 3-D Maze.
#Input: 	Text file 
#Output: 	Return 3-D maze, finished row, finished column
def extract_file(open_file):
	all_lines = open_file.readlines()

	first_line = all_lines[0]

	#extract first line from the file; save item as row and column
	first_line_stripped = first_line.strip()
	first_line_parts = first_line_stripped.split()
	label = string(first_line_parts[0])
	instruction = string(first_line_parts[1])
	destRst = 
	sourceRst = 
	immRst = int()

#format of file
#	 	LW        R0, 0(R9)
#LOOP:   ANDI      R3,R3,1

	
	
#def create_empty_board():	creates an empty maze
#Input: 	The number of rows and columns
#Output: 	Return an empty maze
def create_empty_board(rows, cols):
	maze = []
	for i in range(rows):
		lists = []
		for j in range(cols):
			lists.append("0")
		maze.append(lists)	
	return maze

		
#def cant_make_move(): 	Takes in a a maze and see if we are blocked by walls all around.  
#Input: 	Maze(3-D), the starting point(row and col)
#Output: 	Return Boolean(True or False)
def cant_make_move(maze,starting_row,starting_col):
	if maze[starting_row][starting_col][RIGHT] == WALL and maze[starting_row][starting_col][BOTTOM] == WALL and maze[starting_row][starting_col][LEFT] == WALL and maze[starting_row][starting_col][TOP] == WALL:
		return True	
	return False	
	
	
#def search_maze: 	Takes in a 3-D maze and finds the solution.
# Input: 	maze (3d list), current postion(current row, current column), finishing position(finish row, finish column), current path
#Output: 	returns successful path and boolean
def search_maze(maze,current_row,current_col,fin_row,fin_col,current_path):

	current_path.append((current_row,current_col))

	dead_end = cant_make_move(maze,current_row,current_col)

	# First base case checks if we are at our finishing position
	if (current_row,current_col) == (fin_row,fin_col):
		return True,current_path
	
	# second case checks to see if we have hit a dead end in our maze	
	elif  dead_end == True:
		return False,current_path
	
	else:
		if maze[current_row][current_col][RIGHT] == OPEN and (current_row,current_col +1) not in current_path:
			# call our funcation again saving it as a boolean and the path we've taken so far
			path, saved_path = search_maze(maze,current_row,current_col+1,fin_row,fin_col,current_path[:])
			#check to see if we can take the path == True and return if we can and the saved path.
			if path == True:
				return True, saved_path

		if maze[current_row][current_col][BOTTOM] == OPEN and (current_row +1 ,current_col) not in current_path:
			path, saved_path = search_maze(maze,current_row+1,current_col,fin_row,fin_col,current_path[:])
			if path == True:
				return True, saved_path

		if maze[current_row][current_col][LEFT] == OPEN and (current_row,current_col - 1) not in current_path:
			path, saved_path = search_maze(maze,current_row,current_col-1,fin_row,fin_col,current_path[:])
			if path == True:
				return True, saved_path


		if maze[current_row][current_col][TOP] == OPEN and (current_row - 1,current_col) not in current_path:	
			path, saved_path = search_maze(maze,current_row-1,current_col,fin_row,fin_col,current_path[:])
			if path == True:
				return True, saved_path
	
	return False,current_path

def main():
	print("Welcome to the Maze Solver!")
	file_name = input("Please enter the filename of the maze: ")
	open_file = open(file_name,'r')
	maze, fin_row,fin_col = extract_file(open_file)
	
	maze_nrows = len(maze)
	maze_ncols =  (len(maze[0]))

	starting_row = int(input("Please enter the starting row: "))
	while starting_row < 0 or starting_row > maze_nrows:  
		starting_row = int(input("Invalid, enter a number between 0 and " + str(maze_nrows - 1) + " (inclusive): "))

	starting_col = int(input("Please enter the starting column: "))	
	while starting_col < 0 or starting_col > maze_ncols: 
			starting_col = int(input("Invalid, enter a number between 0 and " + str(maze_ncols- 1) + " (inclusive): "))			


	path, saved_path = search_maze(maze,starting_row,starting_col,fin_row,fin_col,[])

	if path == True:
		print("Solution found!")
		for position in saved_path:
			print(position)
	else:
		print("No solution was found!")		
	

	open_file.close()

main()