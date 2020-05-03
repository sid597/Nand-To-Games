//PUSH THIS

// d = *(*THIS+i)
// *SP = d
// SP++


@%s
D=A
@THIS
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1