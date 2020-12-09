# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

class Token():
    def __init__(self, tag):
        super().__init__()
        self.tag = tag

    def getTag(self):
        return self.tag
    
    def __str__(self):
        return f'{str(self.tag)}'