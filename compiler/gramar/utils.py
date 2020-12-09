class Utils():
    def parse(self, token):
        if token.tag == 290:
            return 'identifier'
        if token.tag == 291 or token.tag == "'":
            return 'string'
        if token.tag == 261:
            return 'integer'
        if token.tag == 262:
            return 'real'
        if token.tag == 263:
            'boolean'
        if token.tag == 292:
            return "comment"
        else:
            return token

    def search_on_table(self,state, input, dict):
        return dict[state].get(str(input))

    def reduce(self, gramar, prod):
        prodToReduce = gramar[prod].split("->")[1].strip()
        elements = len(gramar[prod].split("->")[1].split())*2
        state = str(gramar[prod].split("->")[0]).strip()
        if prodToReduce == "''":
            elements = 0
        return elements, state
