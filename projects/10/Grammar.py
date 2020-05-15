# coding=utf-8
"""
----------------------Program structure: ----------------------
class:          'class' className '{' classVarDec* subroutineDec* '}'
classVarDec:    ('static'|'field') type varName (',' varName)* ';'
type:           'int'|'char'|'boolean' | className
subroutineDec: ('constructor'|'function'|'method')
                ('void' | type) subroutineName '(' parameterList ')'
                subroutineBody
parameterList: ((type varName) (',' type varName)*)?
subroutineBody: '{' varDec* statements '}'
varDec:         'var' type varName (',' varName)* ';'
className: identifier
subroutineName: identifier
varName: identifier

----------------------Statements:------------------------------
statements: statement*
statement:    letStatement | ifStatement | whileStatement |
               doStatement | returnStatement
letStatement: 'let' varName ('[' expression ']')? '=' expression ';'
ifStatement:    'if' '(' expression ')' '{' statements '}'
                ('else' '{' statements '}')?
whileStatement: 'while' '(' expression ')' '{' statements '}'
doStatement: '   do' subroutineCall ';'
ReturnStatement 'return' expression? ';'

----------------------Expressions:------------------------------
expression: term (op term)*
term:           integerConstant | stringConstant | keywordConstant |
                varName | varName '[' expression ']' | subroutineCall |
                '(' expression ')' | unaryOp term
subroutineCall: subroutineName '(' expressionList ')' | (className |
                varName) '.' subroutineName '(' expressionList ')'
expressionList: (expression (',' expression)* )?
op:             '+'|'-'|'*'|'/'|'&'|'|'|'<'|'>'|'='
unaryOp:         '-'|'~'
KeywordConstant: 'true'|'false'|'null'|'this'


-----------------------Grammar------------------------------------
‘xxx’: quoted boldface is used for tokens that appear verbatim (‘‘terminals’’);
xxx: regular typeface is used for names of language constructs (‘‘non-terminals’’);
( ): parentheses are used for grouping of language constructs;
x|y: indicates that either x or y can appear;
x?: indicates that x appears 0 or 1 times;
x*: indicates that x appears 0 or more times.


"""