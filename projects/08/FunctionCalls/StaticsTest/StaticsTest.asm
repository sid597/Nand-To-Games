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

@6
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
// CALL FUNCTION

//add return label Class1.set *SP = Class1.set
@return.Class1.set3
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
@2
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Class1.set
@Class1.set
D;JMP

//label return.Class1.set3
(return.Class1.set3)
//POP TEMP
// *(5+i) = *(*SP-1)

@0
D=A
@5
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
// PUSH CONSTANT

// *SP=i
//SP++

@23
D=A
@SP
A=M
M=D

@SP
M=M+1
// PUSH CONSTANT

// *SP=i
//SP++

@15
D=A
@SP
A=M
M=D

@SP
M=M+1
// CALL FUNCTION

//add return label Class2.set *SP = Class2.set
@return.Class2.set7
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
@2
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Class2.set
@Class2.set
D;JMP

//label return.Class2.set7
(return.Class2.set7)
//POP TEMP
// *(5+i) = *(*SP-1)

@0
D=A
@5
D=A+D
@R13
M=D
@SP
A=M-1
D=M
@R13
A=M
M=D
@SP
M=M-1
// CALL FUNCTION

//add return label Class1.get *SP = Class1.get
@return.Class1.get9
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
@0
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Class1.get
@Class1.get
D;JMP

//label return.Class1.get9
(return.Class1.get9)
// CALL FUNCTION

//add return label Class2.get *SP = Class2.get
@return.Class2.get10
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
@0
D=D+A
@SP
D=M-D
@ARG
M=D


//goto Class2.get
@Class2.get
D;JMP

//label return.Class2.get10
(return.Class2.get10)
// LABEL COMMAND

(Sys$WHILE)
 
// GOTO COMMAND

@Sys$WHILE
D;JMP
 
//FUNCTION COMMAND
(Class2.set)
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
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Class2.0
M=D
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
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Class2.1
M=D
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
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.Class2.set
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Class2.set
A=M-D
D=M
@ret.Class2.set6
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
@endframe.Class2.set
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Class2.set
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Class2.set
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Class2.set
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Class2.set6
A=M
D;JMP
//FUNCTION COMMAND
(Class2.get)
// PUSH STATIC

// *SP = *foo.i
// SP++


@Class2.0
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH STATIC

// *SP = *foo.i
// SP++


@Class2.1
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
@endframe.Class2.set
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Class2.set
A=M-D
D=M
@ret.Class2.set11
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
@endframe.Class2.set
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Class2.set
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Class2.set
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Class2.set
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Class2.set11
A=M
D;JMP
//FUNCTION COMMAND
(Class1.set)
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
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Class1.0
M=D
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
// POP STATIC
// SP--
//foo.i = *SP
//SP++
@SP
M=M-1
@SP
A=M
D=M
@Class1.1
M=D
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
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.Class1.set
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Class1.set
A=M-D
D=M
@ret.Class1.set6
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
@endframe.Class1.set
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Class1.set
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Class1.set
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Class1.set
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Class1.set6
A=M
D;JMP
//FUNCTION COMMAND
(Class1.get)
// PUSH STATIC

// *SP = *foo.i
// SP++


@Class1.0
D=M

@SP
A=M
M=D

@SP
M=M+1
// PUSH STATIC

// *SP = *foo.i
// SP++


@Class1.1
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
@endframe.Class1.set
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Class1.set
A=M-D
D=M
@ret.Class1.set11
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
@endframe.Class1.set
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Class1.set
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Class1.set
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Class1.set
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Class1.set11
A=M
D;JMP
