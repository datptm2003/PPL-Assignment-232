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

.method public static main([Ljava/lang/String;)V
.var 1 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is a F from Label0 to Label1
	ldc 1.0
	fstore_2
	fload_2
Label9:
	fload_2
	ldc 5.0
	fcmpl
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
	fload_2
	invokestatic io/writeNumber(F)V
	ldc "-"
	invokestatic io/writeString(Ljava/lang/String;)V
Label7:
	ldc 1.0
	fload_2
	fadd
	fstore_2
	goto Label9
Label8:
	return
Label1:
.limit stack 12
.limit locals 3
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