from constants import *
import pygame

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col *width
        self.color= WHITE
        self.neighbours =[]

    def getPos(self):
        return self.row,self.col
    
    def isClosed(self):
        return self.color == BLUE
    
    def isOpen(self):
        return self.color == YELLOW
    
    def isStart(self):
        return self.color == ORANGE
    
    def isEnd(self):
        return self.color == RED
    
    def isPath(self):
        return self.color == GREEN
    
    def isWall(self):
        return self.color == BLACK
    
    def reset(self):
        self.color = WHITE
    
    def setClosed(self):
        self.color = BLUE
    
    def setOpen(self):
        self.color = YELLOW
    
    def setWall(self):
        self.color = BLACK
    
    def setEnd(self):
        self.color = RED
    
    def setStart(self):
        self.color = ORANGE

    def setPath(self):
        self.color = GREEN
        
    def draw(self ,win):
        pygame.draw.rect(win, self.color,(self.x,self.y,self.width,self.width))

    def updateNeighbour(self,grid):
        self.neighbours = []
        if self.row< self.total_rows-1 and not grid[self.row+1][self.col].isWall():
            self.neighbours.append(grid[self.row+1][self.col])

        if self.row > 0 and not grid[self.row-1][self.col].isWall():
            self.neighbours.append(grid[self.row-1][self.col])

        if self.col<self.total_rows-1 and not grid[self.row][self.col+1].isWall():
            self.neighbours.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].isWall():
            self.neighbours.append(grid[self.row][self.col-1])

    def __lt__(self, value):
        return False