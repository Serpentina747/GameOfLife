import numpy as np
import pygame
import time

# Compute the total value of alive neighbours of a determinate cell
def getAliveNeighbours(gameState, x, y, width_cells_number, height_cells_number):
    return gameState[(y - 1) % width_cells_number, (x - 1) % height_cells_number] + \
           gameState[(y) % width_cells_number, (x - 1) % height_cells_number] + \
           gameState[(y - 1) % width_cells_number, (x) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number, (x -  1) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number , (x + 1) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number, (x) % height_cells_number] + \
           gameState[(y) % width_cells_number, (x + 1) % height_cells_number] + \
           gameState[(y - 1) % width_cells_number, (x + 1) % height_cells_number]


def  evaluteCell(gameState, x, y):
    if gameState[x, y] == 0:
        return [(128, 128, 128), 1]

    else:
        return ([255, 255, 255], 0)

pygame.init() # Initialize all pygame modules

running = True
width_cells_number  = int(input("Enter number of cells in a row: ")) # Number of cells in the total height of the screen
height_cells_number = int(input("Enter number of cells in a column: ")) # Number of cells in the total width of the screen

height = 700 # Number of height pixels of the screen
width = 700  # Number of width pixels of the screen

screen = pygame.display.set_mode((height, width)) # Initialize screen
pygame.display.set_caption("Game of Life")        # Put some cool title

background = (53, 53, 53, 1)        # Grey background color for the screen
polygon_colour = (0, 0, 0, 1)       # Black color for the cells margins
screen.fill(background)

cell_height = height / height_cells_number      # Cells height
cell_width = width / width_cells_number         # Cells width

# Number 0 for dead cells, 1 for alive.
gameState = np.zeros((width_cells_number, height_cells_number))

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1
while running:

    newGameState = np.copy(gameState)
    screen.fill(background)
    time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # If quit event is activated, stop the program
            running = False
            
    for x in range(0, height_cells_number):             # Iterate each row
        for y in range(0, width_cells_number):          # Iterate each column in a row
                
            # Compute alive neighbours
            neighbours = getAliveNeighbours(gameState, x, y, width_cells_number, height_cells_number)

            # First rule: a death cell that has exactly 3 alive neighbours becomes alive
            if gameState[y, x] == 0 and neighbours == 3:
                newGameState[y, x] = 1

            # Second rule: an alive cell that has les then 2 or more then 3 neighbours alive, dies
            elif(gameState[y, x] == 1 and neighbours < 2 or neighbours > 3):
                newGameState[y, x] = 0

            # We design the cell
            polygon = [(y * cell_width, x * cell_height),
                    ((y + 1) * cell_width, x * cell_height),
                    ((y + 1) * cell_width, (x + 1) * cell_height),
                    (y * cell_width, (x + 1) * cell_height)]

                
            # Evaluate if the cell is death or alive to return the drawn polygon type
            newValues = evaluteCell(gameState, x, y)
            # Put it on the screen
            pygame.draw.polygon(screen, newValues[0], polygon, newValues[1])

    gameState = np.copy(newGameState)
    # Display it
    pygame.display.flip()

pygame.display.quit()
pygame.quit()
exit()
