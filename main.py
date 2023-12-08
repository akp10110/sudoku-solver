def sudoku():
    sudoko_initial_to_solve = [
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
    
    for row in range(len(sudoko_initial_to_solve)):
        # print each column
        print(sudoko_initial_to_solve[row])
    
sudoku()