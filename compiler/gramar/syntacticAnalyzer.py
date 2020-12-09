import sys
from lexer.lexer import Lexer
from lexer.tag import Tag
from gramar.myGrammar import MyGrammar
from gramar.utils import Utils

class SynyacticAnalyzer():
    def analyze(self, lex):
        currentState = 0
        stack = [0]
        token, line, column = lex.scan()
        analyzer = SynyacticAnalyzer()
        gramar = MyGrammar()
        utils = Utils()
        try:
            while True:
                input = utils.parse(token)
                if input == 'comment':
                    token, line, column = lex.scan()
                    continue
                currentState = stack[-1]
                if str(input) not in gramar.TABLE[currentState].keys():
                    print(f'main.pas({line}:{column}) Fatal: Syntax error, near to "{str(token) if str(token) != "$" else "end of file"}"')
                    print('Fatal: Compilation aborted')
                    break
                move = utils.search_on_table(currentState, input, gramar.TABLE)
                if str(input) == '$':
                    print('Compilado')
                    break
                if type(move) == int or move[0] == 's':
                    # shift
                    stack.append(str(input))
                    stack.append(int(move.split('s')[1]))
                    token, line, column = lex.scan()
                if move[0] == 'r':
                    # reduce
                    elements_to_pop, newElemnt = utils.reduce(gramar.GRAMAR, int(move.split('r')[1]))
                    for element in range(elements_to_pop):
                        stack.pop()
                    currentState = stack[-1]
                    stack.append(newElemnt)
                    stack.append(int(gramar.TABLE[currentState][newElemnt]))
        except EOFError as e:
                print(e)