import sys

ZERO = ['0']
NON_ZERO = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q,' 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_id(token):
    i = 0;
    j = 0
    final = [1, 2, 3, 4, 5, 6]
    transition_table = [[1, -1, -1, 2], [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6], \
                        [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6]]

    # Analyze
    for c in token:
        if c in LETTER:
            j = 0
        elif c in ZERO:
            j = 1
        elif c in NON_ZERO:
            j = 2
        elif c in ['_']:
            j = 3
        else:
            return False

        i = transition_table[i][j]

        if i == -1:
            return False

    if i in final:
        return True
    else:
        return False


if __name__ == "__main__":
    # Check the input commend
    token = '_a1214_bcd'
    result = is_id(token)
    print(result)
    
