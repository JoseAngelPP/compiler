# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

import os

class InputFile():

    def __init__(self, filename):
        f = None
        self.position = 0
        self.line_number = 0
        self.column_number = 0
        self.data = []

        f = open(filename, 'r')
        if not f or not os.path.isfile(filename):
            raise Exception
        if os.path.getsize(filename) == 0:
            raise Exception
        
        self.data =f.read() + " $ "
        self.size = len(self.data)

    def is_eof(self):
        return self.position >= self.size
    
    def is_eol(self):
        return self.is_eof or self.peekChar() == '\n'
    
    def getChar(self):
        try:
            self.position += 1
            if self.is_eof():
                raise EOFError

            c = str(self.data[self.position])
            if c == '\n':
                self.column_number = 1
                self.line_number += 1
            else:
                self.column_number += 1
            return c, self.line_number, self.column_number
        except EOFError as e:
            print(e)
    
    def peekChar(self):
        if self.is_eof():
            raise EOFError
        return str(self.data[self.position])