// PUSH CONSTANT

// *SP=i
//SP++

@111
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@333
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@888
D=A
@SP
A=M
M=D

@SP
M=M+1
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Foo.8
M=D
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Foo.3
M=D
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Foo.1
M=D
// PUSH STATIC

// *SP = *foo.i
// SP++


@Foo.3
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH STATIC

// *SP = *foo.i
// SP++


@Foo.1
D=M

@SP
A=M
M=D

@SP
M=M+1
//Sub
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M-D
// PUSH STATIC

// *SP = *foo.i
// SP++


@Foo.8
D=M

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
