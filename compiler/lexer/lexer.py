# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

from .tag import Tag
from .word import Word
from .word import Words
from .token import Token
from .inputFile import InputFile
from .real import Real
from .integer import Integer
from .characterString import CharacterString
import keyword

class Lexer():
    
    def __init__(self, filename):
        self.file_input = InputFile(filename)
        self.words = {}
        self.peek = ''
        self.line = 0 
        self.column = 0

        self.reserve(Word("program", Tag.PROGRAM))
        self.reserve(Word("constante", Tag.CONSTANT))
        self.reserve(Word("var", Tag.VAR))
        self.reserve(Word("begin", Tag.BEGIN))
        self.reserve(Word("end", Tag.END))
        self.reserve(Word("integer", Tag.INTEGER))
        self.reserve(Word("real", Tag.REAL))
        self.reserve(Word("boolean", Tag.BOOLEAN))
        self.reserve(Word("string", Tag.STRING))
        self.reserve(Word("writeln", Tag.WRITELN))
        self.reserve(Word("readln", Tag.READLN))
        self.reserve(Word("while", Tag.WHILE))
        self.reserve(Word("do", Tag.DO))
        self.reserve(Word("repeat", Tag.REPEAT))
        self.reserve(Word("until", Tag.UNTIL))
        self.reserve(Word("for", Tag.FOR))
        self.reserve(Word("to", Tag.TO))
        self.reserve(Word("downto", Tag.DOWNTO))
        self.reserve(Word("if", Tag.IF))
        self.reserve(Word("then", Tag.THEN))
        self.reserve(Word("else", Tag.ELSE))
        self.reserve(Word("not", Tag.NOT))
        self.reserve(Word("div", Tag.DIV))
        self.reserve(Word("mod", Tag.MOD))
        self.reserve(Word("and", Tag.AND))
        self.reserve(Word("or", Tag.OR))

    def reserve(self, w):
        self.words[w.getLexeme()] = w
    
    def isReserved(self, t: Token):
        return (str(t).lower() in self.words.keys())

    def readch(self):
        try:
            self.peek, self.line, self.column = self.file_input.getChar()
        except IOError as e:
            print(e)
    
    def readchs(self, c):
        try:
            self.readch()
            if self.peek != c:
                return False
            return True
        except IOError as e:
            print(e)
    
    def skipWhiteSpaces(self):
        try:
            self.peek = self.file_input.peekChar()
            while self.peek.isspace():
                self.peek, self.line, self.column = self.file_input.getChar()
        except IOError as e:
            print(e)

    def readCharacterString(self):
        cs = str(self.peek)
        self.peek, self.line, self.column = self.file_input.getChar()
        while self.peek != '"' and self.peek != "'":
            cs += self.peek
            self.peek, self.line, self.column = self.file_input.getChar()
        cs += self.peek
        self.readch()
        return CharacterString(cs)

    def readComments(self):
        prev = self.file_input.position
        current = self.file_input.position + 1
        while current < self.file_input.size and self.file_input.data[prev] != '*' and self.file_input.data[current] != ')':
            prev = current
            current += 1
        if current >= self.file_input.size:
            raise EOFError
        self.file_input.position = current + 1
        self.file_input.line_number = self.line + 1
        return Token(Tag.COMMENTS)

    def scan(self):
        self.skipWhiteSpaces()
        
        if self.peek == '(':
            if self.readchs('*'):
                self.readch()
                return self.readComments(), self.line, self.column
            else:
                return Token('('), self.line, self.column

        if self.peek == '<':
            if self.readchs('='):
                return Words.le, self.line, self.column
            elif self.readchs('>'):
                return Words.ne, self.line, self.column
            else:
                return Token('<'), self.line, self.column

        if self.peek == '>':
            if self.readchs('='):
                return Words.ge, self.line, self.column
            else:
                return Token('>'), self.line, self.column

        if self.peek == '=':
            if self.readchs('='):
                return Words.eq, self.line, self.column
            else:
                return Token('='), self.line, self.column

        if self.peek == ':':
            if self.readchs('='):
                self.readch()
                return Words.assing, self.line, self.column
            else:
                return Token(':'), self.line, self.column

        if self.peek == '"' or self.peek == "'":
            return self.readCharacterString(), self.line, self.column


        if self.peek.isdigit():
            v = 0
            while True:
                v = (10 * v) + int(self.peek)
                self.readch()
                if not self.peek.isdigit():
                    break
            if self.peek != '.':
                return Integer(v), self.line, self.column
            x = float(v)
            d = float(10)
            while True:
                self.readch()
                if not self.peek.isdigit():
                    break
                x += int(self.peek) / d
                d *= 10
            return Real(x), self.line, self.column


        if self.peek.isalpha():
            b = ""
            while True:
                b += str(self.peek.lower())
                self.readch()
                if not self.peek.isalnum() or self.peek == '_':
                    break
            s = str(b)
            w = self.words.get(s)
            if w:
                return w, self.line, self.column
            w = Word(s, Tag.ID)
            self.words[s] = w
            return w, self.line, self.column
            
        tok = Token(self.peek)
        self.readch()
        return tok, self.line, self.column