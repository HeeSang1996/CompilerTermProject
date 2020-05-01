import sys

class LexicalAnalyzer(object):


    def __init__(self):
        pass



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Input error")
    
    
    la = LexicalAnalyzer()
    print(sys.argv)
    print(len(sys.argv))
    print("Test func")