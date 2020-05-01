"""A parser for the Hack machine language for course nand2tetris.

This is a Hack parser it takes Hack assembly language code file (example.asm), converts
that to binary code then writes that binary code in other file (example.hack).
There are 4 main parts to this file :

Parser : The main function of parser is to break each assembly command into its underlying
    components ( fields and symbols). In addition removes whitespaces and comments.
Code : Translates Hack assembly language mnemonics into binary codes.
SymbolTable : Creates a table to maintain the correspondence between the symbols and their meaning
Main : The main functions which combines all the other classes/modules to perform the task.

"""

import sys


c_instructions = {"@R0":0,"@R1":1,
"@R2":2,
"@R3":3,
"@R4":4,
"@R5":5,
"@R6":6,
"@R7":7,
"@R8":8,
"@R9":9,
'@R10':10,
"@R11":11,
"@R12":12,
"@R13":13,
"@R14":14,
"@R15":15,"@SCREEN":16384,"@KBD":24576,"@SP":0,"@LCL":1,"@ARG":2,"@THIS":3,"@THAT":4,'dest': {'-D': '001111', '-A': '110011', '-M': '110011', 'M+1': '110111', 'D-A': '010011', 'M-1': '110010', 'D-M': '010011', '1': '111111', '0': '101010', 'D+A': '000010', 'A-1': '110010', 'D+M': '000010', 'A': '110000', 'D': '001100', 'D+1': '011111', 'A+1': '110111', 'M': '110000', 'A-D': '000111', 'D-1': '001110', 'D|A': '010101', 'M-D': '000111', 'D|M': '010101', '!A': '110001', '!D': '001101', '!M': '110001', 'D&M': '000000', '-1': '111010', 'D&A': '000000'}, 'jump': {'JLT': '100', 'JEQ': '010', 'JMP': '111', 'JGE': '011', 'JLE': '110', 'JNE': '101', 'null': '000', 'JGT': '001'}, 'comp': {'A': '100', 'MD': '011', 'D': '010', 'M': '001', 'AM': '101', 'AMD': '111', 'null': '000', 'AD': '110'}}



def add_dest():
    """
    0 0 0 null
    001 M
    010 D
    0 1 1 MD
    100 A
    1 0 1 AM
    1 1 0 AD
    1 1 1 AMD

    Usage: run this function
    then copy paste the above commands in terminal

    """
    c_instructions["comp"] = {}
    for i in range(8):
        inp = raw_input().split()
        ki = inp[-1]
        val = "".join(inp[:-1])
        c_instructions["comp"][ki] = val


def add_jump():
    """
    0 0 0 null
    0 0 1 JGT
    0 1 0 JEQ
    0 1 1 JGE
    1 0 0 JLT
    1 0 1 JNE
    1 1 0 JLE
    1 1 1 JMP

     Usage: run this function
    then copy paste the above commands in terminal
    """
    c_instructions["jump"] = {}
    for i in range(8):
        inp = raw_input().split()
        ki = inp[-1]
        val = "".join(inp[:-1])
        c_instructions["jump"][ki] = val

def add_comp_a_0():
    """

    0 101010
    1 111111
    -1 1 1 1 0 1 0
    D 001100
    !D 0 0 1 1 0 1
    -D 0 0 1 1 1 1
    D+1 0 1 1 1 1 1
    D-1 0 0 1 1 1 0
    A+1 1 1 0 1 1 1 M+1
    !A 1 1 0 0 0 1 !M
    -A 1 1 0 0 1 1 -M
    A 110000 M
    A-1 1 1 0 0 1 0 M-1
    D+A 0 0 0 0 1 0 D+M
    D-A 0 1 0 0 1 1 D-M
    A-D 0 0 0 1 1 1 M-D
    D&A 0 0 0 0 0 0 D&M
    D|A 0 1 0 1 0 1 D|M

    Usage : Pass the above input

    """

    for i in range(8):
        inp = raw_input().split()
        ki = inp[0]
        val = "".join(inp[1:])
        c_instructions["dest"][ki] = val

    for j in range(10):
        n = raw_input().split()
        m = n[0]
        n = ''.join(n[1:-1])
        c_instructions["dest"][m] = n
    return c_instructions

