// PUSH LOCAL

// d = *(*LCL+i)
// *SP = d
// SP++
@%s
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1