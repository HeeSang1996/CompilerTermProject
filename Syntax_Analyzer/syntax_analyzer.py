import sys
import os

class SyntaxAnalyzer(object):

    # input text file
    input_stream = None

    def __init__(self, file):
        # Get text file
        self.input_stream = file

    def run(self):

        
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
    if sa:
        print("Accepted")
    else:
        print("Reject")

    