def add_comp_a_1():
    """

    A+1 1 1 0 1 1 1 M+1
    !A 1 1 0 0 0 1 !M
    -A 1 1 0 0 1 1 -M
    A 110000 M
    A-1 1 1 0 0 1 0 M-1
    D+A 0 0 0 0 1 0 D+M
    D-A 0 1 0 0 1 1 D-M
    A-D 0 0 0 1 1 1 M-D
    D&A 0 0 0 0 0 0 D&M
    D|A 0 1 0 1 0 1 D|M

    Usage : Pass the above input

    """
    c_instructions["dest"] = {}
    for j in range(10):
        n = raw_input().split()
        m = n[-1]
        n = ''.join(n[1:-1])

        c_instructions["dest"][m] = n
    return c_instructions


def c_instruction_symbol_table():
    """ First create the symbol table for C-instruction

    To do this copy paste the following in terminal:

    A+1 1 1 0 1 1 1 M+1
    !A 1 1 0 0 0 1 !M
    -A 1 1 0 0 1 1 -M
    A 110000 M
    A-1 1 1 0 0 1 0 M-1
    D+A 0 0 0 0 1 0 D+M
    D-A 0 1 0 0 1 1 D-M
    A-D 0 0 0 1 1 1 M-D
    D&A 0 0 0 0 0 0 D&M
    D|A 0 1 0 1 0 1 D|M
    0 101010
    1 111111
    -1 1 1 1 0 1 0
    D 001100
    !D 0 0 1 1 0 1
    -D 0 0 1 1 1 1
    D+1 0 1 1 1 1 1
    D-1 0 0 1 1 1 0
    A+1 1 1 0 1 1 1 M+1
    !A 1 1 0 0 0 1 !M
    -A 1 1 0 0 1 1 -M
    A 110000 M
    A-1 1 1 0 0 1 0 M-1
    D+A 0 0 0 0 1 0 D+M
    D-A 0 1 0 0 1 1 D-M
    A-D 0 0 0 1 1 1 M-D
    D&A 0 0 0 0 0 0 D&M
    D|A 0 1 0 1 0 1 D|M
    0 0 0 null
    0 0 1 JGT
    0 1 0 JEQ
    0 1 1 JGE
    1 0 0 JLT
    1 0 1 JNE
    1 1 0 JLE
    1 1 1 JMP
    0 0 0 null
    001 M
    010 D
    0 1 1 MD
    100 A
    1 0 1 AM
    1 1 0 AD
    1 1 1 AMD
    """

    add_comp_a_1()
    add_comp_a_0()
    add_jump()
    add_dest()
    return c_instructions

def remove_whitespace_comments(parse_file):
    """Removes whitespaces and comments from the file

    :param parse_file: The file which needs to be parsed
    :return: A list containing instructions without any comment and whitespace
    """
    instructions = []
    for line in parse_file:
        if len(line) != 0:
            comment_start = line.find('//')
            if comment_start != -1:
                line = line[:comment_start]
            if len(line) != 0:
                line = ''.join(line.strip(' '))
                instructions.append(line)
    return instructions


def command_type(current_command):
    """
    :return: Type of Command
    """
    first_letter = current_command[0]
    if first_letter == '@':
        return "A_Command"
    elif first_letter == '(':
        return "L_Command"
    return "C_Command"


def comp(current_command):
    """Returns the comp mnemonic in the current C-command (28 possibilities).
     Should be called only when commandType() is C_COMMAND.

    C-command structure :   "X=Xxx;yyy"  X-> comp,  Xxx -> dest, yyy -> jump
    :return: Destination mnemonic in C-command
    """

    if "=" in current_command:
        return  c_instructions["comp"][current_command.split('=')[0]]
    return "000"


def destination(current_command):
    """ Returns the dest mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND.

         C-command structure :   "X=Xxx;yyy"  X-> comp,  Xxx -> dest, yyy -> jump
         The way I figure out the comp command is to split the command with
         '=' sign take the last element in list this will remove dest part then split with
         ";" sign take the last element in list this will remove the jump mnemonic if present

        :return: Computation mnemonic in c-command
        """
    if "=" in current_command:
        dest = current_command.split("=")[1]
        dest = dest.split(";")[0]
    else:
        dest = current_command.split(";")[0]
    return c_instructions["dest"][dest]



