#Create grid / clear button
#Create clicking and barrier functions
#Create a drop box select with different algorithms (options for algoithms / points / run)



#implement each algorithm
from constants import *
import pygame
import math
from Algorithms import *
from Spot import *

win = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("PathFinding Visualizer")

def setGrid(rows, width):
    grid= []
    gap =width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)
            grid[i].append(spot)
    return grid

def drawGrid(win, rows , width):
    gap =width //rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))
        pygame.draw.line(win,GREY,(i*gap,0),(i*gap,width))

def draw(win, grid,rows , width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)
    
    drawGrid(win, rows, width)
    pygame.display.update()

def getClickedPos(pos, rows, width):
    x, y =pos
    gap =width//rows
    rows = x//gap
    col =  y//gap
    return rows,col

def main(win, width,ROWS):
    grid = setGrid(ROWS, width)

    run = True
    started = False

    start = None
    end = None
    VISUALIZE = True

    while run :
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue
            
            elif pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row , col = getClickedPos(pos,ROWS , width)
                spot= grid[row][col]
                if not start and spot!=end:
                    start=spot
                    spot.setStart()
                    spot.draw(win)
                elif not end and spot !=start:
                    end = spot
                    spot.setEnd()
                    spot.draw(win)
                elif spot != end and spot != start:
                    spot.setWall()
                    spot.draw(win)
               

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row , col = getClickedPos(pos,ROWS , width)
                spot= grid[row][col]
                if spot == start :
                    start = None
                elif spot ==end:
                    end =None 
                spot.reset()
                spot.draw(win)
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.updateNeighbour(grid)
                    pygame.display.set_caption("A* Algorithm")
                    algorithm(lambda: draw(win,grid,ROWS,width), grid ,start ,end, VISUALIZE)
                if event.key ==pygame.K_c:
                    start =None
                    end   =None
                    grid = setGrid(ROWS, width)
                    pygame.display.set_caption("PathFinding Visualizer")
                if event.key ==pygame.K_v:
                    if VISUALIZE:
                        VISUALIZE = False
                    else:
                        VISUALIZE = True

main(win, WIDTH, ROWS)





