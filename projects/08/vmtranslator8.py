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

        command_and_its_types = {"//": "", 'and': 'C_ARITHMETIC', 'gt': 'C_ARITHMETIC', 'sub': 'C_ARITHMETIC',
                                 'neg': 'C_ARITHMETIC',
                                 'lt': 'C_ARITHMETIC', 'add': 'C_ARITHMETIC', 'not': 'C_ARITHMETIC',
                                 'eq': 'C_ARITHMETIC',
                                 'or': 'C_ARITHMETIC', 'push': 'C_PUSH', 'pop': 'C_POP', 'if-goto': 'C_IF',
                                 'label': 'C_LABEL', 'goto': "C_GOTO"}
        split_command = command.split()
        command_type = split_command[0]
        has_comments = False
        if "//" in command:
            has_comments = True
        # if command_type in arithmetic_commands:
        #     return "C_ARITHMETIC", has_comments
        # elif command_type == "push":
        #     return "C_PUSH", has_comments
        # elif command_type == "pop":
        #     return "C_POP", has_comments

        return command_and_its_types[command_type], has_comments

    def remove_comments(self, command):
        """Remove comments from command received

        :param command: the command whose comments have to be removed
        :return: command with comments removed
        """
        split_command = command.split("//")
        # print split_command,command, "---------"
        if not len(split_command):
            return ''
        else:
            print split_command[0]
            return split_command[0].strip()

    def parse_asm(self):
        """Parse the .vm file

        Write the commands and type of that command and then pass those to code writer
        if the len of instruction is zero it means this is am empty line
        else compute the type of command and if it has comments remove them

        :return: output and command type lists
        """

        with open(self.vm_file_path, 'r') as vmf:
            instructions = vmf.read().splitlines()
        for instruction in instructions:
            if len(instruction) != 0:
                # print self.command_type(instruction)
                c_type, has_comments = self.command_type(instruction)
                if len(c_type) != 0:
                    if has_comments:
                        instruction = self.remove_comments(instruction)

                    self.output.append(instruction)
                    self.command_type_list.append(c_type)
        return self.output, self.command_type_list


