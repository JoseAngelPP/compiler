# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

from .token import Token 
from .tag import Tag 

class Integer(Token):

    def __init__(self, value):
        super().__init__(Tag.INTEGER)
        self.value = value

    def __str__(self):
        return f'{str(self.value)}'

    def get_value(self):
        return self.value