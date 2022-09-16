from queue import PriorityQueue
from tkinter import N
from heuristics import *
import pygame

class A_Star:
    def __init__(self, board, draw_board, diag=False):
        self.draw = draw_board
        self.board = board
        self.diag = diag
    def back_propogation(self, parents, curr):
        while curr in parents:
            curr = parents[curr]
            curr.set_type("path")
            self.draw()

    def find(self, start, end):
        num = 0
        start_f_score = 0
        open_set = PriorityQueue()
        open_set.put((start_f_score, num, start))
        parents = {}
        g_scores = {node: float("inf") for row in self.board for node in row}
        g_scores[start] = 0
        f_scores = {node: float("inf") for row in self.board for node in row}
        f_scores[start] = manhattan(start.get_pos(), end.get_pos()) if not self.diag else diagonal(start.get_pos(), end.get_pos())
        open_set_access = {start}

        running = True
        while not open_set.empty()and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        running = False
            
            curr = open_set.get()[2]
            open_set_access.remove(curr)

            if curr == end:
                self.back_propogation(parents, curr)
                end.set_type("end")
                return True

            for neighbor in curr.neighbors:
                g_score = g_scores[curr] + 1
                if g_score < g_scores[neighbor]:
                    parents[neighbor] = curr
                    g_scores[neighbor] = g_score
                    f_scores[neighbor] = g_score + (manhattan(neighbor.get_pos(), end.get_pos()) if not self.diag else diagonal(neighbor.get_pos(), end.get_pos()))
                    if neighbor not in open_set_access:
                        num += 1
                        open_set.put((f_scores[neighbor], num, neighbor))
                        open_set_access.add(neighbor)
                        neighbor.set_type("open")
            self.draw()

            if curr != start:
                curr.set_type("closed")
        return False