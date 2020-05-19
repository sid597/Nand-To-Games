# Overview of the project 

The computer system described is for real—it can actually be built, and
it works! The multi-tier collection of abstractions underlying the design of a computing system can be described top-down, showing how high-level abstractions can be reduced
into, or expressed by, simpler ones. This structure can also be described bottom-up,
focusing on how lower-level abstractions can be used to construct more complex
ones. This book takes the latter approach: We begin with the most basic elements—
3 Introduction
primitive logic gates—and work our way upward, culminating in the construction
of a general-purpose computer system. And if building such a computer is like
climbing Mount Everest, then planting a flag on the mountaintop is like having the
computer run a program written in some high-level language. Since we are going
to ascend this mountain from the ground up, let us survey the book plan in the opposite direction—from the top down—starting in the familiar territory of high-level
programming.
Our tour consists of three main legs. We start at the top, where people write
and run high-level programs (chapters 9 and 12). We then survey the road down to
hardware land, tracking the fascinating twists and curves of translating high-level
programs into machine language (chapters 6, 7, 8, 10, 11). Finally, we reach the low
grounds of our journey, describing how a typical hardware platform is actually constructed (chapters 1–5).



NOTE : All the chips were developed using the HDL provided in the website 

## Project 1

Implementation of logic gates using NAND gate only. Build following gates as part of this project:

1 bit : Not, And, Or, Xor, Multiplexor, Demultiplexor, Multi-bit Multiplexor

16 bit : Not, And, Or, Xor

Out of the above chips I found Mux and DMux chips to be somewhat tricky to implement. 

## Project 2

In this project I build gate logic designs that represent numbers and perform
arithmetic operations on them. Signed binary numbers are represented using 2's complement.
Following chips are to be implemented in this project :
1. Half-adder : Chip to add 2 bits, outputs sum and the carry bit.
2. Full-adder : Chip to add 3 bits, outputs sum and carry bit.
3. Adder      : A 16 bit adder, it is fairly easy to implement this once one has full-adder
4. Incrementer: 16-bit incrementer, this is an important chip although the functionality is very simple. It is 
                is used as an counter/incrementer
4. ALU        : The Main chip which is used to carry out the arithmetic operations. 



NOTE : In this course the design decision was made to not build a multiplier in hardware, it is to be complemented 
       by software.
       
       
## Project 3

This project was all about implementing RAM. We take D flip-flop and from that build a chip to contain 1 bit, 
then from this bit chip register chip is implemented and from these registers RAM is build (8bit, 64bit, 512, 4k, 16k).
These Registers and Ram can save 16 bit words. 

It was a very good exercise to thing about how to build RAM given its specification

NOTE: I read more about memory in real world systems and it turns out there is a hierarchy of memory which is used by cpu
      Like: registers, L1-L3 caches, DRam, storage memory. And the term RAM commonly refers to DRAM which is implemented 
      using capacitors and transistors. But in this courses implementation we are not making memory hierarchy and 
      assume there is one memory to which cpu reads and writes to.
      
      
## Project 4
A computer can be described constructively, by laying out its hardware platform
and explaining how it is built from low-level chips. A computer can also be described
abstractly, by specifying and demonstrating its machine language capabilities. So in this project we focused on low level
programming in machine language. A low level machine language called HACK machine language was designed by course makers
and that language is to be understood and used to write 2 programs (multiplication, and I/O related program).
We use 2 type of instructions to perform operations on our computer called A-instruction and C-instruction
which are both 16-bit words 






This project was very fascinating to me, it is where hardware meets software. How abstract thoughts manifested in symbolic 
instructions are converted to 1's and 0's physical opertations.

## Project 5

This was the last project in terms on hardware building. And in this project I had to build a general purpose Hack computer platform
Using all the previously made chips. The contract is that this s project should be capable of executing
programs written in the Hack machine language, specified in project 4. This is machine which supports to run any program
Following things had to done in this project:

1. Build CPU chip
2. Use RAM, CPU and ROM to build the full CPU  

This project was tough, challenging, fun and fascinating, it took me quite some time to build it but boy it was worth it.

