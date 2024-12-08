class ioword:
    #constructor
    def __init__(self):
        self.word = " "
    #method -1
    def getword(self):
        self.word=input("Enter word:")
    #method -2
    def display(self):
        print("Uppercase val is:",self.word.upper())
word = ioword()
word.getword()
word.display()