import numpy as np
import pygame
import time


def createPolygon(x, y):

     return [(y * cell_width, x * cell_height),
         ((y + 1) * cell_width, x * cell_height),
         ((y + 1) * cell_width, (x + 1) * cell_height),
         (y * cell_width, (x + 1) * cell_height)]

def initializeGameState():
    running = True
    gameState = np.zeros((width_cells_number, height_cells_number)) # We set all the gameState matrix to 0s
    screen = pygame.display.set_mode((height, width)) # Initialize screen
    pygame.display.set_caption("Game of Life")        # Put some cool title
    screen.fill(background)
    while running:
        screen.fill(background)
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # If quit event is activated, stop the program
                running = False

            mouseClick = pygame.mouse.get_pressed() # If some click of the mouse is pressed, we interact with the gameState matrix
            if sum(mouseClick) > 0:
                posX, posY = pygame.mouse.get_pos()
                celX = int(np.floor(posX / cell_width))
                celY = int(np.floor(posY / cell_height))
                if mouseClick[0] == 1:              # Create alive cells if left click is pressed
                    gameState[celY, celX] = 1
                elif mouseClick[2] == 1:            # Create death cells if right click is pressed
                    gameState[celY, celX] = 0

            if event.type == pygame.KEYDOWN:
                running = False

        for x in range(0, height_cells_number):             # Iterate each row
            for y in range(0, width_cells_number):          # Iterate each column in a row
                # We design the cell
                polygon = createPolygon(y,x)
    
                # Put it on the screen
                if gameState[y, x] == 1:
                    pygame.draw.polygon(screen, (255, 255, 255), polygon, 0)

                else:
                    pygame.draw.polygon(screen, (128, 128, 128), polygon, 1)
                
        # Display it
        pygame.display.flip()

    return gameState
# Compute the total value of alive neighbours of a determinate cell
def getAliveNeighbours(gameState, x, y):
    return gameState[(y - 1) % width_cells_number, (x - 1) % height_cells_number] + \
           gameState[(y) % width_cells_number, (x - 1) % height_cells_number] + \
           gameState[(y - 1) % width_cells_number, (x) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number, (x -  1) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number , (x + 1) % height_cells_number] + \
           gameState[(y + 1) % width_cells_number, (x) % height_cells_number] + \
           gameState[(y) % width_cells_number, (x + 1) % height_cells_number] + \
           gameState[(y - 1) % width_cells_number, (x + 1) % height_cells_number]


def evaluteCell(gameState, x, y):
    if gameState[x, y] == 0:
        return [(128, 128, 128), 1]

    else:
        return [(255, 255, 255), 0]


def main():

    running = True
    pygame.init() # Initialize all pygame modules

    # Number 0 for dead cells, 1 for alive.
    gameState = initializeGameState()

    screen = pygame.display.set_mode((height, width)) # Initialize screen
    pygame.display.set_caption("Game of Life")        # Put some cool title
    screen.fill(background)


    while running:

        newGameState = np.copy(gameState)
        screen.fill(background)
        time.sleep(0.01)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # If quit event is activated, stop the program
                running = False
            
        for x in range(0, height_cells_number):             # Iterate each row
            for y in range(0, width_cells_number):          # Iterate each column in a row
                
                # Compute alive neighbours
                neighbours = getAliveNeighbours(gameState, x, y)

                # First rule: a death cell that has exactly 3 alive neighbours becomes alive
                if gameState[y, x] == 0 and neighbours == 3:
                    newGameState[y, x] = 1

                # Second rule: an alive cell that has les then 2 or more then 3 neighbours alive, dies
                elif(gameState[y, x] == 1 and neighbours < 2 or neighbours > 3):
                    newGameState[y, x] = 0

                # We design the cell
                polygon = createPolygon(x,y)
                
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

width_cells_number  = 100 # Number of cells in the total height of the screen
height_cells_number = 100 # Number of cells in the total width of the screen

height = 700 # Number of height pixels of the screen
width = 700  # Number of width pixels of the screen

background = (53, 53, 53, 1)        # Grey background color for the screen
polygon_colour = (0, 0, 0, 1)       # Black color for the cells margins


cell_height = height / height_cells_number      # Cells height
cell_width = width / width_cells_number         # Cells width

if __name__ == "__main__":
    main()