def jump(current_command):
    """Returns the jump mnemonic in the current C-command (8 possibilities).
         Should be called only when commandType() is C_COMMAND.

        :return: jump mnemonic in c-command
        """

    if ";" in current_command:
        return c_instructions["jump"][current_command.split(';')[1]]
    return "000"


def convert_c_command_to_binary(command):
    cmp = comp(command)
    dst = destination(command)
    jmp = jump(command)

    if "=" in command:
        dest = command.split("=")[1]
        dest = dest.split(";")[0]
    else:
        dest = command.split(";")[0]

    m_or_not = "M" in dest
    if m_or_not:
        in_binary = "1111"
    else:
        in_binary = "1110"
    # print dst,cmp,jmp
    return in_binary  + dst + cmp + jmp

# print convert_c_command_to_binary("0;JMP")=="1110101010000111"

def convert_a_command_to_binary(command,symbol_table,var_tabl):

    # Check if the value provided is an int or var
    # print var_tabl,symbol_table
    if command in c_instructions:
        address = c_instructions[command]
        bin_address = bin(address)[2:]
        return "0" * (16 - len(bin_address)) + bin_address
    else:
        try:
            address = int(command[1:])
            bin_address = bin(address)[2:]
            return "0" * (16 - len(bin_address)) + bin_address
        except ValueError:
            sym_or_var = command[1:]
            if command[1:] in symbol_table:
                address = symbol_table[command[1:]]
                bin_address = bin(address)[2:]
                return "0" * (16 - len(bin_address)) + bin_address
            else:
                address = var_tabl[command[1:]]
                bin_address = bin(address)[2:]
                return "0" * (16 - len(bin_address)) + bin_address

# print convert_a_command_to_binary("R15",{})



def symbol_tbl(parsed):
    symbol_table = {}
    ctr = 0
    cs = set()
    s = set()
    for instruction in parsed:
        typ = command_type(instruction)
        if typ == "L_Command":
            l = instruction[1:-1]
            if l not in symbol_table:
                symbol_table[l] = ctr
                s.add(l)
                cs.add(ctr)
        else:   
            ctr+=1

    return symbol_table

def variable_tbl(parsed,symbol_tbl):
    ctr = 16
    var_table = {}
    for ins in parsed:
        if command_type(ins) == "A_Command":
            if ins not in c_instructions and ins[1].isalpha():
                if ins[1:] not in symbol_tbl and ins[1:] not in var_table:
                    # print ins,ctr
                    var_table[ins[1:]] = ctr
                    ctr+=1
    return var_table


# #
def main():
    """Convert the assembly code to binary code for the file provided.

    :return: Nothing
    """
    # try:

    file_name = sys.argv[1]
    with open(file_name) as assembly_code:
        instruction_file = assembly_code.read().splitlines()
    fn = file_name.split(".")[0]
    hack_file = open("/home/sid597/Nand-To-Games/projects/06/%s"%fn+".hack","w")


    parsed = remove_whitespace_comments(instruction_file)
    # print parsed
    symbol_table = symbol_tbl(parsed)
    var_tabl = variable_tbl(parsed,symbol_table)
    # print symbol_table
    # print var_tabl
    for i in symbol_table:
        if symbol_table[i] == 24577:
            print i
            break
    for j in var_tabl:
        if var_tabl[j] == 24577:
            print j
    for instruction in parsed:
        # print instruction
        Ctype = command_type(instruction)
        if Ctype == "C_Command":
            in_binar = convert_c_command_to_binary(instruction)
            # print instruction, in_binar
            hack_file.write(in_binar + "\n")
        elif Ctype == "A_Command":
            in_binar = convert_a_command_to_binary(instruction, symbol_table,var_tabl)
            # print instruction,in_binar
            hack_file.write(in_binar + "\n")
    hack_file.close()


if __name__ == '__main__':
    main()

