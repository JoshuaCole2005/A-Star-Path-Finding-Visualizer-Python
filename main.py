import pygame
from algorithms import *
from node import Node

#Screen config
WIDTH = 800
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finding Visual")
#Line Color
WHITE = (255, 255, 255)
#Empty color
BLACK = (0, 0, 0)

def draw_board(screen, board, rows, cols, width, height):
    screen.fill(BLACK)
    for row in board:
        for node in row:
            node.draw(screen, width//rows)
    for i in range(rows):
        pygame.draw.line(screen, WHITE, (0, i * (width // rows)), (width, i * (width // rows)))
        for j in range(cols):
            pygame.draw.line(screen, WHITE, (j * (width // rows), 0), (j * (width // rows), height))
    pygame.display.update()

def mouse_pos(pos, rows, width):
    y, x = pos
    row = y // (width//rows)
    col = x // (width//rows)

    return row, col

def main(screen, width, height, diag, rows=20):
    board = []
    for i in range(rows):
        board.append([])
        for j in range(rows):
            node = Node(i, j)
            board[i].append(node)
    start = None
    end = None

    running = True
    while running:
        draw_board(screen, board, rows, rows, width, height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_pos(pos, rows, width)
                node = board[row][col]
                if not start and node != end:
                    start = node
                    node.set_type("start")
                
                elif not end and node != start:
                    end = node
                    node.set_type("end")

                elif node != end and node != start:
                    node.set_type("barrier")
            
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_pos(pos, rows, width)
                node = board[row][col]
                node.set_type("empty")
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start = None
                    end = None
                    board = []
                    for i in range(rows):
                        board.append([])
                        for j in range(rows):
                            node = Node(i, j)
                            board[i].append(node)
                if event.key == pygame.K_SPACE and start and end:
                    for row in board:
                        for node in row:
                            node.set_neighbors(board, rows, diags=diag)
                    agent = A_Star(board, lambda: draw_board(screen, board, rows, rows, width, height), diag=diag)
                    agent.find(start, end)

    pygame.quit()

if __name__ == "__main__":
    choice = input("Press Y for diags, and press anything else to continue: ")
    if choice == "Y" or choice == "y":
        diag = True
    else:
        diag = False
    rows = input("How many rows would you like? \n")
    if choice and rows:
        main(SCREEN, WIDTH, HEIGHT, diag, rows=int(rows))
