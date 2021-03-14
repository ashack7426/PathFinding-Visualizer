from constants import *
import pygame
from queue import PriorityQueue

def h(p1, p2):
    x1,y1 =p1
    x2,y2 =p2
    return abs(x1-x2) +abs(y1-y2)

def reconstructPath(camefrom, end, draw, VISUALIZE):
    current =end
    while current in camefrom:
        current = camefrom[current]
        current.setPath()
        if VISUALIZE:
            draw()

def algorithm(draw, grid, start, end, VISUALIZE):
    count =0
    openSet= PriorityQueue()
    openSet.put((0, count, start))
    openSetHash={start}
    cameFrom ={}
    g_score={cube:float("inf") for rows in grid for cube in rows}
    f_score={cube:float("inf") for rows in grid for cube in rows}
    g_score[start]=0
    f_score[start]= h(start.getPos(),end.getPos())

    while not openSet.empty():
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        current  = openSet.get()[2]
        openSetHash.remove(current)
        if current == end:
            end.setEnd()
            reconstructPath(cameFrom, end , draw, VISUALIZE)
            start.setStart()
            return True
        
        for neighbour in current.neighbours:
            tempGscore = g_score[current]+1

            if tempGscore <g_score[neighbour]:
                cameFrom[neighbour]= current
                g_score[neighbour] =tempGscore
                f_score[neighbour] = tempGscore +h(neighbour.getPos(),end.getPos())
                if neighbour not in openSetHash:
                    count+=1
                    openSet.put((f_score[neighbour], count, neighbour))
                    openSetHash.add(neighbour)
                    if VISUALIZE:
                        neighbour.setOpen()     
        
        if VISUALIZE:
            draw()

        if current != start and VISUALIZE:
            current.setClosed()

    return False


