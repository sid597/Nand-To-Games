// PUSH TEMP

// *SP=*(5+i)
// SP++

@%s
D=A
@5
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1