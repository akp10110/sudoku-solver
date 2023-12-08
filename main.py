def sudoku():
    sudoku_initial_to_solve = [
        [6,0,0,8,0,3,9,0,7],
        [2,0,8,0,0,9,0,5,0],
        [3,0,0,1,2,0,0,8,0],
        [0,0,0,4,9,0,3,0,5],
        [0,0,0,0,0,0,0,0,0],
        [9,0,3,0,1,2,0,0,0],
        [0,3,0,0,6,1,0,0,8],
        [0,2,0,9,0,0,5,0,1],
        [1,0,4,5,0,8,0,0,9]
        ]
    
    rows_length = len(sudoku_initial_to_solve)
    cols_length = len(sudoku_initial_to_solve[0])

    row = []
    col = []
    block = []

    for r in range(rows_length):
        row = []
        print('')
        print(f'========== Row {r} ==========')
        for c in range(cols_length):
            col = []
            block = []
            # Based on the current cell, find the row, column and block which needs to be checked
            
            # Find row
            row = sudoku_initial_to_solve[r]
            
            # Find col
            for ar in range(rows_length):
                col.append(sudoku_initial_to_solve[ar][c])

            # Find block
            br_min = 0
            br_max = 0
            bc_min = 0
            bc_max = 0
            if r >= 0 and r <= 2:
                br_min = 0
                br_max = 2
            elif r >= 3 and r <= 5:
                br_min = 3
                br_max = 5
            elif r >= 6 and r <= 8:
                br_min = 6
                br_max = 8

            if c >= 0 and c <= 2:
                bc_min = 0
                bc_max = 2
            elif c >= 3 and c <= 5:
                bc_min = 3
                bc_max = 5
            elif c >= 6 and c <= 8:
                bc_min = 6
                bc_max = 8

            for i in range(br_min, br_max+1):
                for j in range(bc_min, bc_max+1):
                    block.append(sudoku_initial_to_solve[i][j])
            

            print(row)
            print(col)
            print(f'{br_min}, {br_max} and {bc_min}, {bc_max}')
            print(block)
            print('')
    
sudoku()