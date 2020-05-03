// PUSH CONSTANT

// *SP=i
//SP++

@7
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@8
D=A
@SP
A=M
M=D

@SP
M=M+1
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
