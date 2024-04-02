.text
.globl main
main:
	addi $t1,$t1,16

	add $a0,$t1,$zero
	li $v0,1
	syscall

	li $v0,10
	syscall
