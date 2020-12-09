# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

import sys
from lexer.lexer import Lexer
from gramar.syntacticAnalyzer import SynyacticAnalyzer


def main():
    try:
        if len(sys.argv) != 2:
            print(f'Usage: python main.py filename' )                
            
        lex = Lexer(sys.argv[1])
        analyzer = SynyacticAnalyzer()
        analyzer.analyze(lex)

    except Exception as e:
        print(e)

if __name__== "__main__" :
    main()