## Project 6
Develop an assembler that translates programs written in Hack assembly
language into the binary code understood by the Hack hardware platform.

To translate from one language to another we must know about both the languages syntax. In project 4 we tackled this issue
and there I learned about both assembly language and machine language. So now in this project I needed to implement the 
parsing logic. 

    Assembly program elements:

    • White space
         Empty lines / indentation
         Line comments
         In-line comments
    • Instructions
         A-instructions
         C-instructions
    • Symbols
         References
         Label declarations

So I need to take care of all these elements and convert the legible code to machine instructions


- For Whitespace and comments : We just ignore them and move forware
- For Instructions : We convert them as per the contract of both languages
- For Symbols : Now this is fun, symbols are used by us to represent different places in code. But there is no such
                thing as symbols and variables in machine, there its all about the memory locations. So basically we somehow
                now have to convert these symbols to memory addresses. Also note that we cannot assign any variables to first 
                16 places in the memory because those are reserved for special symbols. So we map the variables to memory
                starting from 16th memory location.

This was the first software side of piece we need to build the full fledged computer and it was very profound to build this 
assembler. It is quite fascinating thinking about how much we can do which such primitive language.

## Project 7
Convert VM code to assembly code

This project is the first steps toward building a compiler for a typical objectbased high-level language. We will approach this substantial task in two stages, each
spanning two projects. High-level programs will first be translated into an intermediate code (projects 10–11), and the intermediate code will then be translated into
machine language (projects 7–8). This two-tier translation model is a rather old idea
that goes back to the 1970s. Recently, it made a significant comeback following its
adoption by modern languages like Java and C#.

The basic idea is as follows: Instead of running on a real platform, the intermediate code is designed to run on a Virtual Machine. The VM is an abstract computer
that does not exist for real, but can rather be realized on other computer platforms.

Also we use stack machines to implement this idea of VM which in itself is a very elegant idea where we explore how to implement the branching and functions on a 
humble stack. In this VM implementation we have the following type of commands :

- Arithmetic / logical commands
- Memory segment commands
- Branching commands
- Function commands


In this project we deal with the implementation of 

1. Arithmetic/Logical commands 

        add, sub, neg, eq, get, lt, and, or, not,

2. Memory segment commands

        - pop segment i
        
            - Where segment is: argument, local, static, constant,this, that, pointer, or temp
        - push segment i
        
           -  Where segment is: argument, local, static,this, that, pointer, or temp
        
These segments are pointer to different memory locations which we can use as a specific type of addresses
for different memory purposes.


## Project 8

Continuing from project 7 in this project we deal with the implementation of :

VM branching commands:

    • goto label
    • if-goto label
    • label label

VM function commands:

    • call function
    • function function
    • return
    
    
Oh man this was a  mind blowing project how branching, recursion, classes and functions can be implemted on stack machine ingenious ideas. 

## Project 9

This was a project about the high level language Jack for which we are developing the compiler and the language in
which we are going to write out OS 

## Project 10-11

Build a syntax analyzer that parses Jack programs according to the Jack
grammar. The analyzer’s output should be written in XML, as defined in the specification section

In this project I had to build a tokeniser and a parser to create a parese tree from the tokens.
This is an intermediate project before developing the full fledged compiler. 

These projects combined were challanging to implement, but these were very knowledgeable and I was very surprised and awe struck how elegantly 
the compiler is designed to work. One of the biggest idea to me was symbol tables how variables are never compiled but only looked up at reference time and have no other use

The challanges which had to be implemented were :

    • Handling variables   : Using symbol tables
    • Handling expressions : This was the mosr challanging for me to implement among the other challing
    • Handling flow of control
    • Handling objects
        • Construction
            • Compiling “new”
            • Compiling constructors
        • Manipulation
            • Compiling method calls (caller side)
            • Compiling methods (callee side)
    • Handling arrays        
        • Array construction
        • Array manipulation
        
        
## Project 12 
Implement the OS described in the last unit. In this project a very minimal services are implemented consisting of the following:

