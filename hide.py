#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : Neha Pai; nrpai@iu.edu
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# # Add a friend to the board at the given position, and return a new board (doesn't change original)
# def add_friend(board, row, col):
#     return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# # Get list of successors of given board state
# def successors(board):
#     succ = []
#     for r in range(0, len(board)):
#         for c in range(0,len(board[0])):
#             if board[r][c] == '.':
#                 b = add_friend(board, r, c)
#                 if is_valid(b,r,c):
#                     succ.append(b)
#     return succ

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row):
    for col in range(0,len(board[0])):
        if board[row][col] == '.':
            board = board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]
            if is_valid(board,row,col) == False:
                board[row][col] = '.'
    return board


# Get list of successors of given board state
def successors(board):
    succ = []
    for r in range(0, len(board)):
        b = add_friend(board,r)
        succ.append(b)
    return succ

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

def is_valid(board,r,c):
    l = [x for x in board[r] if x != '.' and x != '#']
    for i in range(0,len(l)-1):
        if l[i] == 'F' and l[i+1] == 'F':
            return False      
    l = [board[r][c] for r in range(0,len(board)) if board[r][c] != '.' and board[r][c] != '#']
    for i in range(0,len(l)-1):
        if l[i] == 'F' and l[i+1] == 'F':
            return False 
    return True

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    visited = []
    while len(fringe) > 0:
        suc = successors(fringe.pop())
        if suc != []:
            for s in suc:
                if s not in visited:
                    fringe.append(s)
                if is_goal(s):
                    return(s)
                visited.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("\nHere's what we found:")
    print (printable_board(solution) if solution else "None")


