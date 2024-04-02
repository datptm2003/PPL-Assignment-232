.text
.globl main
main:
	addi $t1,$t1,4
	addi $t2,$t2,3
	add $s1,$s1,$t1
	add $s2,$s2,$t2
	add $s0,$s1,$s2

	add $a0,$s0,$zero
	li $v0,1
	syscall

	li $v0,10
	syscall
