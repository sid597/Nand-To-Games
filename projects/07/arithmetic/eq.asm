// EQ
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
D=M-D
@TRUE%t
D;JEQ
@FALSE%t
D;JNE
(TRUE%t)
@SP
A=M-1
M=-1
@OUT%t
0;JMP
(FALSE%t)
@SP
A=M-1
M=0
(OUT%t)