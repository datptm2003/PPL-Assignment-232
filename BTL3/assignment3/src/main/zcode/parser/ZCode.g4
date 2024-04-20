grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program:		newline_list declaration EOF;

declaration:	dclr newline_list declaration | dclr;
dclr:		    (var_dclr | func_dclr) NEWLINE newline_list | func_imp;

newline_list:	newline_prime | ;
newline_prime:	NEWLINE newline_prime | NEWLINE;

var_dclr: 		VAR ID ASSIGN expr | (var_type | DYNAMIC) ID (ASSIGN expr)? | arr_dclr;

para_list:		para_prime | ;
para_prime: 	para_dclr SEP para_prime | para_dclr;
para_dclr: 		var_type (ID | array);
var_type: 		BOOL_TYPE | NUM_TYPE | STR_TYPE;

func_imp: 		func_dclr newline_list (block | return_stmt) NEWLINE newline_list;
block:			BEGIN NEWLINE newline_list stmt_list END;

func_dclr: 		FUNC ID OPEN_BRK para_list CLOSE_BRK;

func_call_stmt:		ID OPEN_BRK expr_list CLOSE_BRK;
func_call_expr:		ID OPEN_BRK expr_list CLOSE_BRK;


arr_dclr:		var_type array ASSIGN expr | var_type array;
array:			ID OPEN_IDX num_prime CLOSE_IDX;

arr_acs:		(ID | func_call_expr) OPEN_IDX expr_prime CLOSE_IDX;


arr_elmt:		OPEN_IDX expr_prime CLOSE_IDX;

num_prime:		NUMBER SEP num_prime | NUMBER;

expr_list:		expr_prime | ;
expr_prime:		expr SEP expr_prime | expr;


expr:			expr1 STR_CONCAT expr1 | expr1;
expr1:			expr2 cmpr_type expr2 | expr2;
expr2:			expr2 (AND | OR) expr3 | expr3;
expr3:			expr3 (ADD | SUB) expr4 | expr4;
expr4:			expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5:			NOT expr5 | expr6;
expr6:			SUB expr6 | expr7;
expr7:			OPEN_BRK expr CLOSE_BRK
				| arr_elmt
				| arr_acs
 				| func_call_expr
				| ID
 				| BOOL | NUMBER | STRING;
				
				

cmpr_type:		EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL | STR_EQUAL;

assgn_expr:		ID (OPEN_IDX expr_prime CLOSE_IDX)? ASSIGN expr;


if_stmt:		IF OPEN_BRK expr CLOSE_BRK newline_list stmt elif_prime else_stmt;
// elif_list:		elif_prime | ;
elif_prime:		elif_stmt elif_prime | ;
elif_stmt:		ELIF OPEN_BRK expr CLOSE_BRK newline_list stmt;
else_stmt:		ELSE newline_list stmt | ;

for_stmt:		FOR ID UNTIL expr BY expr newline_list stmt;

return_stmt:	RETURN expr | RETURN;

stmt_list:		stmt_prime | ;
stmt_prime:		stmt stmt_prime | stmt;
stmt: 			if_stmt 
				| for_stmt 
				| (BREAK
				| CONTINUE
				| block
				| var_dclr 
				| arr_dclr 
				| assgn_expr
				// | arr_assgn
				| func_call_stmt
				| return_stmt) NEWLINE newline_list;




// Keywords: FUNCTION
RETURN: 		'return';
FUNC: 			'func';
// MAIN:			'main';

// Keywords: LOOP
FOR: 			'for';
UNTIL: 			'until';
BY: 			'by';
BREAK: 			'break';
CONTINUE: 		'continue';

// Keywords: VARIABLE
VAR: 			'var';
DYNAMIC: 		'dynamic';
BOOL_TYPE: 		'bool';
NUM_TYPE: 		'number';
STR_TYPE: 		'string';

// Keywords: CONDITION
IF: 			'if';
ELSE: 			'else';
ELIF: 			'elif';

// Keywords: CODE BLOCK
BEGIN: 			'begin';
END: 			'end';

// Variable values
BOOL: 					'true' | 'false';
NUMBER: 				DIGIT+ DEC_PART? EXPO_PART?;
STRING: 				'"' ('\''* (ESC_SEQ | DBL_QUOTES | ~["'\\\n\r]))* '"' {self.text = self.text[1:-1]};

fragment DIGIT: 		[0-9];
fragment DEC_PART: 		'.' DIGIT*;
fragment EXPO_PART: 	[eE] [+-]? DIGIT+;
fragment ESC_SEQ: 		'\\' [nbrtf'\\];
fragment DBL_QUOTES:	'\'"';

// Operators
ASSIGN: 		'<-';
NOT: 			'not';
AND: 			'and';
OR: 			'or';
EQUAL: 			'=';
STR_EQUAL: 		'==';
NOT_EQUAL: 		'!=';
LESS: 			'<';
GREATER: 		'>';
LESS_EQUAL: 	'<=';
GREATER_EQUAL: 	'>=';
ADD: 			'+';
SUB: 			'-';
MUL: 			'*';
DIV: 			'/';
MOD: 			'%';
STR_CONCAT: 	'...';
OPEN_IDX: 		'[';
CLOSE_IDX: 		']';
OPEN_BRK: 		'(';
CLOSE_BRK: 		')';
SEP: 			','; 

// Identifier
ID: 			[a-zA-Z_] [a-zA-Z0-9_]*;

// Comment
COMMENT: 		'##' ~[\r\n]* -> skip;

/******* TODO *******/
NEWLINE: 		[\r\n] | '\r\n' {
	self.text = '\n'
};
WS: 			[ \t\b\f]+ -> skip ;

UNCLOSE_STRING: '"' ('\''* (ESC_SEQ | DBL_QUOTES | ~["'\\\n\r]))* {
	raise UncloseString(self.text[1:].replace('\n', '').replace('\r', ''))
};
ILLEGAL_ESCAPE: '"' ('\''* (ESC_SEQ | DBL_QUOTES | ~["'\\\n\r]))* ('\\' ~[nbrtf'\\]) {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: 	. {raise ErrorToken(self.text)};

/********************/
