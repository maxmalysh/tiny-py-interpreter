grammar TinyPy;

options
{
    language=Python3;
}

tokens { INDENT, DEDENT }

//@lexer::header {
//
//}

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

/**
 *
 * Base statements
 *
 */
stmt
    : simple_stmt ;

simple_stmt
    : small_stmt ( ';' small_stmt )* ';'? NEWLINE
    ;

small_stmt
    : expr_stmt
//    | import_stmt
    | pass_stmt;

expr_stmt
    : testlist_expr  ( '=' ( testlist_expr ) )*
    ;

testlist_expr
    : ( expr ) ( ',' ( expr ) )* ','?
    ;

/**
 *
 * Arithmetic and logic expressions
 *
 */
expr
    : xor_expr ( '|' xor_expr )*;

xor_expr
    : and_expr ( '^' and_expr )*;

and_expr
    : shift_expr ( '&' shift_expr )*;


shift_expr
    : arith_expr ( '<<' arith_expr
                 | '>>' arith_expr
                 )*
    ;

arith_expr
    : term ( '+' term
           | '-' term
           )*
     ;

term
    : factor ( '*' factor
             | '/' factor
             | '%' factor
             )*
    ;

factor
    : '+' factor
    | '-' factor
    | '~' factor
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

/**
 *
 *
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

/**
 *
 * Other statements
 *
 */

pass_stmt:
     PASS;




//*******************************************************//
// Lexer Rules                                           //
//*******************************************************//

fragment ID_START: '_' | [A-Z] | [a-z];
fragment ID_CONTINUE: ID_START | [0-9];

NAME: ID_START ID_CONTINUE*;

STRING_LITERAL: [uU]? [rR]? ( SHORT_STRING );

DECIMAL_INTEGER: NON_ZERO_DIGIT DIGIT* | '0'+;
HEX_INTEGER: '0' [xX] HEX_DIGIT+;

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


PASS : 'pass';
NONE : 'None';
TRUE : 'True';
FALSE : 'False';
//NEWLINE: '\n';
NEWLINE:
    (   {self.atStartOfInput()}? SPACES |
        ( '\r'? '\n' | '\r' ) SPACES?
    )
    { self.zefAction() }
    ;

fragment SPACES: [ \t]+;
fragment COMMENT: '#' ~[\r\n]*;


SKIP
    : ( SPACES | COMMENT ) -> skip
    ;

/*
FLOAT_NUMBER
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;
/// pointfloat    ::=  [intpart] fraction | intpart "."
fragment POINT_FLOAT
 : INT_PART? FRACTION
 | INT_PART '.'
 ;

/// exponentfloat ::=  (intpart | pointfloat) exponent
fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;

/// intpart       ::=  digit+
fragment INT_PART
 : DIGIT+
 ;

/// fraction      ::=  "." digit+
fragment FRACTION
 : '.' DIGIT+
 ;

/// exponent      ::=  ("e" | "E") ["+" | "-"] digit+
fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;
 */
