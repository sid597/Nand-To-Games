// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Foo.%s
M=D
