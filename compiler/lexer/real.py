# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

from .tag import Tag
from .token import Token

class Real(Token):

    def __init__(self, value):                  
        super().__init__(Tag.REAL)
        self.value = value

    def __str__(self):
        return f'{str(self.value)}'

    def get_value(self):
        return self.value