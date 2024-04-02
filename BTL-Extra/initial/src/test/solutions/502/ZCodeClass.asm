.text
.globl main
main:
	addi $t1,$t1,1
	addi $t2,$t2,2
	add $s1,$s1,$t1
	add $s2,$s2,$t2
	add $s0,$s1,$s2
	addi $t3,$t3,3
	add $s3,$s3,$s0
	add $s4,$s4,$t3
	add $s5,$s3,$s4

	add $a0,$s5,$zero
	li $v0,1
	syscall

	li $v0,10
	syscall
