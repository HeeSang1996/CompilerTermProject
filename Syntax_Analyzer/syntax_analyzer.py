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
    RULES = {'0':'S → CODE',
             '1':'CODE → VDECL CODE',
             '2':'CODE → FDECL CODE',
             '3':'CODE → epsilon',
             '4':'VDECL → vtype id semi',
             '5':'VDECL → vtype ASSIGN semi',
             '6':'ASSIGN → id assign RHS',
             '7':'FDECL → vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace',
             '8':'ARG → vtype id MOREARGS',
             '9':'ARG → epsilon',
             '10':'MOREARGS → comma vtype id MOREARGS',
             '11':'MOREARGS → epsilon',
             '12':'BLOCK → STMT BLOCK',
             '13':'BLOCK → epsilon',
             '14':'STMT → VDECL',
             '15':'STMT → ASSIGN semi',
             '16':'STMT → if lparen COND rparen lbrace BLOCK rbrace ELSE',
             '17':'STMT → while lparen COND rparen lbrace BLOCK rbrace',
             '18':'STMT → for lparen ASSIGN semi COND semi ASSIGN rparen lbrace BLOCK rbrace',
             '19':'ELSE → else lbrace BLOCK rbrace',
             '20':'ELSE → epsilon',
             '21':'RHS → EXPR',
             '22':'RHS → literal',
             '23':'EXPR → TERM addsub EXPR',
             '24':'EXPR → TERM',
             '25':'TERM → FACTOR multdiv TERM',
             '26':'TERM → FACTOR',
             '27':'FACTOR → lparen EXPR rparen',
             '28':'FACTOR → id',
             '29':'FACTOR → num',
             '30':'FACTOR → float',
             '31':'COND → FACTOR comp FACTOR',
             '32':'RETURN → return FACTOR semi'}

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

    
