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

@4000
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
@ThisSys2
D;JEQ
@ThatSys2
D;JNE
(ThisSys2)
@SP
A=M
D=M
@THIS
M=D
@OutSys2
0;JMP
(ThatSys2)
@SP
A=M
D=M
@THAT
M=D
(OutSys2)
// PUSH CONSTANT

// *SP=i
//SP++

@5000
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
@ThisSys4
D;JEQ
@ThatSys4
D;JNE
(ThisSys4)
@SP
A=M
D=M
@THIS
M=D
@OutSys4
0;JMP
(ThatSys4)
@SP
A=M
D=M
@THAT
M=D
(OutSys4)
// CALL FUNCTION

//add return label Sys.main *SP = Sys.main
@return.Sys.main5
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


//goto Sys.main
@Sys.main
D;JMP

//label return.Sys.main5
(return.Sys.main5)
//POP TEMP
// *(5+i) = *(*SP-1)

@1
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
// LABEL COMMAND

(Sys$LOOP)
 
// GOTO COMMAND

@Sys$LOOP
D;JMP
 
//FUNCTION COMMAND
(Sys.main)
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
 
@R0
D=A
@SP
A=M
M=D
@SP
M=M+1
 
// PUSH CONSTANT

// *SP=i
//SP++

@4001
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
@ThisSys11
D;JEQ
@ThatSys11
D;JNE
(ThisSys11)
@SP
A=M
D=M
@THIS
M=D
@OutSys11
0;JMP
(ThatSys11)
@SP
A=M
D=M
@THAT
M=D
(OutSys11)
// PUSH CONSTANT

// *SP=i
//SP++

@5001
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
@ThisSys13
D;JEQ
@ThatSys13
D;JNE
(ThisSys13)
@SP
A=M
D=M
@THIS
M=D
@OutSys13
0;JMP
(ThatSys13)
@SP
A=M
D=M
@THAT
M=D
(OutSys13)
// PUSH CONSTANT

// *SP=i
//SP++

@200
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



@1
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
// PUSH CONSTANT

// *SP=i
//SP++

@40
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



@2
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
// POP LOCAL
//R13=*(*LCL+i)
//SP--
//*R13=*SP



@3
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
// PUSH CONSTANT

// *SP=i
//SP++

@123
D=A
@SP
A=M
M=D

@SP
M=M+1
// CALL FUNCTION

//add return label Sys.add12 *SP = Sys.add12
@return.Sys.add1221
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


//goto Sys.add12
@Sys.add12
D;JMP

//label return.Sys.add1221
(return.Sys.add1221)
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
// PUSH LOCAL

// d = *(*LCL+i)
// *SP = d
// SP++


@2
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


@3
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


@4
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
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
// Add
@SP
A=M-1
D=M
@SP
M=M-1
@SP
A=M-1
M=M+D
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
@endframe.Sys.init
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Sys.init
A=M-D
D=M
@ret.Sys.init32
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
@endframe.Sys.init
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Sys.init
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Sys.init
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Sys.init
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Sys.init32
A=M
D;JMP
//FUNCTION COMMAND
(Sys.add12)
// PUSH CONSTANT

// *SP=i
//SP++

@4002
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
@ThisSys35
D;JEQ
@ThatSys35
D;JNE
(ThisSys35)
@SP
A=M
D=M
@THIS
M=D
@OutSys35
0;JMP
(ThatSys35)
@SP
A=M
D=M
@THAT
M=D
(OutSys35)
// PUSH CONSTANT

// *SP=i
//SP++

@5002
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
@ThisSys37
D;JEQ
@ThatSys37
D;JNE
(ThisSys37)
@SP
A=M
D=M
@THIS
M=D
@OutSys37
0;JMP
(ThatSys37)
@SP
A=M
D=M
@THAT
M=D
(OutSys37)
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

@12
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
// RETURN COMMNAD
// Endframe = LCL
@LCL
D=M
// make this endframe unique to this method
@endframe.Sys.init
M=D

// This method returns address ReturnAddr = *(endframe -5)
@5
D=A
@endframe.Sys.init
A=M-D
D=M
@ret.Sys.init41
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
@endframe.Sys.init
A=M-D
D=M
@LCL
M=D

// ARG = endframe - 3
@3
D=A
@endframe.Sys.init
A=M-D
D=M
@ARG
M=D

// THIS = endframe - 2
@2
D=A
@endframe.Sys.init
A=M-D
D=M
@THIS
M=D

// THAT = endframe -1
@1
D=A
@endframe.Sys.init
A=M-D
D=M
@THAT
M=D

// goto return address
@ret.Sys.init41
A=M
D;JMP
