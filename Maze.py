import random #Introduce the random module of Python for generating random integers.

# Generate a maze
def generate_maze(n):
    maze = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]
    maze[0][0] = random.randint(1, n)  # Start
    maze[n-1][n-1] = 0  # End
    return maze

# Print the Maze
def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))

# Move function: Move from the current position
def move(maze, x, y, command, steps):
    n = len(maze)
    max_steps = maze[y][x]  # The maximum steps allowed from current position
    
    # Ensure the number of steps doesn't exceed the maximum allowed
    if steps > max_steps:
        print(f'You cannot move {steps} steps. The maximum allowed is {max_steps}.')
        return x, y
    
    if command == 'up' and y - steps >= 0:
        return x, y - steps
    elif command == 'down' and y + steps < n:
        return x, y + steps
    elif command == 'left' and x - steps >= 0:
        return x - steps, y
    elif command == 'right' and x + steps < n:
        return x + steps, y
    else:
        print("Invalid movement. You can't go outside the maze.")
        return x, y  # Invalid movement, return to the original position

# Check if the game is won
def check_win(x, y, n):
    return x == n-1 and y == n-1

# Main Program
def play_game():
    while True:
        n = int(input('Please enter the size of the maze: '))
        if n < 2:
            print('The size of the maze must be at least 2. Please enter again:  ')
            continue
        break

    maze = generate_maze(n)
    print("Welcome to the Digital Maze!")
    print_maze(maze)
    
    x, y = 0, 0  # Start
    move_count = 0 #Count how many steps the players used
    while True:
        if check_win(x, y, n):
            print("Congratulations! You have successfully reached the finish line!")
            print('')
            print(f'You used {move_count} steps to reach the finish line')
            print('')
            name = input('Please enter your name to record your score: ')

            with open('records.txt', 'a') as file:
                file.write(f'{name} - {move_count} steps\n')
            
            print("Your score has been saved to 'records.txt'.")
            break
        
        print(f"Current position: ({x}, {y}), Current maximum steps: {maze[y][x]}")
        command = input("Please enter the command of movement (up, down, left, right, quit): ").lower()
        if command == 'quit':
            print('Successfully quit!')
            break
        # Get the step count
        steps = int(input(f"Enter the number of steps you want to move (max {maze[y][x]}): "))
        
        # Movement
        new_x, new_y = move(maze, x, y, command, steps)
        
        # If the movement is valid, update the player's position
        if (new_x, new_y) != (x, y):
            x, y = new_x, new_y
            move_count += 1
            print_maze(maze)
        else:
            print("Invalid movement. Please reselect!")
            print_maze(maze)
        
# Start the game
play_game()
