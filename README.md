# SlidingBrickPuzzleSolver

The following Python program solves sliding brick puzzles of relatively complex sizes using a few different algorithms. It is functionally necessary that sliding brick puzzles given to the program are formatted in the expected format. That is, the first line of the puzzle must contain the height and width of the rest of the puzzle. Furthermore, the squares in the puzzle must follow the following key:
-1 = goal space
0 = empty
1 = wall
2 = goal block
3-infinity = obstacle blocks


This implementation requires the installation of Python3. Specifically, Python 3.7 was used in writing this software. Python 2 is not compatible with this program. Not every version of Python 3 was tested but the program has been tested in Python 3.6 (which tux has installed as python3) and Python 3.7
Python 3 can be downloaded from this web URL:
https://www.python.org/downloads/release/


This implementation can be run within a Linux environment by simply running "run.sh" which will run the Python process, assuming the environment has the correct installations installed.

This implementation can also be run within any interface that can read Python files. For example, any IDE that supports Python such as PyCharm would work.
This implementation can also be run at the command line. One needs only to preface the StateRepresentation.py file with the Python 3 python.exe, either by referencing the fully qualified path to your Python 3.7 installation directory, or by adding the Python 3.7 python.exe to your Windows PATH. If using Linux, there are multiple ways you could reference it too, such as creating an alias to the python.exe like 'alias python="path/to/python.exe"

Note: This implementation has been tested on both Windows and Linux, not Mac OSX


All files can be solved with all algorithms implemented in this program. The later puzzles may take some time to solve, however. In particular, iterative-deepening search takes very long to solve the latter puzzles. This is due to the intrinsic nature of iterative-deepening wherein it must necessarily repeat the searching of the beginning nodes of the tree many many times. And this is especially true of trees of very large size, such as the solution trees to the later puzzles. Iterative-deepening too will always eventually find a solution though given enough time to process the nodes.

There is also a file in this directory called 'output.txt' which contains the output of this program with time given for all algorithms to process some of the puzzles.