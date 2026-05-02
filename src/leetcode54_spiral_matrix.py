# walk right, hit the wall, then record the position 
def walk_right(matrix, row, left_bound, right_bound, result): 
    for i in range(left_bound, right_bound): 
        result.append(matrix[row][i])
    return result
# walk down, hit the wall, then record the position 
def walk_down(matrix, column, result, lower_bound, up_bound): 
    for i in range(up_bound, lower_bound): 
        result.append(matrix[i][column])
    return result
# walk left, hit the wall, then record the position 
def walk_left(matrix, row, left_bound, right_bound, result): 
    current = right_bound - 1
    while current != left_bound - 1: 
        result.append(matrix[row][current])
        current -= 1
    return result
# walk up, hit the wall, then record the positon 
def walk_up(matrix, column, result, lower_bound, up_bound): 
    current = lower_bound - 1
    while current != up_bound - 1: 
        result.append(matrix[column][current])
        current -= 1
    return result

if __name__ == "__main__": 
    # record the final result path 
    result = []
    # initialize matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # wall1 -> up_bound
    up_bound = 0
    # wall 2 -> right_bound
    right_bound = len(matrix[0])
    # wall 3 -> lower_bound
    lower_bound = len(matrix)
    # wall 4 -> left_bound
    left_bound = 0
    # test 
    # end: when the wall is the next path 
    # intialize row and column
    row = 0
    column = right_bound - 1
    for i in range(3): 
        result = walk_right(matrix=matrix, row=row, left_bound=left_bound, right_bound=right_bound, result=result)
        # update upper_bound 
        up_bound += 1 
        print(f'result after walking right: {result}')
        result = walk_down(matrix=matrix, column=column, result=result, lower_bound=lower_bound, up_bound=up_bound)
        # update right_bound 
        right_bound -= 1
        print(f'result after walking down: {result}')
        result = walk_left(matrix=matrix, row=row, left_bound=left_bound, right_bound=right_bound, result=result)
        # update lower_bound
        lower_bound -= 1
        print(f'result after walking left: {result}')
        result = walk_up(matrix=matrix, column=column, result=result, lower_bound=lower_bound, up_bound=up_bound)
        # update left_bound 
        left_bound += 1
        print(f'result after walking up: {result}')
    print(result)
