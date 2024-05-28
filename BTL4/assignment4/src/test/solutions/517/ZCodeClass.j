.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public static $concat2string(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
    new java/lang/StringBuilder
    dup
    invokespecial java/lang/StringBuilder/<init>()V

    aload_0
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    aload_1
    invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
    areturn
                           
    .limit stack 3
    .limit locals 3
.end method

.method public static $compare2string(Ljava/lang/String;Ljava/lang/String;)Z
    aload_0
    aload_1

    invokevirtual java/lang/String/equals(Ljava/lang/Object;)Z
    ; Return the result
    ireturn
             
    .limit stack 2
    .limit locals 2
.end method

.method public static $modulo2float(FF)F
    fload_0
    fload_1

    fload_0
    fload_1
    fdiv         
    f2d          
    invokestatic java/lang/Math/floor(D)D
    d2f

    fload_1
    fmul

    fload_0
    fsub
    fneg

    freturn
    
    .limit stack 4
    .limit locals 3
.end method

.method public <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static help(FF)F
.var 0 is x F from Label0 to Label1
.var 1 is y F from Label0 to Label1
Label0:
	ldc 6.0
	ldc 5.0
	fdiv
	fload_0
	fadd
	freturn
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 2 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 3 is a F from Label0 to Label1
	ldc 5.0
	fstore_3
.var 4 is b F from Label0 to Label1
	ldc 11.0
	fstore 4
	fload_3
	fload 4
	invokestatic ZCodeClass/help(FF)F
	invokestatic io/writeNumber(F)V
	return
Label1:
.limit stack 16
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LZCodeClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
