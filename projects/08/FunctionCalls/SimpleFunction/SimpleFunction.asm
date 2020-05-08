@256
D=A
@SP
M=D
@Sys.init
D;JMP
//FUNCTION COMMAND
(SimpleFunction.test)
@R0
D=A
@SP
A=M
M=D
@SP
M=M+1
 
@R0
D=A
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
// PUSH LOCAL

// d = *(*LCL+i)
// *SP = d
// SP++


@1
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
//Not
@SP
A=M-1
M=!M
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
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
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
//Sub
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M-D
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.SimpleFunction.test
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.SimpleFunction.test
A=M-D
D=M
@ret.SimpleFunction.test9
M=D

//*ARG = last element
@SP
A=M-1
D=M
@ARG
A=M
M=D

//SP =ARG + 1
@ARG
D=M+1
@SP
M=D

// LCL = endframe - 4
@4
D=A
@endframe.SimpleFunction.test
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.SimpleFunction.test
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.SimpleFunction.test
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.SimpleFunction.test
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.SimpleFunction.test9
A=M
D;JMP
