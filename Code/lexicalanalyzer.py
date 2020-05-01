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
    MERGE = VARIABLE + KEYWORD + LOGIC + BRACE + PAREN + TERM + COMMA
    LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q,' 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
    'a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    SYMBOL = ['&', '|', '+', '-', '/', '<', '>', '"', '.', '_']
    ZERO = ['0']
    NON_ZERO = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    DIGIT = ZERO + NON_ZERO
    ALPHABET = LETTER + DIGIT + SYMBOL + WHITESPACE + BRACE + PAREN + ASSIGN + TERM + COMMA

    input_strem = None

    def __init__(self):
        pass

    def __init__(self, file):
        self.input_strem = file

    def id_dfa(self, string):
        symbol = LETTER + ZERO + NON_ZERO + ['_']



    def run(self):
        line_num = 1
        sub_string = ""
        symbol_table = []

        for i in range(1, 9):
            c = self.input_strem.read(1)
            if c not in self.ALPHABET:
                print("Wrong character, Line: ", line_num)
                exit()

#$$$$$$$$$
# Core part
            if c in self.WHITESPACE:
                continue

            sub_string = sub_string + c
            
            # Variable, Keyword, LOGIC, BRACE, PAREN, TERM, COMMA
            if sub_string in self.MERGE:
                symbol_table.append(sub_string)
                sub_string = ""
                continue
            # OPERATOR
            if sub_string in self.OPERATOR:
                symbol_table.append(sub_string)
                sub_string = ""
                continue
            # ASSIGN
            if sub_string in self.ASSIGN:
                symbol_table.append(sub_string)
                sub_string = ""
                continue
            # ID
            
#$$$$$$$$$$$$$

        print(symbol_table)
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
    
