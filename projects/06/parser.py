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


class Parser(object):
    """Break each assembly command into its underlying components ( fields and symbols).
     In addition removes whitespaces and comments.

    Attributes:
        instructions: List to contain all the commands assembly commands
        current_command: Current command which is being executed
    """

    def __init__(self):
        self.instructions = []
        self.current_command = ""

    def remove_whitespace_comments(self, parse_file):
        """Removes whitespaces and comments from the file

        :param parse_file: The file which needs to be parsed
        :return: A list containing instructions without any comment and whitespace
        """
        for line in parse_file:
            if len(line) != 0:
                comment_start = line.find('//')
                if comment_start != -1:
                    line = line[:comment_start]

                if len(line) != 0:
                    line = ''.join(line.strip(' '))
                    self.instructions.append(line)
        return self.instructions

    def command_type(self):
        """
        :return: Type of Command
        """
        first_letter = self.current_command[0]
        if first_letter == '@':
            return "A_Command"
        elif first_letter == '(':
            return "L_Command"
        return "C_Command"

    def symbol(self):
        """ Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx).
         Should be called only when commandType() is A_COMMAND or L_COMMAND.

        :return: Symbol
        """
        first_letter = self.current_command[0]
        if first_letter == '@':
            return self.current_command[1:]
        return self.current_command[1:len(self.current_command) - 1]

    def comp(self):
        """Returns the comp mnemonic in the current C-command (28 possibilities).
         Should be called only when commandType() is C_COMMAND.

        C-command structure :   "X=Xxx;yyy"  X-> comp,  Xxx -> dest, yyy -> jump
        :return: Destination mnemonic in C-command
        """

        if "=" in self.current_command:
            return self.current_command.split('=')[0]
        return None

    def dest(self):
        """ Returns the dest mnemonic in the current C-command (8 possibilities).
        Should be called only when commandType() is C_COMMAND.

         C-command structure :   "X=Xxx;yyy"  X-> comp,  Xxx -> dest, yyy -> jump
         The way I figure out the comp command is to split the command with
         '=' sign take the last element in list this will remove dest part then split with
         ";" sign take the last element in list this will remove the jump mnemonic if present

        :return: Computation mnemonic in c-command
        """

        dest = self.current_command.split("=")[1]
        dest = dest.split(";")[0]
        return dest
    def jump(self):
        """Returns the jump mnemonic in the current C-command (8 possibilities).
         Should be called only when commandType() is C_COMMAND.

        :return: jump mnemonic in c-command
        """

        if ";" in self.current_command:
            return self.current_command.split(';')[1]
        return None


def main():
    """Convert the assembly code to binary code for the file provided.

    :return: Nothing
    """
    # try:
    file_name = sys.argv[1]
    with open(file_name) as assembly_code:
        instruction_file = assembly_code.read().splitlines()
    parse_this_file = Parser()
    rem = parse_this_file.remove_whitespace_comments(instruction_file)
    print rem
    # print parsed_file.filename()


# except:
#     print "Error: Please provide a file to assembler"


if __name__ == '__main__':
    main()
