// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

 
    (LP)

    @KBD
    D=M

    @PRESSED
    D;JGT

    @NP
    D;JEQ

    @LP
    0;JMP

    (PRESSED)  // If key is pressed 

    // Let arr = Screen
    @SCREEN
    D=A
    @arr
    M=D

    // Let n = 8192
    @8192
    D=A
    @n
    M=D

    // Let i = 0
    @i
    M=0
    (LOOP)

    // if (i==n) goto Main loop
    @i
    D=M
    @n
    D=D-M

    @LP
    D;JEQ

    // RAM[arr+i] = -1
    @arr
    D=M
    @i
    A=D+M   // THIS IS IMPORTANT POINTER MANIPULATION 
    M=-1

    // i++
    @i
    M=M+1
    
    @LOOP
    0;JMP

    (NP)  // If not pressed

    // Let arr = Screen
    @SCREEN
    D=A
    @arr
    M=D

    // Let n = 8192
    @8192
    D=A
    @n
    M=D

    // Let i = 0
    @i
    M=0
    (LOOP1)

    // if (i==n) goto END
    @i
    D=M
    @n
    D=D-M

    @LP
    D;JEQ

    // RAM[arr+i] = -1
    @arr
    D=M
    @i
    A=D+M
    M=0

    // i++
    @i
    M=M+1
    
    @LOOP1
    0;JMP

    @LP
    0;JMP