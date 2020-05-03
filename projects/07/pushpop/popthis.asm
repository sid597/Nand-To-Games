//R13=*(*THIS+i)
//SP--
//*R13=*SP


@%s
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
