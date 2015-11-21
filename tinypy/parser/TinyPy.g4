grammar TinyPy;

options
{
    language=Python3;
}

tokens { INDENT, DEDENT }

// See @CustomLexer.py
@lexer::members { }

// https://docs.python.org/2/reference/grammar.html
// https://docs.python.org/3/reference/grammar.html
// https://docs.python.org/devguide/grammar.html

//******************************************************//
// Parser Rules                                         //
//******************************************************//

/**
 *
 * Different input types
 *
 # Start symbols for the grammar:
 #       single_input is a single interactive statement;
 #       file_input is a module or sequence of commands read from an input file;
 #       eval_input is the input for the eval() functions.
 */
file_input
    : ( NEWLINE | stmt )* EOF
    ;

single_input
    : NEWLINE
    | simple_stmt
    | compound_stmt NEWLINE
    ;

eval_input
    : test NEWLINE* EOF
    ;

/**
 *
 * Base statements
 *
 */
stmt
    : simple_stmt
    | compound_stmt
    ;

simple_stmt
    : small_stmt ( ';' small_stmt )* ';'? NEWLINE
    ;

small_stmt
    : expr_stmt
//    | import_stmt
    | flow_stmt
    | pass_stmt;

compound_stmt
    : if_stmt
    | while_stmt
    | funcdef;

/**
 *
 * Compound statements
 *
 */

if_stmt:
    IF test ':' suite if_elif* if_else?;

if_elif:
    ELIF test ':' suite;

if_else:
    ELSE ':' suite;

while_stmt
    : WHILE test ':' suite //( ELSE ':' suite )?
    ;

funcdef
    : DEF NAME parameters ':' suite;

parameters
    : '(' param_argslist? ')'
    ;

param_argslist
    : (NAME ',')* NAME ;

suite
    : simple_stmt
    | NEWLINE INDENT stmt+ DEDENT
    ;

/**
 *
 * Small statements
 *
 */

expr_stmt
    : test                # ExprStmtExpr
    | NAME '=' test       # ExprStmtAssign
    | NAME augassign test # ExprStmtAugmented
    ;

augassign : '+=' | '-=' | '*=' | '/=' | '%='
          | '<<=' | '>>=' | '&=' | '|=' | '^='
          ;
//expr_stmt
//    : testlist_expr  ( '=' ( testlist_expr ) )*
//    ;


flow_stmt
    : return_stmt
    | break_stmt
    | continue_stmt
    ;

return_stmt:   RETURN test?;
pass_stmt:     PASS;
break_stmt:    BREAK;
continue_stmt: CONTINUE;

/**
 *
 * Common stuff: comparisons, arithmetic and logic expressions
 *
 * Rules "tests" and "expr" from the official grammar were re-written in order
 * to make AST construction easier; ANTLR handles left recursion for us
 *
 */


test    : expr                  # TestExpr
        | test comp_op test     # Comparison
        | NOT test              # NotTest
        | test AND test         # AndTest
        | test OR test          # OrTest
        ;

comp_op     : '<' | '>' | '==' | '>=' | '<=' | '<>' | '!='
            | IN | NOT IN | IS | IS NOT
            ;


expr    : factor                            # FactorExpr
        | expr op=( '*' | '/' | '%' ) expr  # MulDivMod
        | expr op=( '+' | '-' )       expr  # AddSub
        | expr op=( '<<' | '>>' )     expr  # Shifts
        | expr op='&' expr                  # BitAnd
        | expr op='^' expr                  # BitXor
        | expr op='|' expr                  # BitOr
        ;

factor
    : op='+' factor    # unaryExpr
    | op='-' factor    # unaryExpr
    | '(' test ')'     # parenExpr
    | atom             # atomExpr
    ;

atom
    : NAME
    | funcinvoke
    | number
    | string+
    | NONE
    | TRUE
    | FALSE
    ;

funcinvoke
    : NAME '(' arglist? ')'
    ;

arglist
    : (test ',')* test
    ;
/**
 *
 * Strings and numbers
 *
 */

number
    : integer
    | FLOAT_NUMBER
    ;

integer
    : DECIMAL_INTEGER
    | HEX_INTEGER
    ;

FLOAT_NUMBER
    : POINT_FLOAT
    | EXPONENT_FLOAT
    ;

string
    : STRING_LITERAL
    ;

//*******************************************************//
// Lexer Rules                                           //
//*******************************************************//

DEF    : 'def';
RETURN : 'return';
FROM   : 'from';
IMPORT : 'import';
AS     : 'as';
DEL    : 'del';
PASS   : 'pass';
BREAK  : 'break';
CONTINUE : 'continue';

IF   : 'if';
ELIF : 'elif';
ELSE : 'else';

WHILE: 'while';
FOR  : 'for';
IN   : 'in';

OR  : 'or';
AND : 'and';
NOT : 'not';
IS  : 'is';

NONE  : 'None';
TRUE  : 'True';
FALSE : 'False';

NEWLINE
    : ( {self.atStartOfInput()}? SPACES
      | ( '\r'? '\n' | '\r' )    SPACES?
      )
      { self.newLineAction() }
    ;

COMMA  : ',';
COLON  : ':';

OPEN_PAREN  : '(' { self.opened += 1 };
CLOSE_PAREN : ')' { self.opened -= 1 };

LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';

STAR   : '*';
POWER  : '**';
ASSIGN : '=';
ADD    : '+';
MINUS  : '-';
DIV    : '/';
MOD    : '%';
OR_OP  : '|';
XOR    : '^';
AND_OP : '&';

LESS_THAN    : '<';
GREATER_THAN : '>';
EQUALS       : '==';
GT_EQ        : '>=';
LT_EQ        : '<=';
NOT_EQ_1     : '<>';
NOT_EQ_2     : '!=';


ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
AT_ASSIGN : '@=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
POWER_ASSIGN : '**=';
IDIV_ASSIGN : '//=';

NAME
    : ID_START ID_CONTINUE*;

STRING_LITERAL
    : [uU]? [rR]? ( SHORT_STRING );

DECIMAL_INTEGER
    : NON_ZERO_DIGIT DIGIT* | '0'+;

HEX_INTEGER
    : '0' [xX] HEX_DIGIT+;

SKIP
    : ( SPACES | COMMENT ) -> skip
    ;

UNKNOWN_CHAR
    : .
    ;

CYRILLIC_RANGE : [\u0400-\u04FF] ;

fragment SPACES: [ \t]+;
fragment COMMENT: '#' ~[\r\n]*;
fragment ID_START: '_' | [A-Z] | [a-z] | CYRILLIC_RANGE;
fragment ID_CONTINUE: ID_START | [0-9];

fragment NON_ZERO_DIGIT : [1-9];
fragment DIGIT          : [0-9];
fragment OCT_DIGIT      : [0-7];
fragment HEX_DIGIT      : [0-9a-fA-F];

fragment SHORT_STRING
    : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n'] )* '\''
    | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"'
    ;

fragment STRING_ESCAPE_SEQ
    : '\\' .
    ;

fragment POINT_FLOAT
    : INT_PART? FRACTION
    | INT_PART '.'
    ;


fragment EXPONENT_FLOAT
    : ( INT_PART | POINT_FLOAT ) EXPONENT
    ;

fragment INT_PART: DIGIT+;
fragment FRACTION: '.' DIGIT+;
fragment EXPONENT: [eE] [+-]? DIGIT+;

