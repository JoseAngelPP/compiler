# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

from .token import Token
from .tag import Tag

class Word(Token):

    def __init__(self, lexeme, tag):
        super().__init__(tag)
        self.lexeme = lexeme

    def getLexeme(self):
        return self.lexeme
    
    def __str__(self):
        return f'{str(self.lexeme)}'
    

class Words():
    eq = Word('==', Tag.EQ)
    ne = Word( "<>", Tag.NEQ )
    le  = Word( "<=", Tag.LE  )
    ge =  Word( ">=", Tag.GE )
    minus  = Word( "minus", Tag.MINUS )
    assing = Word( ":=", Tag.ASSIGN )
    true   = Word( "true",  Tag.TRUE)
    false  = Word( "false", Tag.FALSE)

    