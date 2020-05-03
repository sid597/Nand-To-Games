// *SP = *foo.i
// SP++

@%s
D=M
@Foo.%s
M=D

@SP
A=M
M=D

@SP
M=M+1
