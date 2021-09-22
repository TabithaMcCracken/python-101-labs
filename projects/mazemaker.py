# Challenge yourself and practice learning from outside resources
# by following this tutorial to build a maze generator:
# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e

import random
import time
from colorama import init
from colorama import Fore, Back, Style

def printMaze(maze):
    for i in range(0,height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                print(Fore.WHITE + str(maze[i][j], end=""))
            elif (maze[i][j] == 'c'):
                print(Fore.GREEN + str(maze[i][j], end=""))
            else: 
                print(Fore.RED + str(maze[i][j], end=""))

        print('\n')
