// d = *(*THAT+i)
// *SP = d
// SP++


@%s
D=A
@THAT
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1