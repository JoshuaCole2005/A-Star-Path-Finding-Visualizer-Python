import pygame

#Colors
#Empty color
BLACK = (0, 0, 0)
#Start Color
RED = (255, 0, 0)
#End Color
BLUE = (64, 224, 208)
#Open Color
GREEN = (0, 255, 0)
#Barrier color
GRAY = (128, 128, 128)
#Path Color
PURPLE = (128, 0, 128)
#Closed Color
LIGHT_BLUE = (79, 107, 247)


def get_color(node_type):
    if node_type == "empty":
        return BLACK
    elif node_type == "start":
        return RED
    elif node_type == "end":
        return BLUE
    elif node_type == "open":
        return GREEN
    elif node_type == "barrier":
        return GRAY
    elif node_type == "path":
        return PURPLE
    elif node_type == "closed":
        return LIGHT_BLUE
    else:
        raise NotImplementedError


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = "empty"
        self.neighbors = []

    def get_pos(self):
        return self.row, self.col

    def is_type(self, node_type):
        return self.type == node_type
    
    def set_type(self, node_type):
        self.type = node_type

    def draw(self, screen, width):
        pygame.draw.rect(screen, get_color(self.type), ((self.row * width), (self.col * width), width, width))
    
    def set_neighbors(self, board, total_rows, diags=False):
        if not diags:
            if self.row < total_rows - 1 and not board[self.row + 1][self.col].is_type("barrier"):
                self.neighbors.append(board[self.row + 1][self.col])
            if self.row > 0 and not board[self.row - 1][self.col].is_type("barrier"): 
                self.neighbors.append(board[self.row - 1][self.col])
            if self.col < total_rows - 1 and not board[self.row][self.col + 1].is_type("barrier"):
                self.neighbors.append(board[self.row][self.col + 1])
            if self.col > 0 and not board[self.row][self.col - 1].is_type("barrier"):
                self.neighbors.append(board[self.row][self.col - 1])
        else:
            if self.row < total_rows - 1 and not board[self.row + 1][self.col].is_type("barrier"):
                self.neighbors.append(board[self.row + 1][self.col])
            if self.row > 0 and not board[self.row - 1][self.col].is_type("barrier"):
                self.neighbors.append(board[self.row - 1][self.col])
            if self.col < total_rows - 1 and not board[self.row][self.col + 1].is_type("barrier"):
                self.neighbors.append(board[self.row][self.col + 1])
            if self.col > 0 and not board[self.row][self.col - 1].is_type("barrier"):
                self.neighbors.append(board[self.row][self.col - 1])
            if self.row < total_rows - 1 and self.col > 0 and not board[self.row + 1][self.col - 1].is_type("barrier"):
                self.neighbors.append(board[self.row + 1][self.col - 1])
            if self.row < total_rows - 1 and self.col < total_rows - 1 and not board[self.row + 1][self.col + 1].is_type("barrier"): 
                self.neighbors.append(board[self.row + 1][self.col + 1])
            if self.row > 0 and self.col > 0 and not board[self.row - 1][self.col - 1].is_type("barrier"):
                self.neighbors.append(board[self.row - 1][self.col - 1])
            if self.row > 0 and self.col < total_rows - 1 and not board[self.row - 1][self.col + 1].is_type("barrier"):
                self.neighbors.append(board[self.row - 1][self.col + 1])
