grammar TinyPy;

options
{
    language=Python3;
}

tokens { INDENT, DEDENT }

@lexer::members {
def atStartOfInput(self):
    return self.column == 0 and self.line == 1
}

//******************************************************//
// Parser Rules                                         //
//******************************************************//

/**
 *
 * Different input types
 *
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

if_stmt
    : IF test ':' suite ( ELIF test ':' suite )* ( ELSE ':' suite )?
    ;

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
    : expr ('=' expr)?;

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
 */
test        : or_test  ( IF or_test ELSE test )?;
or_test     : and_test ( OR and_test )*;
and_test    : not_test ( AND not_test )*;
not_test    : NOT not_test | comparison;
comparison  : expr ( comp_op expr )*;

comp_op     : '<' | '>' | '==' | '>=' | '<=' | '<>' | '!='
            | IN | NOT IN | IS | IS NOT
            ;

//expr_stmt
//    : testlist_expr  ( '=' ( testlist_expr ) )*
//    ;

//testlist_expr
//    : ( expr ) ( ',' ( expr ) )* ','?
//    ;

expr        : xor_expr   ( '|' xor_expr )*;
xor_expr    : and_expr   ( '^' and_expr )*;
and_expr    : shift_expr ( '&' shift_expr )*;
shift_expr  : arith_expr ( '<<' arith_expr | '>>' arith_expr)*;
arith_expr  : term ( '+' term | '-' term)*;

term
    : factor ( '*' factor
             | '/' factor
             | '%' factor
             )*
    ;

factor
    : '+' factor
    | '-' factor
    | '(' test ')'
    | funcinvoke
    | atom
    ;

atom
    : NAME
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
//    | FLOAT_NUMBER
    ;

integer
    : DECIMAL_INTEGER
    | HEX_INTEGER
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

LESS_THAN    : '<';
GREATER_THAN : '>';
EQUALS       : '==';
GT_EQ        : '>=';
LT_EQ        : '<=';
NOT_EQ_1     : '<>';
NOT_EQ_2     : '!=';

COMMA  : ',';
COLON  : ':';


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

fragment SPACES: [ \t]+;
fragment COMMENT: '#' ~[\r\n]*;
fragment ID_START: '_' | [A-Z] | [a-z];
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




