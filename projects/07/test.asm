// PUSH CONSTANT

// *SP=i
//SP++

@10
D=A
@SP
A=M
M=D

@SP
M=M+1
// POP LOCAL
//R13=*(*LCL+i)
//SP--
//*R13=*SP


@0
D=A
@LCL
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH CONSTANT

// *SP=i
//SP++

@21
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@22
D=A
@SP
A=M
M=D

@SP
M=M+1
// POP ARGUMENT
//R13=*(*ARG+i)
//SP--
//*R13=*SP


@2
D=A
@ARG
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// POP ARGUMENT
//R13=*(*ARG+i)
//SP--
//*R13=*SP


@1
D=A
@ARG
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH CONSTANT

// *SP=i
//SP++

@36
D=A
@SP
A=M
M=D

@SP
M=M+1
// POP THIS

//R13=*(*THIS+i)
//SP--
//*R13=*SP


@6
D=A
@THIS
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH CONSTANT

// *SP=i
//SP++

@42
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@45
D=A
@SP
A=M
M=D

@SP
M=M+1
//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@5
D=A
@THAT
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@2
D=A
@THAT
A=D+M
D=M
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH CONSTANT

// *SP=i
//SP++

@510
D=A
@SP
A=M
M=D

@SP
M=M+1
//POP TEMP
// *(5+i) = *(*SP-1)

@6
D=A
%5
D=M+D