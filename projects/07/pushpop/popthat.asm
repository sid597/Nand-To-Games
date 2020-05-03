//POP THAT

//R13=*(*THAT+i)
//SP--
//*R13=*SP


@%s
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
