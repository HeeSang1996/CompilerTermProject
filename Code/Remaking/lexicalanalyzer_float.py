import sys

class LexicalAnalyzer(object):

    # Token Definition
    VARIABLE = ['int', 'float','char', 'bool']
    KEYWORD = ['if', 'else', 'while', 'for', 'return']
    LOGIC = ['true', 'false']
    OPERATOR = ['-', '+', '*', '/', '<<', '>>', '&', '|']
    COMPARISON = ['<', '>', '==', '!=', '<=', '>=']
    WHITESPACE = ['\t', '\n', ' ']
    BRACE = ['{', '}']
    PAREN = ['(', ')']
    ASSIGN = ['=']
    TERM = [';']
    COMMA = [',']
    MERGE = BRACE + PAREN + TERM + COMMA + OPERATOR[1:] + COMPARISON

    # Alphabet Definition
    LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q,' 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    SYMBOL = ['&', '|', '+', '-', '*', '/', '<', '>', '"', '.', '_', '!'] + BRACE + PAREN + ASSIGN + TERM + COMMA
    ZERO = ['0']
    NON_ZERO = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    DIGIT = ZERO + NON_ZERO
    ALPHABET = LETTER + DIGIT + SYMBOL + WHITESPACE

    # input text file
    input_stream = None

    def __init__(self):
        pass

    def __init__(self, file):
        # Get text file
        self.input_stream = file

    # ID DFA
    def is_id(self, input_string, char):
        sub_string = ""
        symbol = self.LETTER + self.ZERO + self.NON_ZERO + ['_']
        i = 0; j = 0
        final = [1, 2, 3, 4, 5, 6]
        transition_table = [[1, -1, -1, 2], [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6], \
                            [3, 4, 5, 6], [3, 4, 5, 6], [3, 4, 5, 6]]

        if char == "":
            char = self.input_stream.read(1)

        # Read string
        while char in symbol:
            input_string = input_string + char
            char = self.input_stream.read(1)

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

            if i == -1:
                return sub_string, False, char

        if i in final:
            return sub_string, True, char
        else:
            return sub_string, False, char

    # INT DFA
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

    # FLOAT DFA
    def is_float(self, input_string, char):
        state = ["T0", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"]
        recentState = state[0]

        sub_string1 = ""
        sub_string2 = ""
        buf_string = input_string

        if len(input_string) == 1:
            input = input_string
            input_string = ""
        read_flag = True

        while(True):
            if len(input_string) > 1:
                if len(buf_string)!=0:
                    input = buf_string[0]
                    buf_string = buf_string[1:]
                    read_flag = False
                if len(buf_string)==0:
                    read_flag = True

            if recentState == state[7] or recentState == state[8]:
                sub_string1 = sub_string2

            if recentState == state[0]:
                if input == "-":
                    recentState = state[1]
                    sub_string1 = sub_string1 + input
                    sub_string2 = sub_string1
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.ZERO:
                    recentState = state[2]
                    sub_string1 = sub_string1 + input
                    sub_string2 = sub_string1
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[3]
                    sub_string1 = sub_string1 + input
                    sub_string2 = sub_string1
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[1]:
                if input in self.ZERO:
                    recentState = state[2]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[3]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[2]:
                if input == ".":
                    recentState = state[4]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[3]:
                if input in self.ZERO:
                    recentState = state[5]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input == ".":
                    recentState = state[4]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[6]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[4]:
                if input in self.ZERO:
                    recentState = state[7]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[8]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[5]:
                if input in self.ZERO:
                    recentState = state[5]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input == ".":
                    recentState = state[4]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[6]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[6]:
                if input in self.ZERO:
                    recentState = state[5]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input == ".":
                    recentState = state[4]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[6]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf + input)
            elif recentState == state[7]:
                if input in self.ZERO:
                    recentState = state[9]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[8]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    return sub_string1, True, input
            elif recentState == state[8]:
                if input in self.ZERO:
                    recentState = state[9]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[8]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    return sub_string1, True, input
            elif recentState == state[9]:
                if input in self.ZERO:
                    recentState = state[9]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                elif input in self.NON_ZERO:
                    recentState = state[8]
                    sub_string2 = sub_string2 + input
                    if read_flag: input = self.input_stream.read(1)
                else:
                    buf = sub_string2.replace(sub_string1, "", 1)
                    return sub_string1, False, (buf+input)
            if input not in (self.DIGIT + ['.']):
                break
        if recentState == state[7] or recentState == state[8]:
            sub_string1 = sub_string2
            return sub_string1, True, input
        else:
            buf = sub_string2.replace(sub_string1, "", 1)
            return sub_string1, False, (buf+input)

    # Literal DFA
    def is_string(self, input_string, char):
        sub_string = ""
        symbol = self.LETTER + self.ZERO + self.NON_ZERO + [' ', '"']
        i = 0; j = 0
        final = [2]
        transition_table = [[1, -1, -1, -1, -1], [2, 3, 4, 5, 6], [-1, -1, -1, -1, -1], \
                            [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]

        if char == "":
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
            elif c in [' ']: j = 4
            else:
                return sub_string, False, char

            i = transition_table[i][j]
            sub_string = sub_string + c

            if i == -1:
                return sub_string, False, char

        if i in final:
            return sub_string, True, char
        else:
            return sub_string, False, char

    # Run Lexical Analyzer
    def run(self):
        flag = True
        line_num = 1
        sub_string = ""
        symbol_table = []

        while (True):
            # Check the character is read or not
            if flag:
                c = self.input_stream.read(1)
                flag = True

            # EOF
            if (c == "") and (sub_string == ""):
                break

            # Test the character is in the alphabet
            if c not in self.ALPHABET:
                error_noti = "Line" + str(line_num) + ": Wrong input stream"
                # Open file for writing Error
                try:
                    f = open(file_name[:-2]+'_error.out', 'w')
                except:
                    print("Fail to write file")
                    exit()

                for i in error_noti:
                    f.writelines(i)
                f.close()
                print(error_noti)
                exit()

            # Check the # of line
            if c == '\n':
                line_num = line_num + 1
                c = ""; flag = True
                continue

            # Ignore the white space
            if c in self.WHITESPACE:
                c = ""; flag = True
                continue

            # Attach the character to sub_string
            sub_string = sub_string + c
            c = ""; flag = True

            # Variable, Keyword, Logic
            if sub_string in self.LETTER:
                if c == "":
                    c = self.input_stream.read(1)
                    flag = False

                while (c in self.LETTER):
                    sub_string = sub_string + c
                    c = self.input_stream.read(1)

                if c == '_':
                    flag = False
                    continue
                
                if c in self.DIGIT:
                    flag = False
                    continue

                if sub_string in self.VARIABLE:
                    symbol_table.append(['VARIABLE', sub_string])
                    sub_string = ""
                    continue
                elif sub_string in self.KEYWORD:
                    symbol_table.append(['KEYWORD', sub_string])
                    sub_string = ""
                    continue
                elif sub_string in self.LOGIC:
                    symbol_table.append(['LOGIC', sub_string])
                    sub_string = ""
                    continue

            # ASSIGN, COMPARISON
            if sub_string in self.ASSIGN:
                if c == "":
                    c = self.input_stream.read(1)
                    flag = False

                # COMPARISON ==
                if sub_string + c in self.COMPARISON:
                    symbol_table.append(['COMPARISON', sub_string + c])
                    sub_string = ""
                    c = ""; flag = True
                    continue
                # ASSIGN
                else:
                    symbol_table.append(['ASSIGN', sub_string])
                    sub_string = ""
                    continue

            # Subtract
            if sub_string in ['-']:
                # if ('INT' or 'FLOAT' or 'ID') in symbol_table[-1]:
                if (len(symbol_table) != 0) and (('INT' in symbol_table[-1]) or \
                    ('FLOAT' in symbol_table[-1]) or ('ID' in symbol_table[-1]) or (')' in symbol_table[-1])):
                    symbol_table.append(['OPERATOR', sub_string])
                    print(symbol_table[-1])
                    sub_string = ""
                    continue

            # BRACE, PAREN, TERM, COMMA, OPERATOR, COMPARISON
            if sub_string in self.MERGE + ['!']:
                if sub_string in ['<', '>']:
                    if c == "":
                        c = self.input_stream.read(1)
                        flag = False
                    if c == sub_string:
                        symbol_table.append(['OPERATOR', sub_string + c])
                        sub_string = ""; flag = True
                        continue
                    elif sub_string + c in self.COMPARISON:
                        symbol_table.append(['COMPARISON', sub_string + c])
                        sub_string = ""; flag = True
                        continue

                if sub_string == '!':
                    if c == "":
                        c = self.input_stream.read(1)
                        flag = False
                    if c == '=':
                        symbol_table.append(['COMPARISON', sub_string + c])
                        sub_string = ""; flag = True
                        continue
                    else:
                        error_noti = "Line" + str(line_num) + ": Wrong input stream"
                        # Open file for writing Error
                        try:
                            f = open(file_name[:-2]+'_error.out', 'w')
                        except:
                            print("Fail to write file")
                            exit()

                        for i in error_noti:
                            f.writelines(i)
                        f.close()
                        print(error_noti)
                        exit()

                if sub_string in self.BRACE:
                    symbol_table.append(['BRACE', sub_string])
                elif sub_string in self.PAREN:
                    symbol_table.append(['PAREN', sub_string])
                elif sub_string in self.TERM:
                    symbol_table.append(['TERM', sub_string])
                elif sub_string in self.COMMA:
                    symbol_table.append(['COMMA', sub_string])
                elif sub_string in self.OPERATOR:
                    symbol_table.append(['OPERATOR', sub_string])
                elif sub_string in self.COMPARISON:
                    symbol_table.append(['COMPARISON', sub_string])
                sub_string = ""
                continue

            # FLOAT
            if sub_string[0] in self.DIGIT + ['-', '.']:
                sub_string, fact, c = self.is_float(sub_string, c)

                if fact:
                    symbol_table.append(['FLOAT', sub_string])
                    sub_string = ""
                else:
                    if sub_string=='-':
                        symbol_table.append(['OPERATOR', sub_string])
                        sub_string = ""
                    elif len(c) > 0:
                        symbol_table.append(['FLOAT', sub_string])
                        sub_string = c
                        c = ""
                        flag = True
                        continue
                    else:
                        symbol_table.append(['FLOAT', sub_string])
                        sub_string = ""
                        continue
                    '''else:
                        error_noti = "Line" + str(line_num) + ": Wrong input stream"
                        print(error_noti)
                        exit()'''

                if c != "":
                    flag = False
                    continue
                else:
                    flag = True
                    continue
                '''else:
                    error_noti = "Line" + str(line_num) + ": Wrong input stream"
                    # Open file for writing Error
                    try:
                        f = open(file_name[:-2]+'_error.out', 'w')
                    except:
                        print("Fail to write file")
                        exit()

                    for i in error_noti:
                        f.writelines(i)
                    f.close()
                    print(error_noti)
                    exit()'''

            # ID
            if sub_string[0] in self.LETTER + ['_']:
                sub_string, fact, c = self.is_id(sub_string, c)
                if fact:
                    symbol_table.append(['ID', sub_string])
                    sub_string = ""
                    if c != "":
                        flag = False
                        continue
                    else:
                        flag = True
                        continue
                else:
                    error_noti = "Line" + str(line_num) + ": Wrong input stream"
                    # Open file for writing Error
                    try:
                        f = open(file_name[:-2]+'_error.out', 'w')
                    except:
                        print("Fail to write file")
                        exit()

                    for i in error_noti:
                        f.writelines(i)
                    f.close()
                    print(error_noti)
                    exit()

            # String
            if sub_string[0] == '"':
                sub_string, fact, c = self.is_string(sub_string, c)
                if fact:
                    symbol_table.append(['LITERAL', sub_string])
                    sub_string = ""
                    if c != "":
                        flag = False
                        continue
                    else:
                        flag = True
                        continue
                else:
                    error_noti = "Line" + str(line_num) + ": Wrong input stream"
                    # Open file for writing Error
                    try:
                        f = open(file_name[:-2]+'_error.out', 'w')
                    except:
                        print("Fail to write file")
                        exit()

                    for i in error_noti:
                        f.writelines(i)
                    f.close()
                    print(error_noti)
                    exit()

        return symbol_table


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

    # Visualize the result
    for i in symbol_table:
        print(i[0], i[1])

    # Open file for writing result
    try:
        f = open(file_name[:-2]+'.out', 'w')
    except:
        print("Fail to write file")
        exit()

    for i in symbol_table:
        token = i[0]
        lexeme = i[1]
        f.writelines(token + ' ' + lexeme + '\n')
    f.close()
