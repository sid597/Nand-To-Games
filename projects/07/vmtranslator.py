"""Write a VM-to-Hack translator confirming to standard VM-on-Hack Mapping.

A .vm file will be passed and I have to translate the file to .asm with all the translated
code init.
Following are the commands which need to converted from vm to hack :
1. Arithmetic commands : add, sub, neg, eq, gt, lt, and, or, not
2. Memory segment commands : push segment i, pop segment i
    where segment is a memory segment which can be : static, local, argument, constant, this, that,
                                                     pointer, temp

Use of RAM memory registers:
Register  Name  Usage
0       SP
1       LCL
2       ARG
3       THIS
4       THAT
5-12    Temp
13-15   General registers
16-255  Static
256-2047 Stack

The process of translating will be carried out with the following Classes:
Main : Construct a "parser" to parse the vm input file and a "code_writer" to generate code into the
       corresponding output file. Also if the program's argument is a directory instead of a file
       this will process all the .vm files in that directory.
Parser : Handles the parsing of a single .vm file, and encapsulates access to the input
         code. It reads VM commands, parses them, and provides convenient access to their
         components. In addition, it removes all white space and comments.
Code Writer: Translates VM commands into Hack assembly code.


"""

import sys
import os, inspect


class Parser(object):
    """

    """
    def __init__(self, vm_file, vm_file_path):
        self.vm_file = vm_file
        self.vm_file_path = vm_file_path
        self.output = []
        self.command_type_list = []


    def command_type(self, command):
        """Return the command type of command

        :param command: Command that is being evaluated
        :return: type of command
        """

        arithmetic_commands = {'and', 'gt', 'sub', 'neg', 'lt', 'add', 'not', 'eq', 'or'}
        split_command = command.split()
        command_type = split_command[0]
        has_comments = False

        if "//" in command_type:
            has_comments = True
        if command_type in arithmetic_commands:
            return "C_ARITHMETIC", has_comments
        elif command_type == "push" :
            return "C_PUSH", has_comments
        elif command_type == "pop":
            return "C_POP", has_comments
        else:
            return '',has_comments

    def remove_comments(self, command):
        """Remove comments from command received

        :param command: the command whose comments have to be removed
        :return: command with comments removed
        """
        split_command = command.split("//")
        print split_command,"---------"
        if not len(split_command):
            return ''
        else:
            return split_command[0].strip()


    def parse_asm(self):
        """Parse the .vm file

        Write the commands and type of that command and then pass those to code writer
        if the len of instruction is zero it means this is am empty line
        else compute the type of command and if it has comments remove them

        :return:
        """

        with open(self.vm_file_path, 'r') as vmf:
            instructions = vmf.read().splitlines()
        for instruction in instructions:
            if len(instruction) != 0:
                c_type, has_comments = self.command_type(instruction)
                if len(c_type) != 0:
                    if has_comments :
                        c_type = self.remove_comments(c_type)

                    self.output.append(instruction)
                    self.command_type_list.append(c_type)
        return self.output, self.command_type_list


