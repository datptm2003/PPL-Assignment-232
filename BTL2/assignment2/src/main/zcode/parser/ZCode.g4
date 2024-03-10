grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// program: 		dclr_list (main_imp NEWLINE dclr_list | main_imp);
program:		newline_list declaration EOF;

// dclr_list:		declaration | ;
// declaration:	dclr declaration | dclr;
// dclr:			(var_dclr | func_imp | func_dclr) NEWLINE;

// dclr_list:		declaration | ;
declaration:	dclr newline_list declaration | dclr;
dclr:		    (var_dclr | func_dclr) NEWLINE newline_list | func_imp;

newline_list:	newline_prime | ;
newline_prime:	NEWLINE newline_prime | NEWLINE;

var_dclr: 		VAR ID ASSIGN expr | (var_type | DYNAMIC) ID (ASSIGN expr)? | arr_dclr;

para_list:		para_prime | ;
para_prime: 	para_dclr SEP para_prime | para_dclr;
para_dclr: 		var_type (ID | array);
var_type: 		BOOL_TYPE | NUM_TYPE | STR_TYPE;
// imp_var:		VAR | DYNAMIC;

func_imp: 		func_dclr newline_list (block | return_stmt) NEWLINE newline_list;
block:			BEGIN NEWLINE newline_list stmt_list END;

func_dclr: 		FUNC ID OPEN_BRK para_list CLOSE_BRK;

func_call_stmt:		ID OPEN_BRK expr_list CLOSE_BRK;
func_call_expr:		ID OPEN_BRK expr_list CLOSE_BRK;

// main_imp: 		FUNC MAIN OPEN_BRK CLOSE_BRK newline_list main_block;
// main_block:		BEGIN newline_list stmt_list END;

arr_dclr:		var_type array ASSIGN expr | var_type array;
array:			ID OPEN_IDX num_prime CLOSE_IDX;

arr_acs:		(ID | func_call_expr) OPEN_IDX expr_prime CLOSE_IDX;

// elmt_prime:		elmt SEP elmt_prime | elmt;
// elmt:			arr_elmt | expr;

// arr_list:		arr_prime | ;
// arr_prime:		arr_elmt SEP arr_prime | arr_elmt;

arr_elmt:		OPEN_IDX expr_prime CLOSE_IDX;

num_prime:		NUMBER SEP num_prime | NUMBER;

expr_list:		expr_prime | ;
expr_prime:		expr SEP expr_prime | expr;

// expr:			assoc_expr | cmpr_expr | concat_expr;

// assoc_expr:		OPEN_BRK assoc_expr CLOSE_BRK
// 				| OPEN_IDX elmt_prime CLOSE_IDX
// 				| SUB assoc_expr
// 				| NOT assoc_expr
// 				| assoc_expr (MUL | DIV | MOD) assoc_expr
// 				| assoc_expr (ADD | SUB) assoc_expr
// 				| assoc_expr (AND | OR) assoc_expr
// 				| arr_acs
//  				| func_call
// 				| ID
//  				| BOOL | NUMBER | STRING;

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
				
				

// expr:			ID | logic_expr | arith_expr | str_expr;

cmpr_type:		EQUAL | NOT_EQUAL | LESS | LESS_EQUAL | GREATER | GREATER_EQUAL | STR_EQUAL;

// logic_expr: 	OPEN_BRK logic_expr CLOSE_BRK
// 				| NOT logic_expr
// 				| logic_expr (AND | OR) logic_expr
// 				| arr_acs
// 				| func_call
// 				| cmpr_expr
// 				| ID
// 				| BOOL;

// arith_expr: 	SUB? OPEN_BRK arith_expr CLOSE_BRK
// 				| arith_expr (MUL | DIV | MOD) arith_expr
// 				| arith_expr (ADD | SUB) arith_expr
// 				| arr_acs
// 				| func_call
// 				| SUB? ID
// 				| SUB? NUMBER;

// str_expr: 		str_oprnd STR_CONCAT str_oprnd | str_oprnd;
// str_oprnd:		OPEN_BRK str_oprnd CLOSE_BRK
// 				| arr_acs
// 				| func_call
// 				| ID
// 				| BOOL | NUMBER | STRING;

assgn_expr:		ID (OPEN_IDX expr_prime CLOSE_IDX)? ASSIGN expr;
// arr_assgn:		ID OPEN_IDX expr_prime CLOSE_IDX ASSIGN expr;

// if_stmt:		IF OPEN_BRK logic_expr CLOSE_BRK NEWLINE? struct_body elif_list else_stmt;
// elif_list:		elif_prime | ;
// elif_prime:		elif_stmt elif_prime;
// elif_stmt:		ELIF OPEN_BRK logic_expr CLOSE_BRK NEWLINE? struct_body;
// else_stmt:		ELSE NEWLINE? struct_body | ;

// struct_body:	stmt | (return_stmt | block) NEWLINE;

// for_stmt:		FOR ID UNTIL logic_expr BY arith_expr NEWLINE? loop_body;
// loop_body:		stmt | (BREAK | CONTINUE | return_stmt | block) NEWLINE;

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


// read_io:        read_type OPEN_BRK CLOSE_BRK;
// read_type:		READ_NUM | READ_BOOL | READ_STR;

// wrt_io:			write_type OPEN_BRK expr CLOSE_BRK;
// write_type:		WRITE_NUM | WRITE_BOOL | WRITE_STR;



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

// IO
// READ_NUM:		'readNumber';
// WRITE_NUM:		'writeNumber';
// READ_BOOL:		'readBool';
// WRITE_BOOL:		'writeBool';
// READ_STR:		'readString';
// WRITE_STR:		'writeString';

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
