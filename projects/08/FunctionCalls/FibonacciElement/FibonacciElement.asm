@261
D=A
@SP
M=D
@Sys.init
D;JMP
//FUNCTION COMMAND
(Sys.init)
// PUSH CONSTANT

// *SP=i
//SP++

@4
D=A
@SP
A=M
M=D

@SP
M=M+1
// CALL FUNCTION

//add return label Main.fibonacci *SP = Main.fibonacci
@return.Main.fibonacci2
D=A
@SP
A=M
M=D
@SP
M=M+1

//save LCL -> *SP= LCL,SP++
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// save ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// Lcl = Sp
@SP
D=M
@LCL
M=D


// ARG = SP - (nargs+5)
@R5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Main.fibonacci
@Main.fibonacci
D;JMP

//label return.Main.fibonacci2
(return.Main.fibonacci2)
// LABEL COMMAND

(Sys$WHILE)
 
// GOTO COMMAND

@Sys$WHILE
D;JMP
 
//FUNCTION COMMAND
(Main.fibonacci)
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
//LT
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
D=M-D
@TRUEMain3
D;JLT
@FALSEMain3
D;JGE
(TRUEMain3)
@SP
A=M-1
M=-1
@OUTMain3
0;JMP
(FALSEMain3)
@SP
A=M-1
M=0
(OUTMain3)
// if-goto COMMAND Name

@SP
M=M-1
@SP
A=M
D=M
@IF_TRUE
D;JNE
// GOTO COMMAND

@Main$IF_FALSE
D;JMP
 
// LABEL COMMAND

(Main$IF_TRUE)
 
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
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.Main.fibonacci
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@ret.Main.fibonacci8
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
@endframe.Main.fibonacci
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Main.fibonacci8
A=M
D;JMP
// LABEL COMMAND

(Main$IF_FALSE)
 
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
// CALL FUNCTION

//add return label Main.fibonacci *SP = Main.fibonacci
@return.Main.fibonacci13
D=A
@SP
A=M
M=D
@SP
M=M+1

//save LCL -> *SP= LCL,SP++
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// save ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// Lcl = Sp
@SP
D=M
@LCL
M=D


// ARG = SP - (nargs+5)
@R5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Main.fibonacci
@Main.fibonacci
D;JMP

//label return.Main.fibonacci13
(return.Main.fibonacci13)
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
// CALL FUNCTION

//add return label Main.fibonacci *SP = Main.fibonacci
@return.Main.fibonacci17
D=A
@SP
A=M
M=D
@SP
M=M+1

//save LCL -> *SP= LCL,SP++
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1

// save ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1

//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1

// Lcl = Sp
@SP
D=M
@LCL
M=D


// ARG = SP - (nargs+5)
@R5
D=A
@1
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Main.fibonacci
@Main.fibonacci
D;JMP

//label return.Main.fibonacci17
(return.Main.fibonacci17)
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.Main.fibonacci
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@ret.Main.fibonacci19
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
@endframe.Main.fibonacci
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Main.fibonacci
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Main.fibonacci19
A=M
D;JMP
