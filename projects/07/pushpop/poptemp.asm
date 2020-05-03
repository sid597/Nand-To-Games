// *(5+i) = *(*SP-1)


@%s
D=M
%5
D=M+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D