//POP TEMP
// *(5+i) = *(*SP-1)

@%s
D=A
@5
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1