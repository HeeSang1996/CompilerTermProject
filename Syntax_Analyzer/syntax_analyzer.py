import sys
import os

class SyntaxAnalyzer(object):

    #terminals
    TERMINALS = ['vtype','num','float','literal','id','if','else','while','for',
                 'return','addsub','multdiv','assign','comp','semi','comma',
                 'lparen','rparen','lbrace','rbrace']
    
    #non-terminals
    NON_TERMINALS = ['CODE','VDECL','FDECL','ARG','MOREARGS','BLOCK','STMT','ASSIGN'
                     ,'RHS','EXPR','TERM','FACTOR','COND','RETURN','ELSE']

    #epsilon
    EPSILON = ['epsilon']

    #rules
    RULES = ['S → CODE',
             'CODE → VDECL CODE',
             'CODE → FDECL CODE',
             'CODE → epsilon',
             'VDECL → vtype id semi',
             'VDECL → vtype ASSIGN semi',
             'ASSIGN → id assign RHS',
             'FDECL → vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace',
             'ARG → vtype id MOREARGS',
             'ARG → epsilon',
             'MOREARGS → comma vtype id MOREARGS',
             'MOREARGS → epsilon',
             'BLOCK → STMT BLOCK',
             'BLOCK → epsilon',
             'STMT → VDECL',
             'STMT → ASSIGN semi',
             'STMT → if lparen COND rparen lbrace BLOCK rbrace ELSE',
             'STMT → while lparen COND rparen lbrace BLOCK rbrace',
             'STMT → for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace',
             'ELSE → else lbrace BLOCK rbrace',
             'ELSE → epsilon',
             'RHS → EXPR',
             'RHS → literal',
             'EXPR → TERM addsub EXPR',
             'EXPR → TERM',
             'TERM → FACTOR multdiv TERM',
             'TERM → FACTOR',
             'FACTOR → lparen EXPR rparen',
             'FACTOR → id',
             'FACTOR → num',
             'FACTOR → float',
             'COND → FACTOR comp FACTOR',
             'RETURN → return FACTOR semi']

    # Variables
    file = None         # input text file
    terminal_list = []     # input terminal

    def __init__(self, file):
        # Get text file
        self.file = file

    def readFile(self):
        lines = self.file.readlines()
        for line in lines:
            terminal = line.split()[0]
            self.terminal_list.append(terminal)

            #Print for debugging
            #print(terminal)

    def run(self):
        # Read file
        self.readFile()
        #Print for debugging
        print(self.terminal_list)
        #Print for debugging
        print(len(self.TERMINALS))
        #Print for debugging
        print(len(self.NON_TERMINALS))
        #Print for debugging
        print(len(self.RULES))
        return True

# Main function
if __name__ == "__main__":
    # Check the input commend
    if len(sys.argv) != 2:
        print("Input error")
        exit()

    # Check the file existence
    if os.path.isfile(sys.argv[1]):
        # Open file for reading
        try:
            file_name = sys.argv[1]
            f = open(file_name)
        except:
            print("Fail to read file")
            exit()
    else:
        print("Cannot find file")
        exit()
    
    sa = SyntaxAnalyzer(f)
    result = sa.run()

    # Close the file
    f.close()

    # Result
    if result:
        print("Accepted")
    else:
        print("Reject")

    
