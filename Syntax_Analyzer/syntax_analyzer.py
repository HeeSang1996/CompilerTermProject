import sys
import os

class SyntaxAnalyzer(object):

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

            # Print for debugging
            print(terminal)

    def run(self):
        # Read file
        self.readFile()


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

    