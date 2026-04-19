if __name__ == '__main__':
    N = int(input())
    operators = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse'] 
    result = []
    # for N input 
    for _ in range(N): 
        input_ = input()
    # determine the operator
    # split by space and get the first element
        modified_input = input_.split(' ')
        # is operator valid?
        if modified_input[0] not in operators: 
            SystemExit 
    # insert
        if modified_input[0] == 'insert':
            # get the position i and the integer e 
            result.insert(int(modified_input[1]), int(modified_input[2]))
    # print
        if modified_input[0] == 'print': 
            print(result)
    # remove
        if modified_input[0] == 'remove': 
            result.remove(int(modified_input[1]))
    # append
        if modified_input[0] == 'append': 
            result.append(int(modified_input[1])) 
    # sort
        if modified_input[0] == 'sort': 
            result.sort()
    # pop
        if modified_input[0] == 'pop': 
            result.pop()
    # reverse
        if modified_input[0] == 'reverse': 
            result = result[::-1]
