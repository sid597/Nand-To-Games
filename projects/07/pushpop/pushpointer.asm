//*SP = This 0
//*SP = That 1
//SP++

@%s
D=M
@This
D;JEQ
@That
D;JNE
(This)
@THIS
D=M
@SP
A=M
M=D
@End
0;JMP
(That)
@THAT
D=M
@SP
A=M
M=D
(End)
@SP
M=M+1