//SP--
//THIS=*SP   if 0
//THAT=*SP   if 1

@SP
M=M-1
@%s
D=M
@This
D;JEQ
@That
D;JNE
(This)
@SP
A=M
D=M
@THIS
M=D
@Out
0;JMP
(That)
@SP
A=M
D=M
@THAT
M=D
(Out)