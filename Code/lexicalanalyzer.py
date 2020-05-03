import sys

class LexicalAnalyzer(object):

    VARIABLE = ['int', 'float','char', 'bool']
    KEYWORD = ['if', 'else', 'while', 'for', 'return']
    LOGIC = ['true', 'false']
    OPERATOR = ['+', '-', '*', '/', '<<', '>>', '&', '|']
    COMPARISON = ['<', '>', '==', '!=', '<=', '>=']
    WHITESPACE = ['\t', '\n', ' ']
    BRACE = ['{', '}']
    PAREN = ['(', ')']
    ASSIGN = ['=']
    TERM = [';']
    COMMA = [',']
    MERGE = BRACE + PAREN + TERM + COMMA + OPERATOR + COMPARISON
    LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q,' 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    SYMBOL = ['&', '|', '+', '-', '/', '<', '>', '"', '.', '_', '!'] + BRACE + PAREN + ASSIGN + TERM + COMMA
    ZERO = ['0']
    NON_ZERO = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    DIGIT = ZERO + NON_ZERO
    ALPHABET = LETTER + DIGIT + SYMBOL + WHITESPACE

    input_stream = None

    def __init__(self):
        pass

    def __init__(self, file):
        self.input_stream = file

    def is_id(self, input_string, char):
        sub_string = ""
        symbol = self.LETTER + self.ZERO + self.NON_ZERO + ['_']
        final = [1, 2, 3, 4, 5, 6]
        i = 0; j = 0
        transition_table = [[1, -1, -1, 2], [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6], \
        [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6]]

        if char == "":
            char = self.input_stream.read(1)

        # Read string
        if char in symbol:
            input_string = input_string + char
            char = self.input_stream.read(1)
            while char in symbol:
                input_string = input_string + char
                char = self.input_stream.read(1)

        if char not in self.WHITESPACE + self.BRACE + self.PAREN + self.ASSIGN:
            input_string = input_string + char
            char = ""

        # Analyze
        for c in input_string:
            if c in self.LETTER: j = 0
            elif c in self.ZERO: j = 1
            elif c in self.NON_ZERO: j = 2
            elif c in ['_']: j = 3
            else:
                return sub_string, False, char

            tmp_i = i
            i = transition_table[i][j]
            sub_string = sub_string + c

            if i==-1:
                i = tmp_i
                break
        
        if i in final:
            return sub_string, True, char
        else:
            return sub_string, False, char

    def is_string(self, input_string, char):
        sub_string = ""
        symbol = self.LETTER + self.ZERO + self.NON_ZERO + [' ', '"']
        i = 0; j = 0
        final = [2]
        transition_table = [[1, -1, -1, -1, -1], [2, 3, 4, 5, 6], [-1, -1, -1, -1, -1],\
        [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6] ]

        if char == "":
            char = self.input_stream.read(1)

        # Read string
        if char in symbol:
            input_string = input_string + char
            char = self.input_stream.read(1)
            while char in symbol:
                input_string = input_string + char
                char = self.input_stream.read(1)

        # Analyze
        for c in input_string:
            if c in '"': j = 0
            elif c in self.LETTER: j = 1
            elif c in self.ZERO: j = 2
            elif c in self.NON_ZERO: j = 3
            elif c in ['_']: j = 4


            tmp_i = i
            i = transition_table[i][j]
            sub_string = sub_string + c

            if i==-1:
                i = tmp_i
                break
        
        if i in final:
            return sub_string, True, char
        else:
            return sub_string, False, char

    def is_int(self, input_string, char):
        state = ["T0", "T1", "T2", "T3", "T4", "T5"]
        recentState = state[0]


        for input in input_string:
            if recentState == state[0]:
                if input == "-":
                    recentState = state[1]
                elif input in self.ZERO:
                    recentState = state[2]
                elif input in self.NON_ZERO:
                    recentState = state[3]
                else:
                    return None, False, char
            elif recentState == state[1]:
                if input in self.NON_ZERO:
                    recentState = state[3]
                else:
                    return None, False, char
            elif recentState == state[2]:
                return None, False, char
            elif recentState == state[3]:
                if input in self.ZERO:
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[5]
                else:
                    return None, False, char
            elif recentState == state[4]:
                if input in self.ZERO:
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[5]
                else:
                    return None, False, char
            elif recentState == state[5]:
                if input in self.ZERO:
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[5]
                else:
                    return None, False, char
        if recentState == state[2] or recentState == state[3] or recentState == state[4] or recentState == state[5]:
            return input_string, True, char
        else:
            return None, False, char


    def is_float(self, input_string, char):
        state = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]
        recentState = state[0]

        for input in input_string:
            if recentState == state[0]:
                if input == "-":
                    recentState = state[1]
                elif input in self.ZERO:
                    recentState = state[2]
                elif input in self.NON_ZERO:
                    recentState = state[3]
                else:
                    None, False, char
            elif recentState == state[1]:
                if input in self.ZERO:
                    recentState = state[2]
                elif input in self.NON_ZERO:
                    recentState = state[3]
                else:
                    None, False, char
            elif recentState == state[2]:
                if input == ".":
                    recentState = state[4]
                else:
                    None, False, char
            elif recentState == state[3]:
                if input in self.ZERO:
                    recentState = state[5]
                elif input == ".":
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[6]
                else:
                    None, False, char
            elif recentState == state[4]:
                if input in self.ZERO:
                    recentState = state[7]
                elif input in self.NON_ZERO:
                    recentState = state[8]
                else:
                    None, False, char
            elif recentState == state[5]:
                if input in self.ZERO:
                    recentState = state[5]
                elif input == ".":
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[6]
                else:
                    None, False, char
            elif recentState == state[6]:
                if input in self.ZERO:
                    recentState = state[5]
                elif input == ".":
                    recentState = state[4]
                elif input in self.NON_ZERO:
                    recentState = state[6]
                else:
                    None, False, char
            elif recentState == state[7]:
                if input in self.ZERO:
                    recentState = state[9]
                elif input in self.NON_ZERO:
                    recentState = state[8]
                else:
                    None, False, char
            elif recentState == state[8]:
                if input in self.ZERO:
                    recentState = state[9]
                elif input in self.NON_ZERO:
                    recentState = state[8]
                else:
                    None, False, char
            elif recentState == state[9]:
                if input in self.ZERO:
                    recentState = state[9]
                elif input in self.NON_ZERO:
                    recentState = state[8]
                else:
                    None, False, char
        if recentState == state[7] or recentState == state[8]:
            return input_string, True, char
        else:
            return None, False, char







    def run(self):
        flag = True
        line_num = 1
        sub_string = ""
        symbol_table = []

        while (True):
        #for i in range(1, 72):
            if flag:
                c = self.input_stream.read(1)

            if c=="":
                break
            
            flag = True

            if c not in self.ALPHABET:
                print("Wrong character, Line: ", line_num)
                exit()

            # Check the line
            if c == '\n':
                line_num = line_num + 1
                c = ""
                continue

            # Ignore thre white space
            if c in self.WHITESPACE:
                c = ""
                continue

            sub_string = sub_string + c
            c = ""

            # Variable, Keyword, Logic
            if sub_string in self.LETTER:
                c = self.input_stream.read(1)
                while (c in self.LETTER):
                    sub_string = sub_string + c
                    c = self.input_stream.read(1)
                if sub_string in self.VARIABLE + self.KEYWORD + self.LOGIC:
                    symbol_table.append(sub_string)
                    sub_string = ""
                    flag = False
                    continue
                

            # BRACE, PAREN, TERM, COMMA, OPERATOR, COMPARISON
            if sub_string in self.MERGE:
                if sub_string in ['<', '>']:
                    if c == "":
                        c = self.input_stream.read(1)
                    if c == sub_string:
                        symbol_table.append(sub_string + c)
                        sub_string = ""
                        c = ""
                        continue
                    elif sub_string+c in self.COMPARISON:
                        symbol_table.append(sub_string + c)
                        sub_string = ""
                        c = ""
                        continue

                symbol_table.append(sub_string)
                sub_string = ""
                continue

            # ASSIGN, OPERATOR
            if sub_string in self.ASSIGN:
                c = self.input_stream.read(1)
                # Comparison ==
                if sub_string + c in self.COMPARISON:
                    symbol_table.append(sub_string + c)
                    sub_string = ""
                    c = ""
                    continue
                # ASSIGN
                else:
                    symbol_table.append(sub_string)
                    sub_string = ""
                    flag = False
                    continue

            # INTEGER & FLOAT
            if sub_string in self.DIGIT + ['-']:
                symbol = self.DIGIT + ['-', '.']
                if c == "":
                    c = self.input_stream.read(1)

                if c in symbol:
                    sub_string = sub_string + c
                    c = self.input_stream.read(1)
                    while c in symbol:
                        sub_string = sub_string + c
                        c = self.input_stream.read(1)

                flag_int = False
                if '.' in sub_string:
                    sub_string, fact, c = self.is_float(sub_string, c)
                else:
                    sub_string, fact, c = self.is_int(sub_string, c)
                    flag_int = True

                if fact:
                    symbol_table.append(sub_string)
                    sub_string = ""
                    if c != "":
                        flag = False
                        continue
                    else:
                        flag = True
                        continue
                else:
                    if flag_int:
                        print("Line", line_num, ": Wrong input stream - Integer")
                    else:
                        print("Line", line_num, ": Wrong input stream - Float")
                    exit()


            # ID
            if sub_string[0] in self.LETTER + ['_']:
                sub_string, fact, c = self.is_id(sub_string, c)
                if fact:
                    symbol_table.append(sub_string)
                    sub_string = ""
                    if c != "":
                        flag = False
                        continue
                    else:
                        flag = True
                        continue
                else:
                    print("Line", line_num, ": Wrong input stream - Identifier")
                    exit()

            # String
            if sub_string[0] == '"':
                sub_string, fact, c = self.is_string(sub_string, c)
                if fact:
                    symbol_table.append(sub_string)
                    sub_string = ""
                    if c != "":
                        flag = False
                        continue
                    else:
                        flag = True
                        continue
                else:
                    print("Line", line_num, ": Wrong input stream - String")
                    exit()

                    
        print(symbol_table)

        return 0

        #while (True):
        #    # Check the alphabet
        #    # Check the whitespace
        #    sub_string = 
        #    if ()


if __name__ == "__main__":
    # Check the input commend
    if len(sys.argv) != 2:
        print("Input error")
        exit()

    # Open file for reading
    try:
        file_name = sys.argv[1]
        f = open(file_name)
    except:
        print("Fail to read file")
        exit()

    # Run lexical Analyzer
    la = LexicalAnalyzer(f)
    symbol_table = la.run()

    # Close the file
    f.close()

    '''
    # Open file for writing
    try:
        f = open('test.out')
    except:
        print("Fail to open file")
        exit()
    '''
    
