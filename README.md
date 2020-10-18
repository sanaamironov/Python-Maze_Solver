# maze-solver-python

For this project, you will harness the computing power of Python to solve a maze, using a recursive search algorithm. You will need to understand algorithms, Python data structures, file I/O, and recursion to complete this project.

The maze will be rectangular, comprised of square spaces. The Maze Solver can move freely between two adjacent squares, as long as the movement is horizontal or vertical (no diagonal moves), and the way is not blocked by a wall. The dimensions, finishing square, and configuration of the maze are provided in a separate file. The starting square from which the maze solution is attempted is chosen by the user.

Your Maze Solver will start from the user's choice of starting position, and will search out a path to the finish square. It can travel right, down, left, or up, as long as it doesn't go through any walls. When it finds a solution, it will print out the successful path. If there is no successful path, it must print out that there is no solution.

Your Maze Solver must use a recursive algorithm. Starting from the start square, your algorithm will scan for all the adjacent squares it can legally travel to in the next step. For each candidate “next square,” it will first check that it has not already been there. If not, it will try adding that square to the path built so far, and will use recursion to find a path from that new square to the end. If that recursion fails, it moves on to the next candidate. If all “next square” candidates fail, this instance of the recursion itself fails.
