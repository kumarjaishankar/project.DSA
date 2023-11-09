import random
import numpy as np
from colorama import Fore, init

init(autoreset=True)

class Maze:
    def __init__(self, size):
        self.size = size
        self.maze = np.random.choice([0, 1], size=(size, size))
        self.maze[0, 0] = 0
        self.maze[size - 1, size - 1] = 0

    def print_maze(self):
        for row in self.maze:
            for cell in row:
                if cell == 0:
                    print(Fore.BLUE + ".", end=" ")
                elif cell == 1:
                    print(Fore.RED + "X", end=" ")
            print()

    def find_path(self):
        pass

    def print_path(self, path):
        pass

def main():
    print("Welcome to the Maze Generator and Solver!")
    size = int(input("Enter the size of the maze (n x n): "))

    maze = Maze(size)

    while True:
        print("\nGenerated Maze:")
        maze.print_maze()

        print("\nOptions:")
        print("1. Print the path")
        print("2. Generate another puzzle")
        print("3. Exit the Game")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            path = maze.find_path()
            if path:
                print("\nFound Path:")
                maze.print_path(path)
            else:
                print("No path found.")
        elif choice == '2':
            size = int(input("Enter the size of the maze (n x n): "))
            maze = Maze(size)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