class Code_Writer(object):
    """

    """

    def __init__(self,fm_file_path, parsed_file,command_types):
        self.fm_file_path = fm_file_path
        self.parsed_file = parsed_file
        self.command_types = command_types

    def add(self,where):
        """
        example (initially) :
            sp -> 259
                    257, 258, 259
            stack -> 12,  13,  sp
            add
        operations for add :
            sp--        258
            d = *sp     13
            sp--        257
            *sp += d    25      ++
            sp++        258
        operations for sub
            sp--        258
            d = *sp     13
            sp--        257
            *sp -= d    25      --
            sp++        258
        operations for eq
            sp--        258
            d = *sp     13
            sp--        257
            *sp == d    25      eq
            sp++        258
        operations for gt
            sp--        258
            d = *sp     13
            sp--        257
            *sp > d     25      GT
            sp++        258
        operations for lt
            sp--        258
            d = *sp     13
            sp--        257
            *sp < d     25      LT
            sp++        258
        operations for And
            sp--        258
            d = *sp     13
            sp--        257
            *sp && d    25      &&
            sp++        258
        operations for Or
            sp--        258
            d = *sp     13
            sp--        257
            *sp || d    25      ||
            sp++        258
        operations for Not
            sp--        258
            d = *sp     13
            sp--        257
            *sp ~ d     25       Not
            sp++        258


        So the above operations can be written in assembly as follows for add, sub,||,&&,~:
            //sp--
                @sp
                M=M-1

            // d = *sp
                @sp
                A=M
                D=M

            //sp--
                @sp
                M=M-1

            //*sp += D  //*sp -= D
                @sp          @sp
                A=M          A=M
                M=M+D        M=M-D

            //sp++
                @sp
                M=M+1

        For gt,eq,lt we need to use jump :

            //sp--
                @sp
                M=M-1
            // d = *sp
                @sp
                A=M
                D=M
            //sp--
                @sp
                M=M-1
            // *sp = D-*sp  // comparison for lt
                @sp
                A=M
                D=D-M
            // if lt goto LT
                @TRUE
                D;JLT
            //else NLT
                @FALSE
                D;JGE

            (TRUE)
            // *sp =1
                @sp
                A=M
                M=1
            //sp++
                @sp
                M=M+1
            // jmp the following loop
                @OUT
                0;JMP

            (FALSE)
            // *sp =1

                @sp
                A=M
                M=0
            //sp++
                @sp
                M=M+1
            (OUT)




        operations for neq  -> This one is different from all the others
            sp--        258
            d = *sp     13
            *sp = -d    -13
            sp++        259

        :param where:
        :return:
        """

    def neg(self, where):

    def write_aritmatic(self,command):

        return ''

    def local(self, where):
    def argument(self, where):
    def pointer(self, where):
    def temp(self, where):
    def static(self, where):
    def constant(self, where):
    def this(self, where):
    def that(self, where):




    def write_push(self,command):
        return ''

    def write_pop(self,command):

    def open_file_and_write(self):
        file_path = self.vm_file_path.split('/')
        create_here = '/'.join(file_path[:-1])
        with_name = file_path[-1].split('.')[0] + '.asm'

        asm_file_location = create_here + "/" + with_name
        asm_file = open(asm_file_location, 'w')
        for ctr in xrange(len(self.parsed_file)):
            command = self.parsed_file[ctr]
            command_type = self.command_types
            if command_type == "C_ARITHMETIC":
                self.write_aritmatic(command)
            elif command_type == "C_PUSH":
                self.write_push(command)
            elif command_type == "C_POP":
                self.write_pop(command)


        asm_file.close()



def main():
    """Process .vm file and pass it to parser

    Construct a "parser" to parse the vm input file and a "code_writer" to generate code into the
    corresponding output file. Also if the program's argument is a directory instead of a file this
    will process all the .vm files in that directory.

    python I/O :https://realpython.com/working-with-files-in-python/,
                https://dbader.org/blog/python-file-io
    :return: Writes to another file the corresponding assembly code for the passed file
    """
    file_or_dir = sys.argv[-1]
    # print file_or_dir
    # If the argv is file
    if os.path.isfile(file_or_dir):
        print file_or_dir
        with open(file_or_dir, 'r') as vm_file_code:
            file_path = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + "/" + file_or_dir
            p = Parser(vm_file_code, file_path)
            parsed_file, command_typ = p.parse_asm()
            asm_file_loc = p.create_asm_file()

        vm_file_code.close()

    # If the argv is a dir
    elif os.path.isdir(file_or_dir):
        for dirpath, dirnames, files in os.walk(file_or_dir):
            for file_name in files:
                if file_name.endswith('.vm'):
                    file_path = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + "/" + \
                                dirpath + "/" + file_name
                    with open(file_path, 'r') as vm_file_code:
                        p = Parser(vm_file_code, file_path)
                        parsed_file, command_typ = p.parse_asm()

                    vm_file_code.close()

    else:
        print "Pass a valid file or dir"

    # for file in  os.walk(file_or_dir):
    #     print file


if __name__ == "__main__":
    main()

