// POP LOCAL
//R13=*(*LCL+i)
//SP--
//*R13=*SP


@%s
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
