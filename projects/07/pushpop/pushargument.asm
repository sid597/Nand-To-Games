// d = *(*ARG+i)
// *SP = d
// SP++


@%s
D=A
@ARG
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1