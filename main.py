import sudoku

hard_grid = [[2, 0, 0, 5, 0, 7, 4, 0, 6],
             [0, 0, 0, 0, 3, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 2, 3, 0],
             [0, 0, 0, 0, 2, 0, 0, 0, 0],
             [8, 6, 0, 3, 1, 0, 0, 0, 0],
             [0, 4, 5, 0, 0, 0, 0, 0, 0],
             [0, 0, 9, 0, 0, 0, 7, 0, 0],
             [0, 0, 6, 9, 5, 0, 0, 0, 2],
             [0, 0, 1, 0, 0, 6, 0, 0, 8]]


if __name__ == '__main__':
    problem = hard_grid # sudoku.create_grid()

    if sudoku.solve_sudoku(problem, 0, 0):
        sudoku.print_solution(problem)
    else:
        print("Invalid Sudoku")
