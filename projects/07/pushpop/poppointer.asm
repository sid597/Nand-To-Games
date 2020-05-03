// POP POINTER
//SP--
//THIS=*SP   if 0
//THAT=*SP   if 1

@SP
M=M-1
@%s
D=A
@This%t
D;JEQ
@That%t
D;JNE
(This%t)
@SP
A=M
D=M
@THIS
M=D
@Out%t
0;JMP
(That%t)
@SP
A=M
D=M
@THAT
M=D
(Out%t)