The operating system is divided into eight classes:

    - Math: provides basic mathematical operations
            abs, multiply, divide, min, max, sqrt
    - String: implements the String type and string-related operations
            - constructor String new(int maxLength): constructs a new empty string (of length
            zero) that can contain at most maxLength characters;
            - method void dispose( ): disposes this string;
            - method int length( ): returns the length of this string;
            - method char charAt(int j): returns the character at location j of this string;
            - method void setCharAt(int j, char c): sets the j-th element of this string to c;
            - method String appendChar(char c): appends c to this string and returns this
              string;
              method void eraseLastChar( ): erases the last character from this string;
            - method int intValue( ): returns the integer value of this string (or the string prefix until a non-digit character is detected);
            - method void setInt(int j): sets this string to hold a representation of j;
            - function char backSpace( ): returns the backspace character;
            - function char doubleQuote( ): returns the double quote (‘‘) character;
            - function char newLine( ): returns the newline character.
            
    - Array: implements the Array type and array-related operations
             - function Array new(int size): constructs a new array of the given size;
             - method void dispose( ): disposes this array
             
    - Output: handles text output to the screen
     function void init( ): for internal use only;
            - function void moveCursor(int i, int j): moves the cursor to the j-th column of the
              i-th row, and erases the character displayed there;
            - function void printChar(char c): prints c at the cursor location and advances the
              cursor one column forward;
            - function void printString(String s): prints s starting at the cursor location and
              advances the cursor appropriately;
            - function void printInt(int i): prints i starting at the cursor location and advances the cursor appropriately;
            - function void println( ): advances the cursor to the beginning of the next line;
            - function void backSpace( ): moves the cursor one column back.
    - Screen: handles graphic output to the screen
            - function void init( ): for internal use only;
            - function void clearScreen( ): erases the entire screen;
            - function void setColor(boolean b): sets a color (white ¼ false, black ¼ true) to
              be used for all further drawXXX commands;
            - function void drawPixel(int x, int y): draws the (x,y) pixel;
            - function void drawLine(int x1, int y1, int x2, int y2): draws a line from pixel
              (x1,y1) to pixel (x2,y2);
            - function void drawRectangle(int x1, int y1, int x2, int y2): draws a filled rectangle whose top left corner is (x1,y1) and whose bottom right corner is (x2,y2);
            - function void drawCircle(int x, int y, int r): draws a filled circle of radius
              r <¼ 181 around (x,y).
    - Keyboard: handles user input from the keyboard
            - function void init( ): for internal use only;
            - function char keyPressed( ): returns the character of the currently pressed key
                on the keyboard; if no key is currently pressed, returns 0;
                m function char readChar( ): waits until a key is pressed on the keyboard and released, then echoes the key to the screen and returns the character of the pressed key;
            - function String readLine(String message): prints the message on the screen, reads
                the line (text until a newline character is detected) from the keyboard, echoes the line
                to the screen, and returns its value. This function also handles user backspaces;
            - function int readInt(String message): prints the message on the screen, reads the
                line (text until a newline character is detected) from the keyboard, echoes the line to
                the screen, and returns its integer value (until the first non-digit character in the line
                is detected). This function also handles user backspaces.
    
    - Memory: handles memory operations
            - function void init( ): for internal use only;
            - function int peek(int address): returns the value of the main memory at this
                address;
                266 Chapter 12
            - function void poke(int address, int value): sets the contents of the main memory
                at this address to value;
            - function Array alloc(int size): finds and allocates from the heap a memory block
                of the specified size and returns a reference to its base address;
            - function void deAlloc(Array o): De-allocates the given object and frees its
                memory space.
    
    - Sys: provides some execution-related services
        - function void init( ): calls the init functions of the other OS classes and then
            calls the Main.main() function. For internal use only;
        - function void halt( ): halts the program execution;
        - function void error(int errorCode): prints the error code on the screen and halts;
        - function void wait(int duration): waits approximately duration milliseconds and
            returns.

The OS services that is used comprise an operating system in a very minimal
fashion, aiming at 

1. encapsulating various hardware-specific services in a software friendly way, and
 
2. extending high-level languages with various functions and abstract data types