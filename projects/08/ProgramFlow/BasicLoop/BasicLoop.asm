// PUSH CONSTANT

// *SP=i
//SP++

@0
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
D=M+D
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// Label

(LOOP_START)
// PUSH ARGUMENT

// d = *(*ARG+i)
// *SP = d
// SP++


@0
D=A
@ARG
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH LOCAL

// d = *(*LCL+i)
// *SP = d
// SP++


@0
D=A
@LCL
A=D+M
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
// POP LOCAL
//R13=*(*LCL+i)
//SP--
//*R13=*SP



@0
D=A
@LCL
D=M+D
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH ARGUMENT

// d = *(*ARG+i)
// *SP = d
// SP++


@0
D=A
@ARG
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@1
D=A
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
// POP ARGUMENT
//R13=*(*ARG+i)
//SP--
//*R13=*SP



@0
D=A
@ARG
D=M+D
@R13
M=D

@SP
M=M-1
A=M
D=M

@R13
A=M
M=D
// PUSH ARGUMENT

// d = *(*ARG+i)
// *SP = d
// SP++


@0
D=A
@ARG
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1
// if-goto Label Name

@SP
M=M-1
@SP
A=M
D=M
@LOOP_START
D;JNE
// PUSH LOCAL

// d = *(*LCL+i)
// *SP = d
// SP++


@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
