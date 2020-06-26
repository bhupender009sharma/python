board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def solve(bo):                  # its the backtracking algo
    find = find_empty(bo)       # gets the coordinates of empty element it finds first
    if not find:                   # if it does not find any empty element , this means we have completed the board , and this is only possible when we have entered all the elements correctly
        return True             # so return true
    else:
        row ,col = find         # if we find empty element , then put its row value in row and its column value in col

    for i in range(1,10):           # now try each value from 1-9 in order at the empty element
        if valid(bo,i,(row,col)):   # now check if the value entered is valid or not
            bo[row][col] = i        # if value is valid , then save it

            if solve(bo):           # here we use recursion(back tracking) and check again if the board is solved yet
                return True         # if board is solved return true, it will occur when we reach at the last empty value, and we will start coming out of the recurion

            bo[row][col] = 0        # if the board is not solved, that means above if condition does not work, then we put that pos =0 and check next value from the loop

    return False                    # returns false when we have entered some wrong value and now we have to track back, it is the condition when you fitted right value in previous row (or column, depends on how you are solving sudoku , orizontally or vertucally)
                                    # but now when we go forward we found that  we should have put some another value at the previous empty_value(it occurs when we have more than 1 option to fit at an empty place)

def valid(bo , num, pos):
    # check row
    for i in range(len(bo)):                               # length of column or vertical length
        if bo[pos[0]][i] == num and pos[1] != i:    #pos[0] means 1 value of tuple (i,j) i.e. i.
            return False                            # if the num we just entered is repeated in row then return false and also we should not check it for the position at which we jus entered the num , i.e. pos[1] != i

    # check column
    for i in range(len(bo[0])):                            #length of row or horizontal length
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check for square box
    box_i = pos[0] // 3         # doing integer divison by 3 , and so the result will be 0,1 or 2.
    box_j = pos[1] // 3         # so now the positions of 9 square boxes can be defined by (box_i,box_j) and its values will be [0-2,0-2]

    for i in range(box_i * 3 , box_i*3 + 3 ):       # this will give actual position on the board of the element that we are going to check for the box
        for j in range(box_j *3, box_j*3 + 3):      # +3 is done so that it works upto the 3rd element in the box
            if bo[i][j] == num and (i,j)!= pos:
                return False

    return True                 # if all the above conditions fail then it means it is valid, and now we can move to the next empty place

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('------------------------')

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")             # end="" is used so after printing it does not goes to the next line and contnue checking in the same line

            if j == 8:
                print(bo[i][j])                 # so that for the last element , it goes to the next line
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)                # return empty element's row and column value

    return None

print_board(board)        #before solving
solve(board)        #solving...
print("----------------------------------------------")
print_board(board)        # after solving