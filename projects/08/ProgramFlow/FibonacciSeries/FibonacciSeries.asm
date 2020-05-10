// PUSH ARGUMENT

// d = *(*ARG+i)
// *SP = d
// SP++


@1
D=A
@ARG
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1
// POP POINTER
//SP--
//THIS=*SP   if 0
//THAT=*SP   if 1

@SP
M=M-1
@1
D=A
@This1
D;JEQ
@That1
D;JNE
(This1)
@SP
A=M
D=M
@THIS
M=D
@Out1
0;JMP
(That1)
@SP
A=M
D=M
@THAT
M=D
(Out1)
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
//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@0
D=A
@THAT
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
//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@1
D=A
@THAT
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

@2
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
// Label

(MAIN_LOOP_START)
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
@COMPUTE_ELEMENT
D;JNE
// Label

@END_PROGRAM
D;JMP
// Label

(COMPUTE_ELEMENT)
// PUSH THAT

// d = *(*THAT+i)
// *SP = d
// SP++


@0
D=A
@THAT
A=D+M
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH THAT

// d = *(*THAT+i)
// *SP = d
// SP++


@1
D=A
@THAT
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
//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@2
D=A
@THAT
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
//PUSH POINTER

//*SP = This 0
//*SP = That 1
//SP++

@1
D=A
@This19
D;JEQ
@That19
D;JNE
(This19)
@THIS
D=M
@SP
A=M
M=D
@End19
0;JMP
(That19)
@THAT
D=M
@SP
A=M
M=D
(End19)
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
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
// POP POINTER
//SP--
//THIS=*SP   if 0
//THAT=*SP   if 1

@SP
M=M-1
@1
D=A
@This22
D;JEQ
@That22
D;JNE
(This22)
@SP
A=M
D=M
@THIS
M=D
@Out22
0;JMP
(That22)
@SP
A=M
D=M
@THAT
M=D
(Out22)
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
// Label

@MAIN_LOOP_START
D;JMP
// Label

(END_PROGRAM)
