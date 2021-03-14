from constants import *
import pygame
from queue import PriorityQueue

def h(p1, p2):
    x1,y1 =p1
    x2,y2 =p2
    return abs(x1-x2) +abs(y1-y2)

def reconstructPath(camefrom, end, start, draw, VISUALIZE):
    current =end
    while current in camefrom and current != start:
        current = camefrom[current]
        current.setPath()
        if VISUALIZE:
            draw()


def algo(draw, grid, start, end, VISUALIZE, num):
    check = False

    if num == 1:
        check = Astar(draw, grid, start, end, VISUALIZE)
    elif num == 2:
        check = Dijkstras(draw, grid, start, end, VISUALIZE)
    elif num == 3:
        check = Breadth_first_search(draw, grid, start, end, VISUALIZE)
    elif num == 4:
        visited = {spot:False for rows in grid for spot in rows}
        cameFrom[start] = None
        check = Depth_first_search(draw, grid, start, end, VISUALIZE, cameFrom, visited)
    elif num == 5:
        check = best_first_search(draw, grid, start, end, VISUALIZE)
    

    return check


def Astar(draw, grid, start, end, VISUALIZE):
    count =0
    openSet= PriorityQueue()
    openSet.put((0, count, start))
    openSetHash={start}
    cameFrom ={}
    g_score={spot:float("inf") for rows in grid for spot in rows}
    f_score={spot:float("inf") for rows in grid for spot in rows}
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
            reconstructPath(cameFrom, end , start,draw, VISUALIZE)
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


def Dijkstras(draw, grid, start, end, VISUALIZE):
    pass

def Breadth_first_search(draw, grid, start, end, VISUALIZE):
    visited = {spot:False for rows in grid for spot in rows}
    queue = []
    cameFrom = {}

    queue.append(start)
    cameFrom[start] = None

    while queue:
        spot = queue.pop(0)

        if spot == end:
            end.setEnd()
            reconstructPath(cameFrom, end , start, draw, VISUALIZE)
            start.setStart()
            return True

        for neighbour in spot.neighbours:
            if neighbour not in cameFrom:
                queue.append(neighbour)
                cameFrom[neighbour] = spot

                if VISUALIZE:
                    neighbour.setOpen()   

        if VISUALIZE:
            draw()

        if spot != start and VISUALIZE:
            spot.setClosed()

    return False



def Depth_first_search(draw, grid, start, end, VISUALIZE, cameFrom, visited):
    pass




def best_first_search(draw, grid, start, end, VISUALIZE):
    visited = {spot:False for rows in grid for spot in rows}
    visited[start] = True
    pq = PriorityQueue()
    pq.put((0,start))
    count = 0
    cameFrom = {}
    cameFrom[start] = None

    while not pq.empty():
        spot = pq.get()[1]
        
        if spot == end:
            end.setEnd()
            reconstructPath(cameFrom, end , start, draw, VISUALIZE)
            start.setStart()
            return True

        for neighbour in spot.neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                cameFrom[neighbour] = spot
                pq.put((h(end.getPos(), neighbour.getPos()), neighbour))

                if VISUALIZE:
                    neighbour.setOpen()   

        if VISUALIZE:
            draw()

        if spot != start and VISUALIZE:
            spot.setClosed()

    return False
        

        
