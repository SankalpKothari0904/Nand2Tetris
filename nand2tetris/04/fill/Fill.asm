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

@BorW
M=0     // variable black or white, 0 indicates white, -1 black
(LOOP1)
    @KBD
    D=M
    @black
    D;JNE
    @BorW
    M=0
    @FILL_SCREEN
    0;JMP
    (black)
        @BorW
        M=-1
    (FILL_SCREEN)
        @SCREEN
        D=A
        @address
        M=D
        (LOOP2)
            @address
            D=M
            @24576
            D=D-A
            @END2
            D;JGE
            @BorW
            D=M
            @address
            A=M
            M=D
            @address
            M=M+1
            @LOOP2
            0;JMP
(END2)
    @LOOP1
    0;JMP