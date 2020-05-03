//PUSH POINTER

//*SP = This 0
//*SP = That 1
//SP++

@%s
D=A
@This%t
D;JEQ
@That%t
D;JNE
(This%t)
@THIS
D=M
@SP
A=M
M=D
@End%t
0;JMP
(That%t)
@THAT
D=M
@SP
A=M
M=D
(End%t)
@SP
M=M+1