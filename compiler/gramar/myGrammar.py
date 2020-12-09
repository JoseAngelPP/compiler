# Autor: José Angel Peña A010208033
# Diseño de compiladores - Lexer 

class MyGrammar():
    def __init__(self):

        self.TABLE = [
                    # State 0
                    {"program": "s3", "START": 1, "PROGRAM-HEADING": 2},
                    # State 1
                    {"$": "acc"},
                    # State 2 
                    {";": "s4", },
                    # State 3
                    {"identifier": "s5"},
                    # State 4
                    {".": "r8", "constant": "s8", "var": "r8", "begin": "r8", "PROGRAM-BLOCK": 6, "CONSTANT-DECLARATION-PART": 7},
                    # State 5
                    {";": "r4", "(": "s10", "OPT-PROGRAM-PARAMETERS": 9},
                    # State 6 
                    {".": "s11"},
                    # State 7
                    {"var": "s13", "begin": "r13", "VARIABLE-DECLARATION-PART": 12},
                    # State 8
                    {"identifier": "s15", "CONSTANT-DEFINITION": 14},
                    # State 9
                    {";": "r2"},
                    # State 10
                    {"identifier": "s18","PROGRAM-PARAMETERS": 16, "IDENTIFIER-LIST": 17},
                    # State 11
                    {"$": "r1"},
                    # State 12
                    {"begin": "s20", "STATEMENT-PART": 19},
                    # State 13
                    {"identifier": "s18", "VARIABLE-DECLARATION": 21, "IDENTIFIER-LIST": 22},
                    # State 14
                    {";": "s23"},
                    # State 15
                    {"=": "s24"},
                    # State 16
                    {"=": "s25"},
                    # State 17
                    {")": "r5"},
                    # State 18
                    {")": "r24", ":": "r24", ",": "s27", "MORE-IDENTIFIER": 26},
                    # State 19
                    {".": "r6", },
                    # State 20
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44","STATEMENT-SEQUENCE": 28,"STATEMENT": 29,
                    "SIMPLE-STATEMENT": 30,"ASSIGNMENT-STATEMENT": 32,"IO-STATEMENT": 33,"WRITELN-STATEMENT": 38,"READLN-STATEMENT": 39,"STRUCTURED-STATEMENT": 31,"COMPOUND-STATEMENT": 34,"REPETITIVE-STATEMENT": 35,"WHILE-STATEMENT": 41,"REPEAT-STATEMENT": 42,"FOR-STATEMENT": 43,"CONDITIONAL-STATEMENT": 36},
                    # State 21
                    {";": "s50"},
                    # State 22
                    {":": "s51"},
                    # State 23
                    {".": "r11", "identifier": "s15", "var": "r11", "begin": "r11", "CONSTANT-DEFINITION": 53, "MORE-CONSTANT-DEFINITION": 52},
                    # State 24
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 54, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 25
                    {";": "r3"},
                    # State 26
                    {")": "r22", ":": "r22"},
                    # State 27
                    {"identifier": "s59"},
                    # State 28
                    {"end": "s60"},
                    # State 29
                    {";": "s61"},
                    # State 30
                    {";": "r28", "else": "r28"},
                    # State 31
                    {";": "r29", "else": "r29"},
                    # State 32
                    {";": "r30", "else": "r30"},
                    # State 33
                    {";": "r31", "else": "r31"},
                    # State 34
                    {";": "r47", "else": "r47"},
                    # State 35
                    {";": "r48", "else": "r48"},
                    # State 36
                    {";": "r49", "else": "r49"},
                    # State 37
                    {":=": "s62"},
                    # State 38
                    {";": "r33", "else": "r33"},
                    # State 39
                    {";": "r34", "else": "r34"},
                    # State 40
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44",    "STATEMENT-SEQUENCE": 63,    "STATEMENT": 29,    "SIMPLE-STATEMENT": 30,    "ASSIGNMENT-STATEMENT": 32,    "IO-STATEMENT": 33,    "WRITELN-STATEMENT": 38,    "READLN-STATEMENT": 39,    "STRUCTURED-STATEMENT": 31,    "COMPOUND-STATEMENT": 34,    "REPETITIVE-STATEMENT": 35,    "WHILE-STATEMENT": 41,    "REPEAT-STATEMENT": 42,    "FOR-STATEMENT": 43,    "CONDITIONAL-STATEMENT": 36},
                    # State 41
                    {";": "r51"},
                    # State 42
                    {";": "r52"},
                    # State 43
                    {";": "r53", "else": "r53"},
                    # State 44
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 64,"SIMPLE-EXPRESSION": 55,"OPT-SIGN": 56},
                    # State 45
                    {"(": "s65"},
                    # State 46
                    {";": "r46", "(": "s67", "else": "r46","OPT-IDENTIFIER-LIST": 66},
                    # State 47
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 68, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 48
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44",    "STATEMENT-SEQUENCE": 69,    "STATEMENT": 29,    "SIMPLE-STATEMENT": 30,    "ASSIGNMENT-STATEMENT": 32,    "WRITELN-STATEMENT": 38,    "READLN-STATEMENT": 39,    "STRUCTURED-STATEMENT": 31,    "COMPOUND-STATEMENT": 34,    "REPETITIVE-STATEMENT": 35,    "WHILE-STATEMENT": 41,    "REPEAT-STATEMENT": 42,    "FOR-STATEMENT": 43,     "CONDITIONAL-STATEMENT": 36},
                    # State 49
                    {"identifier": "s70"},
                    # State 50
                    {"identifier": "s18", "begin": "r15","MORE-VARIABLE-DECLARATION": 71, "VARIABLE-DECLARATION": 72, "IDENTIFIER-LIST": 22},
                    # State 51
                    {"integer": "s74", "real": "s75", "boolean": "s76", "string": "s77","TYPE": 73},
                    # State 52
                    {".": "r7", "var": "r7", "begin": "r7"},
                    # State 53
                    {";": "s78",},
                    # State 54
                    {";": "r9"},
                    # State 55
                    {";": "r64",")": "r64","=": "s81", "do": "r64", "to": "r64", "downto": "r64", "then": "r64", "else": "r64", "<>": "s82", "<": "s83", "<=": "s84", ">": "s85",     ">=": "s86","OPT-REL-EXPRESSION": 79, "RELATIONAL-OPERATOR": 80},
                    # State 56
                    {"identifier": "s89", "(": "s92", "string": "s91", "number": "s90", "not": "s93","TERM": 87, "FACTOR": 88},
                    # State 57
                    {"identifier": "r66", ")": "r66", "string": "r66", "number": "r66", "not": "r66"},
                    # State 58
                    {"identifier": "r67", "(": "r67", ")": "r67", "string": "r67", "number": "r67", "not": "r67"},
                    # State 59
                    {")": "r24", ":": "r24", ",": "s27", 'MORE-IDENTIFIER': 94},
                    # State 60
                    {".": "r17"},
                    # State 61
                    {"identifier": "s37", "begin": "s40", "end": "r27", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "until": "r27", "for": "s49", "if": "s44","MORE-STATEMENT": 95, "STATEMENT": 96, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 62
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 97, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 63
                    {"end": "s98"},
                    # State 64
                    {"then": "s99" },
                    # State 65
                    {"identifier": "s105", ')':'r37', "string": "s104", "number": "s103","OPT-ELEMENT-LIST": 100, "ELEMENT-LIST": 101, "ELEMENT": 102},
                    # State 66
                    {";": "r44", "else": "r44"},
                    # State 67
                    {"identifier": "s18","IDENTIFIER-LIST": 106},
                    # State 68
                    {"do": "s107"},
                    # State 69
                    {"until": "s108"},
                    # State 70
                    {":=": "s109"},
                    # State 71
                    {"begin": "r12", },
                    # State 72
                    {";": "s110"},
                    # State 73
                    {";": "r16", },
                    # State 74
                    {";": "r18"},
                    # State 75
                    {";": "r19"},
                    # State 76
                    {";": "r20"},
                    # State 77
                    {";": "r21"},
                    # State 78
                    {".": "r11", "identifier": "s15", "var": "r11", "begin": "r11","CONSTANT-DEFINITION": 53, "MORE-CONSTANT-DEFINITION": 111},
                    # State 79
                    {";": "r62", ")": "r62", "to": "r62", "downto": "r62", "then": "r62", "else": "r62"},
                    # State 80
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","SIMPLE-EXPRESSION": 112, "OPT-SIGN": 56},
                    # State 81
                    {";": "r79", "identifier": "r79", "(": "r79", ")": "r79", "string": "r79", "number": "r79", "+": "r79", "-": "r79", "not": "r79"},
                    # State 82
                    {";": "r80", "identifier": "r80", "(": "r80", ")": "r80", "string": "r80", "number": "r80", "do": "r80", "to": "r80", "downto": "r80", "then": "r80", "else": "r80", "+": "r80", "-": "r80", "not": "r80"},
                    # State 83
                    {";": "r81", "identifier": "r81", "(": "r81", ")": "r81", "string": "r81", "number": "r81", "do": "r81", "to": "r81", "downto": "r81", "then": "r81", "else": "r81", "+": "r81", "-": "r81", "not": "r81"},
                    # State 84
                    {";": "r82", "identifier": "r82", "(": "r82", ")": "r82", "string": "r82", "number": "r82", "do": "r82", "to": "r82", "downto": "r82", "then": "r82", "else": "r82", "+": "r82", "-": "r82", "not": "r82"},
                    # State 85
                    {";": "r83", "identifier": "r83", "(": "r83", ")": "r83", "string": "r83", "number": "r83", "do": "r83", "to": "r83", "downto": "r83", "then": "r83", "else": "r83", "+": "r83", "-": "r83", "not": "r83"},
                    # State 86
                    {";": "r84", "identifier": "r84", "(": "r84", ")": "r84", "string": "r84", "number": "r84", "do": "r84", "to": "r84", "downto": "r84", "then": "r84", "else": "r84", "+": "r84", "-": "r84", "not": "r84"},
                    # State 87
                    {";": "r70", ")": "r70", "=": "r70", "do": "r70", "to": "r70", "downto": "r70", "then": "r70", "else": "r70", "+": "s115", "-": "s116", "<>": "r70", "<": "r70", "<=": "r70", ">": "r70", ">=":"r70", "or": "s117","MORE-ADD-TERM": 113, "ADDITION-OPERATOR": 114},
                    # State 88
                    {";": "r73", ")": "r73", "=": "r73", "do": "r73", "to": "r73", "downto": "r73", "then": "r73", "else": "r73", "+": "r73", "-": "r73", "<>": "r73", "<": "r73", "<=": "r73", ">": "r73", ">=": "r73", "or": "r73", "*": "s120", "/": "s121", "div": "s122", "mod": "s123", "and": "s124","MORE-MULT-TERM": 118, "MULTIPLICATION-OPERATOR": 119},
                    # State 89
                    {";": "r74", ")": "r74", "=": "r74", "do": "r74", "to": "r74", "downto": "r74", "then": "r74", "else": "r74", "+": "r74", "-": "r74", "<>": "r74", "<": "r74", "<=": "r74", ">": "r74", ">=": "r74", "or": "r74", "*": "r74", "/": "r74", "div": "r74", "mod": "r74", "and": "r74"},
                    # State 90
                    {";": "r75", ")": "r75", "=": "r75", "do": "r75", "to": "r75", "downto": "r75", "then": "r75", "else": "r75", "+": "r75", "-": "r75", "<>": "r75", "<": "r75", "<=": "r75", ">": "r75", ">=": "r75", "or": "r75", "*": "r75", "/": "r75", "div": "r75", "mod": "r75", "and": "r75"},
                    # State 91
                    {";": "r76", ")": "r76", "=": "r76", "do": "r76", "to": "r76", "downto": "r76", "then": "r76", "else": "r76", "+": "r76", "-": "r76", "<>": "r76", "<": "r76", "<=": "r76", ">": "r76", ">=": "r76", "or": "r76", "*": "r76", "/": "r76", "div": "r76", "mod": "r76", "and": "r76"},
                    # State 92
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 125, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 93
                    {"identifier": "s89", "(": "s92", "string": "s91", "number": "s90", "not": "s93","FACTOR": 126},
                    # State 94
                    {")": "r23", ":": "r23"},
                    # State 95
                    {"end": "r25", "until": "r25", },
                    # State 96
                    {";": "s127"},
                    # State 97
                    {";": "r32", "else": "r32"},
                    # State 98
                    {";": "r50", "else": "r50"},
                    # State 99
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44","STATEMENT": 128, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 100
                    {")": "s129"},
                    # State 101
                    {")": "r36"},
                    # State 102
                    {")": "r40", ",": "s131","MORE-ELEMENT": 130},
                    # State 103
                    {")": "r41", ",": "r41"},
                    # State 104
                    {")": "r42", ",": "r42"},
                    # State 105
                    {")": "r43", ",": "r43"},
                    # State 106
                    {")": "s132"},
                    # State 107
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44","STATEMENT": 133, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 108
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 134, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 109
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68","EXPRESSION": 135, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 110
                    {"identifier": "s18", "begin": "r15","MORE-VARIABLE-DECLARATION": 136, "VARIABLE-DECLARATION": 72, "IDENTIFIER-LIST": 22, },
                    # State 111
                    {".": "r10", "var": "r10", "begin": "r10"},
                    # State 112
                    {";": "r63", ")": "r63", "do": "r63", "to": "r63", "downto": "r63", "then": "r63", "else": "r63"},
                    # State 113
                    {";": "r65", ")": "r65", "=": "r65", "do": "r65", "to": "r65", "downto": "r65", "then": "r65", "else": "r65", "<>": "r65", "<": "r65", "<=": "r65", ">": "r65", ">=": "r65"},
                    # State 114
                    {"identifier": "s89", "(": "s92", "string": "s91", "number": "s90", "not": "s93","TERM": 137, "FACTOR": 88},
                    # State 115
                    {"identifier": "r85", "(": "r85", "string": "r85", "number": "r85", "not": "r85"},
                    # State 116
                    {"identifier": "r86", "(": "r86", "string": "r86", "number": "r86", "not": "r86"},
                    # State 117
                    {"identifier": "r87", "(": "r87", "string": "r87", "number": "r87", "not": "r87"},
                    # State 118
                    {";": "r71", ")": "r71", "=": "r71", "do": "r71", "to": "r71", "downto": "r71", "then": "r71", "else": "r71", "+": "r71", "-": "r71", "<>": "r71", "<": "r71", "<=": "r71", ">": "r71", ">=": "r71", "or": "r71"},
                    # State 119
                    {"identifier": "s89", "(": "s92", "string": "s91", "number": "s90", "not": "s93","FACTOR": 138},
                    # State 120
                    {"identifier": "r88", "(": "r88", "string": "r88", "number": "r88", "not": "r88"},
                    # State 121
                    {"identifier": "r89", "(": "r89", "string": "r89", "number": "r89", "not": "r89"},
                    # State 122
                    {"identifier": "r90", "(": "r90", "string": "r90", "number": "r90", "not": "r90"},
                    # State 123
                    {"identifier": "r91", "(": "r91", "string": "r91", "number": "r91", "not": "r91"},
                    # State 124
                    {"identifier": "r92", "(": "r92", "string": "r92", "number": "r92", "not": "r92"},
                    # State 125
                    {")": "s139", },
                    # State 126
                    {";": "r78", ")": "r78", "=": "r78", "do": "r78", "to": "r78", "downto": "r78", "then": "r78", "else": "r78", "+": "r78", "-": "r78", "<>": "r78", "<": "r78", "<=": "r78", ">": "r78", ">=": "r78", "or": "r78", "*": "r78", "/": "r78", "div": "r78", "mod": "r78", "and": "r78"},
                    # State 127
                    {"identifier": "s37", "begin": "s40", "end": "r27", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "until": "r27", "for": "s49", "if": "s44","MORE-STATEMENT": 140, "STATEMENT": 96, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 128
                    {";": "r61", "else": "s142","OPT-ELSE": 141},
                    # State 129
                    {";": "r35", "else": "r35"},
                    # State 130
                    {")": "r38"},
                    # State 131
                    {"identifier": "s105", "string": "s104", "number": "s103","ELEMENT": 143},
                    # State 132
                    {";": "r45", "else": "r45", "number": "s103"},
                    # State 133
                    {";": "r54", "else": "r54"},
                    # State 134
                    {";": "r55", "else": "r55", "number": "s103"},
                    # State 135
                    {"to": "s145", "downto": "s146", "TO-DOWNTO": 144},
                    # State 136
                    {"begin": "r14"},
                    # State 137
                    {";": "r70", ")": "r70", "=": "r70", "do": "r70", "to": "r70", "downto": "r70", "then": "r70", "else": "r70", "+": "s115", "-": "s116", "<>": "r70", "<": "r70", "<=": "r70", ">": "r70", ">=": "r70", "or": "s117", "MORE-ADD-TERM": 147, "ADDITION-OPERATOR": 114},
                    # State 138
                    {";": "r73", ")": "r73", "=": "r73", "do": "r73", "to": "r73", "downto": "r73", "then": "r73", "else": "r73", "+": "r73", "-": "r73", "<>": "r73", "<": "r73", "<=": "r73", ">": "r73", ">=": "r73", "or": "r73", "*": "s120", "/": "s121", "div": "s122", "mod": "s123", "and": "s124", "MORE-MULT-TERM": 148, "MULTIPLICATION-OPERATOR": 119},
                    # State 139
                    {";": "r77", ")": "r77", "=": "r77", "do": "r77", "to": "r77", "downto": "r77", "then": "r77", "else": "r77", "+": "r77", "-": "r77", "<>": "r77", "<": "r77", "<=": "r77", ">": "r77", ">=": "r77", "or": "r77", "*": "r77", "/": "r77", "mod": "r77", "and": "r77"},
                    # State 140
                    {"end": "r26", "until": "r26", "number": "s103"},
                    # State 141
                    {";": "r59", "else": "r59"},
                    # State 142
                    {"identifier": "s37", "begin": "s40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "for": "s49", "if": "s44", "STATEMENT": 149, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 143
                    {")": "r40", ",": "s131", "MORE-ELEMENT": 150},
                    # State 144
                    {"identifier": "r68", "(": "r68", "string": "r68", "number": "r68", "+": "s57", "-": "s58", "not": "r68", "EXPRESSION": 151, "SIMPLE-EXPRESSION": 55, "OPT-SIGN": 56},
                    # State 145
                    {";": "r57", "identifier": "r57", "(": "r57", "=": "r57", "string": "r57", "number": "r57", "do": "r57", "else": "r57", "+": "r57", "-": "r57", "not": "r57", "<>": "r57", "<": "r57", "<=": "r57", ">": "r57", ">=": "r57"},
                    # State 146
                    {";": "r58", "identifier": "r58", "(": "r58", "=": "r58", "string": "r58", "number": "r58", "do": "r58", "else": "r58", "+": "r58", "-": "r58", "not": "r58", "<>": "r58", "<": "r58", "<=": "r58", ">": "r58", ">=": "r58"},
                    # State 147
                    {";": "r69", ")": "r69", "=": "r69", "do": "r69", "to": "r69", "downto": "r69", "then": "r69", "else": "r69", "<>": "r69", "<": "r69", "<=": "r69", ">": "r69", ">=": "r69"},
                    # State 148
                    {";": "r72", ")": "r72", "=": "r72", "do": "r72", "to": "r72", "downto": "r72", "then": "r72", "else": "r72", "<>": "r72", "<": "r72", "<=": "r72", ">": "r72", ">=": "r72", "or": "r72"},
                    # State 149
                    {";": "r60", "else": "r60"},
                    # State 150
                    {")": "r39"},
                    # State 151
                    {"do": "s152"},
                    # State 152
                    {"identifier": "s37", "begin": "40", "writeln": "s45", "readln": "s46", "while": "s47", "repeat": "s48", "if": "s44", "STATEMENT": 153, "SIMPLE-STATEMENT": 30, "ASSIGNMENT-STATEMENT": 32, "IO-STATEMENT": 33, "WRITELN-STATEMENT": 38, "READLN-STATEMENT": 39, "STRUCTURED-STATEMENT": 31, "COMPOUND-STATEMENT": 34, "REPETITIVE-STATEMENT": 35, "WHILE-STATEMENT": 41, "REPEAT-STATEMENT": 42, "FOR-STATEMENT": 43, "CONDITIONAL-STATEMENT": 36},
                    # State 153
                    {";": "r56", "else": "r56"}
                    ]

        self.GRAMAR = [
            "START' -> START",
            "START -> PROGRAM-HEADING ; PROGRAM-BLOCK .",
            "PROGRAM-HEADING -> program identifier OPT-PROGRAM-PARAMETERS",
            "OPT-PROGRAM-PARAMETERS -> ( PROGRAM-PARAMETERS )",
            "OPT-PROGRAM-PARAMETERS -> ''",
            "PROGRAM-PARAMETERS -> IDENTIFIER-LIST",
            "PROGRAM-BLOCK -> CONSTANT-DECLARATION-PART VARIABLE-DECLARATION-PART STATEMENT-PART",
            "CONSTANT-DECLARATION-PART -> constant CONSTANT-DEFINITION ; MORE-CONSTANT-DEFINITION",
            "CONSTANT-DECLARATION-PART -> ''",
            "CONSTANT-DEFINITION -> identifier = EXPRESSION",
            "MORE-CONSTANT-DEFINITION -> CONSTANT-DEFINITION ; MORE-CONSTANT-DEFINITION",
            "MORE-CONSTANT-DEFINITION -> ''",
            "VARIABLE-DECLARATION-PART -> var VARIABLE-DECLARATION ; MORE-VARIABLE-DECLARATION",
            "VARIABLE-DECLARATION-PART -> ''",
            "MORE-VARIABLE-DECLARATION -> VARIABLE-DECLARATION ; MORE-VARIABLE-DECLARATION",
            "MORE-VARIABLE-DECLARATION -> ''",
            "VARIABLE-DECLARATION -> IDENTIFIER-LIST : TYPE",
            "STATEMENT-PART -> begin STATEMENT-SEQUENCE end ",
            "TYPE -> integer",
            "TYPE -> real",
            "TYPE -> boolean",
            "TYPE -> string",
            "IDENTIFIER-LIST -> identifier MORE-IDENTIFIER",
            "MORE-IDENTIFIER -> , identifier MORE-IDENTIFIER",
            "MORE-IDENTIFIER -> ''",
            "STATEMENT-SEQUENCE -> STATEMENT ; MORE-STATEMENT",
            "MORE-STATEMENT -> STATEMENT ; MORE-STATEMENT",
            "MORE-STATEMENT -> ''",
            "STATEMENT -> SIMPLE-STATEMENT",
            "STATEMENT -> STRUCTURED-STATEMENT",
            "SIMPLE-STATEMENT -> ASSIGNMENT-STATEMENT",
            "SIMPLE-STATEMENT -> IO-STATEMENT",
            "ASSIGNMENT-STATEMENT -> identifier := EXPRESSION",
            "IO-STATEMENT -> WRITELN-STATEMENT",
            "IO-STATEMENT -> READLN-STATEMENT",
            "WRITELN-STATEMENT -> writeln ( OPT-ELEMENT-LIST )",
            "OPT-ELEMENT-LIST -> ELEMENT-LIST",
            "OPT-ELEMENT-LIST -> ''",
            "ELEMENT-LIST -> ELEMENT MORE-ELEMENT",
            "MORE-ELEMENT -> , ELEMENT MORE-ELEMENT",
            "MORE-ELEMENT -> ''",
            "ELEMENT -> number",
            "ELEMENT -> string",
            "ELEMENT -> identifier",
            "READLN-STATEMENT -> readln OPT-IDENTIFIER-LIST",
            "OPT-IDENTIFIER-LIST -> ( IDENTIFIER-LIST )",
            "OPT-IDENTIFIER-LIST -> ''",
            "STRUCTURED-STATEMENT -> COMPOUND-STATEMENT",
            "STRUCTURED-STATEMENT -> REPETITIVE-STATEMENT",
            "STRUCTURED-STATEMENT -> CONDITIONAL-STATEMENT",
            "COMPOUND-STATEMENT -> begin STATEMENT-SEQUENCE end",
            "REPETITIVE-STATEMENT -> WHILE-STATEMENT",
            "REPETITIVE-STATEMENT -> REPEAT-STATEMENT",
            "REPETITIVE-STATEMENT -> FOR-STATEMENT",
            "WHILE-STATEMENT -> while EXPRESSION do STATEMENT",
            "REPEAT-STATEMENT -> repeat STATEMENT-SEQUENCE until EXPRESSION",
            "FOR-STATEMENT -> for identifier := EXPRESSION TO-DOWNTO EXPRESSION do STATEMENT",
            "TO-DOWNTO -> to",
            "TO-DOWNTO -> downto",
            "CONDITIONAL-STATEMENT -> if EXPRESSION then STATEMENT OPT-ELSE",
            "OPT-ELSE -> else STATEMENT",
            "OPT-ELSE -> ''",
            "EXPRESSION -> SIMPLE-EXPRESSION OPT-REL-EXPRESSION",
            "OPT-REL-EXPRESSION -> RELATIONAL-OPERATOR SIMPLE-EXPRESSION",
            "OPT-REL-EXPRESSION -> ''",
            "SIMPLE-EXPRESSION -> OPT-SIGN TERM MORE-ADD-TERM",
            "OPT-SIGN -> +",
            "OPT-SIGN -> -",
            "OPT-SIGN -> ''",
            "MORE-ADD-TERM -> ADDITION-OPERATOR TERM MORE-ADD-TERM",
            "MORE-ADD-TERM -> ''",
            "TERM -> FACTOR MORE-MULT-TERM",
            "MORE-MULT-TERM -> MULTIPLICATION-OPERATOR FACTOR MORE-MULT-TERM",
            "MORE-MULT-TERM -> ''",
            "FACTOR -> identifier",
            "FACTOR -> number",
            "FACTOR -> string",
            "FACTOR -> ( EXPRESSION )",
            "FACTOR -> not FACTOR",
            "RELATIONAL-OPERATOR -> =",
            "RELATIONAL-OPERATOR -> <>",
            "RELATIONAL-OPERATOR -> <",
            "RELATIONAL-OPERATOR -> <=",
            "RELATIONAL-OPERATOR -> >",
            "RELATIONAL-OPERATOR -> >=",
            "ADDITION-OPERATOR -> +",
            "ADDITION-OPERATOR -> -",
            "ADDITION-OPERATOR -> or",
            "MULTIPLICATION-OPERATOR -> *",
            "MULTIPLICATION-OPERATOR -> /",
            "MULTIPLICATION-OPERATOR -> div",
            "MULTIPLICATION-OPERATOR -> mod",
            "MULTIPLICATION-OPERATOR -> and",
        ]