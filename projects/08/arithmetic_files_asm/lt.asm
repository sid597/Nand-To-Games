//LT
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
D=M-D
@TRUE$%t
D;JLT
@FALSE$%t
D;JGE
(TRUE$%t)
@SP
A=M-1
M=-1
@OUT$%t
0;JMP
(FALSE$%t)
@SP
A=M-1
M=0
(OUT$%t)