# Connect Four game
# given 6x7 grid, and an array represents p1 and p2 moves
# return the game board when the game is over
# additional rules
'''
- As soon as one of the players gets 4 discs in a row 
  (horizontally, vertically, or diagonally), the game is over (ignore all moves after that).

- If a player attempts to drop a piece into a column 
  that's already full, disregard that move (go on to the next player's turn).

- When outputting the grid, empty spaces are represented by " ", 
  while the two players' discs are represented by "0" and "1" respectively.
'''

def connectFour(moves):
    game_grid = [[" "]*7 for i in range(6)]
    
    def game_end(grid):
        from itertools import groupby as grb
        S = lambda a: any([i>=4 for i in a])
        C = lambda g: [sum(1 for _ in grp) for row in g for k,grp in grb(row) if not k == " "]

        h,w = len(grid),len(grid[0])
        
	# check horizontal
        horz = C(grid)
        if S(horz): return True
        
	# check vertical
        vert = C([[grid[i][j] for i in range(h)] for j in range(w)])
        if S(vert): return True
        
	# check diagonal /
        diag_mat = [[grid[h - p + q - 1][q] for q in range(max(p-h+1, 0), min(p+1, w))] for p in range(h + w - 1) ]
        diag = C(diag_mat)
        if S(diag): return True
        
	# check antidiagonal \
        a_diag_mat = [[grid[p - q][q] for q in range(max(p-h+1,0), min(p+1, w))] for p in range(h + w - 1)]
        a_diag = C(a_diag_mat)
        if S(a_diag): return True
        
        return False
        
    
    for index,move in enumerate(moves):
        if game_end(game_grid):
            break
        if index%2:
            for i in range(5,-1,-1):
                if game_grid[i][move] == " ":
                    game_grid[i][move] = "1"
                    break
        else:
            for i in range(5,-1,-1):
                if game_grid[i][move] == " ":
                    game_grid[i][move] = "0"
                    break
                    
    return [''.join(i) for i in game_grid]
