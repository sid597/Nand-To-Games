//sp--
@sp
M=M-1
// d = *sp
@sp
A=M
D=M
//sp--
@sp
M=M-1
// *sp = D-*sp
@sp
A=M
D=D-M

@LT
D;JLT

@NLT
D;JGE
(LT)
@sp
A=M
M=1
@sp
M=M+1
@L
0;JMP

(NLT)
@sp
A=M
M=0
@sp
M=M+1

(L)





//sp++
//@sp
//M=M+