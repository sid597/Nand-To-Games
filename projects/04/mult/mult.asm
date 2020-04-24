// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
 
    @R0    // set a to r0
    D=M
    @a
    M=D

    @R1    // set b to r1
    D=M
    @b
    M=D

    @sum   // set sum to 0
    M=0   

    (LOOP)

    @a     // get value of a
    D=M

    @STOP  // If d less than 0 stop
    D;JEQ

    @b     // Get value of b to add to sum
    D=M

    @sum
    M=M+D

    @a     // Subtract 1 from a
    M=M-1

    @LOOP
    0;JMP


    (STOP)
    @sum
    D=M
    @R2
    M=D

    (END)
    @END
    0;JMP
 


