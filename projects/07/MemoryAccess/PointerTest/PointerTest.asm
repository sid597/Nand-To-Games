// PUSH CONSTANT

// *SP=i
//SP++

@3030
D=A
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
@0
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

@3040
D=A
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
@This3
D;JEQ
@That3
D;JNE
(This3)
@SP
A=M
D=M
@THIS
M=D
@Out3
0;JMP
(That3)
@SP
A=M
D=M
@THAT
M=D
(Out3)
// PUSH CONSTANT

// *SP=i
//SP++

@32
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


@2
D=A
@THIS
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

@46
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


@6
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

@0
D=A
@This8
D;JEQ
@That8
D;JNE
(This8)
@THIS
D=M
@SP
A=M
M=D
@End8
0;JMP
(That8)
@THAT
D=M
@SP
A=M
M=D
(End8)
@SP
M=M+1
//PUSH POINTER

//*SP = This 0
//*SP = That 1
//SP++

@1
D=A
@This9
D;JEQ
@That9
D;JNE
(This9)
@THIS
D=M
@SP
A=M
M=D
@End9
0;JMP
(That9)
@THAT
D=M
@SP
A=M
M=D
(End9)
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
//PUSH THIS

// d = *(*THIS+i)
// *SP = d
// SP++


@2
D=A
@THIS
A=D+M
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
// PUSH THAT

// d = *(*THAT+i)
// *SP = d
// SP++


@6
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
