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
    EPSILON ='epsilon'

    #end mark
    END_MARK ='$'

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

    # SLR table
    SLR_TABLE = [{'vtype': 'S3', '$': 'R(3)', 'CODE': 1, 'VDECL': 4, 'FDECL': 2},
                 {'$': 'R(0)'},
                 {'vtype': 'S3', '$': 'R(3)', 'CODE': 5, 'VDECL': 4, 'FDECL': 2},
                 {'id': 'S6', 'ASSIGN': 7},
                 {'vtype': 'S3', '$': 'R(3)', 'CODE': 8, 'VDECL': 4, 'FDECL': 2},
                 {'$': 'R(2)'},
                 {'assign': 'S10', 'semi': 'S11', 'lparen': 'S9'},
                 {'semi': 'S12'},
                 {'$': 'R(1)'},
                 {'vtype': 'S14', 'rparen': 'R(9)', 'ARG': 13},
                 {'num': 'S21', 'float': 'S20', 'literal': 'S16', 'id': 'S22', 'lparen': 'S23', 'RHS': 15, 'EXPR': 17, 'TERM': 18, 'FACTOR': 19},
                 {'vtype': 'R(4)', 'id': 'R(4)', 'if': 'R(4)', 'while': 'R(4)', 'for': 'R(4)', 'return': 'R(4)', 'rbrace': 'R(4)', '$': 'R(4)'},
                 {'vtype': 'R(5)', 'id': 'R(5)', 'if': 'R(5)', 'while': 'R(5)', 'for': 'R(5)', 'return': 'R(5)', 'rbrace': 'R(5)', '$': 'R(5)'},
                 {'rparen': 'S24'},
                 {'id': 'S25'},
                 {'semi': 'R(6)', 'rparen': 'R(6)'},
                 {'semi': 'R(22)', 'rparen': 'R(22)'},
                 {'semi': 'R(21)', 'rparen': 'R(21)'},
                 {'addsub': 'S26', 'semi': 'R(24)', 'rparen': 'R(24)'},
                 {'addsub': 'R(26)', 'multdiv': 'S27', 'semi': 'R(26)', 'rparen': 'R(26)'},
                 {'addsub': 'R(30)', 'multdiv': 'R(30)', 'comp': 'R(30)', 'semi': 'R(30)', 'rparen': 'R(30)'},
                 {'addsub': 'R(29)', 'multdiv': 'R(29)', 'comp': 'R(29)', 'semi': 'R(29)', 'rparen': 'R(29)'},
                 {'addsub': 'R(28)', 'multdiv': 'R(28)', 'comp': 'R(28)', 'semi': 'R(28)', 'rparen': 'R(28)'},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'EXPR': 28, 'TERM': 18, 'FACTOR': 19},
                 {'lbrace': 'S29'},
                 {'comma': 'S31', 'rparen': 'R(11)', 'MOREARGS': 30},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'EXPR': 32, 'TERM': 18, 'FACTOR': 19},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'TERM': 33, 'FACTOR': 19},
                 {'rparen': 'S34'},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 35, 'STMT': 36, 'ASSIGN': 38},
                 {'rparen': 'R(8)'},
                 {'vtype': 'S44'},
                 {'semi': 'R(23)', 'rparen': 'R(23)'},
                 {'addsub': 'R(25)', 'semi': 'R(25)', 'rparen': 'R(25)'},
                 {'addsub': 'R(27)', 'multdiv': 'R(27)', 'comp': 'R(27)', 'semi': 'R(27)', 'rparen': 'R(27)'},
                 {'return': 'S46', 'RETURN': 45},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 47, 'STMT': 36, 'ASSIGN': 38},
                 {'vtype': 'R(14)', 'id': 'R(14)', 'if': 'R(14)', 'while': 'R(14)', 'for': 'R(14)', 'return': 'R(14)', 'rbrace': 'R(14)'},
                 {'semi': 'S48'},
                 {'lparen': 'S49'},
                 {'lparen': 'S50'},
                 {'lparen': 'S51'},
                 {'id': 'S52', 'ASSIGN': 7},
                 {'assign': 'S10'},
                 {'id': 'S53'},
                 {'rbrace': 'S54'},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'FACTOR': 55},
                 {'return': 'R(12)', 'rbrace': 'R(12)'},
                 {'vtype': 'R(15)', 'id': 'R(15)', 'if': 'R(15)', 'while': 'R(15)', 'for': 'R(15)', 'return': 'R(15)', 'rbrace': 'R(15)'},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'FACTOR': 57, 'COND': 56},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'FACTOR': 57, 'COND': 58},
                 {'id': 'S43', 'ASSIGN': 59},
                 {'assign': 'S10', 'semi': 'S11'},
                 {'comma': 'S31', 'rparen': 'R(11)', 'MOREARGS': 60},
                 {'vtype': 'R(7)', '$': 'R(7)'},
                 {'semi': 'S61'},
                 {'rparen': 'S62'},
                 {'comp': 'S63'},
                 {'rparen': 'S64'},
                 {'semi': 'S65'},
                 {'rparen': 'R(10)'},
                 {'rbrace': 'R(32)'},
                 {'lbrace': 'S66'},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'FACTOR': 67},
                 {'lbrace': 'S68'},
                 {'num': 'S21', 'float': 'S20', 'id': 'S22', 'lparen': 'S23', 'FACTOR': 57, 'COND': 69},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 70, 'STMT': 36, 'ASSIGN': 38},
                 {'semi': 'R(31)', 'rparen': 'R(31)'},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 71, 'STMT': 36, 'ASSIGN': 38},
                 {'semi': 'S72'},
                 {'rbrace': 'S73'},
                 {'rbrace': 'S74'},
                 {'id': 'S43', 'ASSIGN': 75},
                 {'vtype': 'R(20)', 'id': 'R(20)', 'if': 'R(20)', 'else': 'S77', 'while': 'R(20)', 'for': 'R(20)', 'return': 'R(20)', 'rbrace': 'R(20)', 'ELSE': 76},
                 {'vtype': 'R(17)', 'id': 'R(17)', 'if': 'R(17)', 'while': 'R(17)', 'for': 'R(17)', 'return': 'R(17)', 'rbrace': 'R(17)'},
                 {'rparen': 'S78'},
                 {'vtype': 'R(16)', 'id': 'R(16)', 'if': 'R(16)', 'while': 'R(16)', 'for': 'R(16)', 'return': 'R(16)', 'rbrace': 'R(16)'},
                 {'lbrace': 'S79'},
                 {'lbrace': 'S80'},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 81, 'STMT': 36, 'ASSIGN': 38},
                 {'vtype': 'S42', 'id': 'S43', 'if': 'S39', 'while': 'S40', 'for': 'S41', 'return': 'R(13)', 'rbrace': 'R(13)', 'VDECL': 37, 'BLOCK': 82, 'STMT': 36, 'ASSIGN': 38},
                 {'rbrace': 'S83'},
                 {'rbrace': 'S84'},
                 {'vtype': 'R(19)', 'id': 'R(19)', 'if': 'R(19)', 'while': 'R(19)', 'for': 'R(19)', 'return': 'R(19)', 'rbrace': 'R(19)'},
                 {'vtype': 'R(18)', 'id': 'R(18)', 'if': 'R(18)', 'while': 'R(18)', 'for': 'R(18)', 'return': 'R(18)', 'rbrace': 'R(18)'}]

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
        self.terminal_list.append(self.END_MARK)

    def run(self):
        # Read file
        self.readFile()
        #only includes end mark
        if (len(self.terminal_list)==1):
            return True
        
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

    
