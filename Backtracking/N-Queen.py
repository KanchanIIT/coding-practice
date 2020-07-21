"""
https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
Given a 2d matrix, place N number of queen in a way so that no queen can attack to each other. A queen can attack
another queen if that queen are in same row or same column or in same diagonal from any side.
1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column.
   Do following for every tried row.
    a) If the queen can be placed safely in this row
       then mark this [row, column] as part of the
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to
       a solution then return true.
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to
       step (a) to try other rows.
3) If all rows have been tried and nothing worked,
   return false to trigger backtracking.

"""

# input
N = 4  # number of queen
M = 4  # the 4x4 matrix

# output
out = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],  # 1 means the placement of a queen.
    [0, 0, 1, 0],
]