class Code_Writer(object):
    """

    """

    def __init__(self, vm_file_path, parsed_file, command_types):
        self.vm_file_path = vm_file_path
        self.parsed_file = parsed_file
        self.command_types = command_types

    # def write_to_file(self,assembly_code):
    #     """Write the assembly code supplied to the corresponding asm file
    #
    #     :param assembly_code: the code that is to be written
    #     :return: write to the file
    #     """
    #     with open(self.fm_file_path,'a') as write_file:
    #         write_file.write(assembly_code)

    def write_arithmetic(self, command, ctr):
        """Perform arithmetic_files_asm operations on the last 2 elements in the stack

        FOR ARITHMETIC BASED :

        Perform arithmetic_files_asm operations on the last 2 elements in the stack, save the result
        in 2 positions before the current pointer location. Arithmetic operations are:
        add, sub, And, Or

        example (initially) :
            sp(stack pointer) -> 259
            memory address ->                   257, 258, 259
            memory address values (stack) ->     12,  13,  sp

        operations for add :
            1. sp--        258
            2. d = *sp     13
            3. sp--        257
            4. *sp += d    25      ++
            5. sp++        258
        operations for sub
            1. same as add operation 1
            2. same as add operation 2
            3. same as add operation 3
            4. *sp -= d    25      --
            5. same as add operation 5
        operations for And
           1. same as add operation 1
            2. same as add operation 2
            3. same as add operation 3
            *sp && d    25      &&
           5. same as add operation 5
        operations for Or
            1. same as add operation 1
            2. same as add operation 2
            3. same as add operation 3
            *sp || d    25      ||
            5. same as add operation 5

        NOTE: Above operations are not the best and compact implementation possible ,
             I made some changes to the actual algorithm to do basically the same ops
             above but in an efficient way

        So the above operations can be written in assembly as follows for add, sub,||,&&,~:
            // d = *(*sp-1)
                @SP
                A=M-1
                D=M

            // sp--
                @SP
                M=M-1

            // *(*sp-1) = *(*sp-1) + D  ->  this is an example for add but we can replace with other operations
                @SP
                A=M-1
                M=M+D


        FOR NEG :

        Goto last element in the stack, negate its value, move the counter to next position where
        the item was modified. Following is the pseudo implementation.
         *(*sp-1)= neq *(*sp-1)    -13
            // d = *(*sp-1)
                @SP
                A=M-1
                M=-M


        FOR COMPARISION BASED :

        Perform comparision operations on the last 2 elements in the stack, save the result
        in 2 positions before the current pointer location. Comparision operations are:
        eq, lt, gt

        example (initially) :
            sp(stack pointer) -> 259
            memory address ->                   257, 258, 259
            memory address values (stack) ->     12,  13,  sp

        Operations for the operations :

             # LT
                1. d = *(*sp-1)              13
                2. sp--                      258
                3. *sp = D-*(*sp-1)          -1  (goto 257, sub value in 258)
                4. if lt goto TRUE           if the value in step 3 is -ve (i.e 257<258)
                    1. *(*sp-1) =1           1 (set value at 257 to 1 (i.e True 257<258)
                    2. Skip the False  loop
                5. else FALSE                else
                    1. *(*sp-1) =1           0 (set value at 257 to 1 (i.e False 257>258)

             # GT
                1. Same as in LT             13
                2. Same as in LT             258
                3. Same as in LT             -1 (goto 257, sub value in 258)
                4. If gt goto TRUE           if the value in step 3 is +ve (i.e 257>258)
                    1. *(*sp-1) =1           1 (set value at 257 to 1 (i.e True 257<258)
                    2. Same as in LT
                5. else False
                    1. *(*sp-1) =1           0 (set value at 257 to 1 (i.e False 257<258)


             #EQ
                1. Same as in LT             13
                2. Same as in LT             258
                3. Same as in LT             -1  (goto 257, sub value in 258)
                4. If gt goto TRUE           if the value in step 3 is 0 (i.e 257==258)
                    1. *(*sp-1) =1           1 (set value at 257 to 1 (i.e True 257==258)
                    2. Same as in LT
                5. else False
                    1. *(*sp-1) =1           0 (set value at 257 to 1 (i.e False 257!=258)



        Following the psuedo assembly code for lt command can be replaced accordingly for others :
                    // d = *(*sp-1)
                        @SP
                        A=M-1
                        D=M
                    //sp--
                        @SP
                        M=M-1
                    // *sp = D-*(*sp-1)  // comparison for lt
                        @SP
                        A=M-1
                        D=M-D
                    // if lt goto TRUE
                        @TRUE
                        D;JLT
                    //else FALSE
                        @FALSE
                        D;JGE

                    (TRUE)
                    // *(*sp-1) =1
                        @SP
                        A=M-1
                        M=1

                    // Skip the False  loop
                        @OUT
                        0;JMP

                    (FALSE)
                    // *(*sp-1) =1

                        @SP
                        A=M-1
                        M=0

                    (OUT)
        :param command_type: The type of arithmetic_files_asm command
        :return: Write the corresponding command in the output file
        """

        d = {}
        for dirpath, dirnames, files in os.walk("arithmetic_files_asm"):
            for file_name in files:
                with open("./arithmetic_files_asm/" + file_name, 'r') as ff:
                    file_name = file_name.split('.')[0]
                    file_ = ff.read().splitlines()
                    d[file_name] = file_
        command_list = d[command]
        command_list = self.replace_with_i(command_list, 0, ctr)
        return command_list

    def replace_with_i(self, command_list, i, ctr):
        for item in range(len(command_list)):
            if "%s" in command_list[item]:
                command_list[item] = command_list[item].replace("%s", i)
            if "%t" in command_list[item]:
                command_list[item] = command_list[item].replace("%t", str(ctr))
        return command_list

    def label(self, label_name):
        """

        :param label_name:
        :return:
        """
        commands_list = ["// Label\n", "(%s)" % label_name.split()[-1]]
        return commands_list

    def goto_label(self, label_name):
        """

        :param label_name:
        :return:
        """
        command_list = ['// Label\n', '@%s' % label_name.split()[-1], 'D;JMP']
        return command_list

    def if_goto_label_name(self, label_name):
        """Implement the if-goto command

        If top stack value is 0  then continue
        else jump to required destination
        # Check value at sp--

        @SP
        A=M-1
        D=M
        # if not 0 jump to the mentioned location else continue
        @label_name
        D;JNE

        :param label_name:
        :return:
        """
        command_list = ['// if-goto Label Name\n', '@SP', 'M=M-1', '@SP', 'A=M', 'D=M', '@%s' % label_name.split()[-1],
                        'D;JNE', ]
        return command_list

    def write_push_pop(self, command, ctr):
        command = command.split()
        commandtype = ''.join(command[:2])
        i = command[-1]
        # print commandtype, i
        d = {}
        for dirpath, dirnames, files in os.walk("pushpop_files_asm"):
            for file_name in files:
                with open("./pushpop_files_asm/" + file_name, 'r') as ff:
                    file_name = file_name.split('.')[0]
                    file_ = ff.read().splitlines()
                    d[file_name] = file_
                ff.close()
        command_list = d[commandtype]
        command_list = self.replace_with_i(command_list, i, ctr)
        return command_list

    def open_file_and_write(self):
        file_path = self.vm_file_path.split('/')
        create_here = '/'.join(file_path[:-1])
        with_name = file_path[-1].split('.')[0] + '.asm'

        asm_file_location = create_here + "/" + with_name
        asm_file = open(asm_file_location, 'w')
        for ctr in xrange(len(self.parsed_file)):
            command = self.parsed_file[ctr]
            command_type = self.command_types[ctr]
            print command_type, command
            if command_type == "C_ARITHMETIC":
                command_list = self.write_arithmetic(command, ctr)
            elif command_type == "C_PUSH" or command_type == "C_POP":
                command_list = self.write_push_pop(command, ctr)
            elif command_type == "C_IF":
                command_list = self.if_goto_label_name(command)
            elif command_type == "C_LABEL":
                # print command
                command_list = self.label(command)
            elif command_type == "C_GOTO":
                command_list = self.goto_label(command)
            for assembly_command in command_list:
                asm_file.write(assembly_command + "\n")
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
        # print file_or_dir
        with open(file_or_dir, 'r') as vm_file_code:
            file_path = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + "/" + file_or_dir
            parser = Parser(vm_file_code, file_path)
            parsed_file, command_type_list = parser.parse_asm()
            code_writer = Code_Writer(file_path, parsed_file, command_type_list)
            code_writer.open_file_and_write()

        vm_file_code.close()

    # If the argv is a dir
    elif os.path.isdir(file_or_dir):
        for dirpath, dirnames, files in os.walk(file_or_dir):
            for file_name in files:
                if file_name.endswith('.vm'):
                    file_path = (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))) + "/" + \
                                dirpath + "/" + file_name
                    with open(file_path, 'r') as vm_file_code:
                        parser = Parser(vm_file_code, file_path)
                        parsed_file, command_type_list = parser.parse_asm()
                        code_writer = Code_Writer(file_path, parsed_file, command_type_list)
                        code_writer.open_file_and_write()

                    vm_file_code.close()

    else:
        print "Pass a valid file or dir"

    # for file in  os.walk(file_or_dir):
    #     print file


if __name__ == "__main__":
    main()
