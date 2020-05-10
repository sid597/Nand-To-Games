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




 TODO: Implement function to handle directory
                  From all classes in dictonary extract their functions and also put them in dictionary

                  d = {
                    "class_1":{
                        "function_1" : [],
                        "finction_2" : []
                    }
                    ...
                    ...
                  }

                  Convert function code

"""

import sys
import os, inspect


class Parser(object):
    """

    """

    def __init__(self, vm_file="", vm_file_path="", dir_path=""):
        self.vm_file = vm_file
        self.vm_file_path = vm_file_path
        self.output = []
        self.command_type_list = []
        self.dir_path = dir_path

    def command_type(self, command):
        """Return the command type of command

        :param command: Command that is being evaluated
        :return: type of command
        """

        command_and_its_types = {"//": "", 'and': 'C_ARITHMETIC', 'gt': 'C_ARITHMETIC', 'sub': 'C_ARITHMETIC',
                                 'neg': 'C_ARITHMETIC',
                                 'lt': 'C_ARITHMETIC', 'add': 'C_ARITHMETIC', 'not': 'C_ARITHMETIC',
                                 'eq': 'C_ARITHMETIC',
                                 'function': 'C_FUNCTION',
                                 'call': 'C_CALL',
                                 'return': 'C_RETURN',
                                 'or': 'C_ARITHMETIC', 'push': 'C_PUSH', 'pop': 'C_POP', 'if-goto': 'C_IF',
                                 'label': 'C_LABEL', 'goto': "C_GOTO"}
        split_command = command.split()
        command_typ = split_command[0]
        has_comments = False
        if "//" in command:
            has_comments = True
        return command_and_its_types[command_typ], has_comments

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
            # print split_command[0]
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

    def parse_directory(self):
        """
        This method does 3 things:
        1. Create a .asm file with the same name as the directory
        2. Create a dictionary with all the content in different vm files( i.e different classes) in the directory
        3. Remove comments from all the classes
        :return:
        """
        classes = {}
        # print os.getcwd() + "/" + self.dir_name
        # dire = os.getcwd() + "/" + self.dir_name +"/"+ self.dir_name
        # print '------'
        for dirpath, dirnames, files in os.walk(self.dir_path):

            print dirpath, files
            for file_name in files:
                if file_name.endswith('.vm'):
                    file_path = (dirpath + "/" + file_name)
                    print file_path
                    with open(file_path, 'r') as vm_file_code:
                        class_name = file_name.split('.')[0]
                        classes[class_name] = {}
                        classes[class_name]['asm_commands'] = []
                        classes[class_name]['command_type'] = []
                        for instruction in vm_file_code:
                            instruction = self.remove_comments(instruction)
                            if instruction:
                                classes[class_name]['asm_commands'].append(instruction)
                                command_typ = self.command_type(instruction)[0]
                                classes[class_name]['command_type'].append(command_typ)
                    vm_file_code.close()
        # vm_commands = []
        # vm_commands.extend(classes['Sys'])
        # for cls in classes:
        #     if cls != "Sys":
        #         vm_commands.extend(classes[cls])
        return classes

    def create_dir_asm(self):
        file_path = self.dir_path + '.asm'
        print file_path, 'ff'
        open(file_path, 'a').close()

        # Write Bootstrap code in file
        set_sp = ["@256", "D=A", "@SP", "M=D"]
        call_sysinit = ["@Sys.init", "D;JMP"]
        with open(file_path, 'w') as asm_file:
            for sp in set_sp:
                asm_file.write(sp + "\n")
            for call in call_sysinit:
                asm_file.write(call + "\n")
        asm_file.close()
        return file_path


class Code_Writer(object):
    """

    """

    def __init__(self, vm_file_path="", parsed_file="", command_types=""):
        self.vm_file_path = vm_file_path
        self.parsed_file = parsed_file
        self.command_types = command_types

    def write_arithmetic(self, command, ctr, fun_name):
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
        arithmetic_dir = "/home/sid597/Nand-To-Games/projects/08/arithmetic_files_asm"
        for dirpath, dirnames, files in os.walk(arithmetic_dir):
            for file_name in files:
                with open(arithmetic_dir + "/" + file_name, 'r') as ff:
                    file_name = file_name.split('.')[0]
                    file_ = ff.read().splitlines()
                    d[file_name] = file_
        command_list = d[command]
        command_list = self.replace_with_i(command_list, 0, ctr, fun_name)
        return command_list

    def replace_with_i(self, command_list, i, ctr, fun_name):
        """
        %s is for the integer values which need to be replaced
        %f is for replacing with function name
        %t for creating unique names
        :param command_list:
        :param i:
        :param ctr:
        :param fun_name:
        :return:
        """
        for item in range(len(command_list)):
            if "%f" in command_list[item]:
                command_list[item] = command_list[item].replace("%f", fun_name)
            if "%s" in command_list[item]:
                command_list[item] = command_list[item].replace("%s", i)
            if "%t" in command_list[item]:
                command_list[item] = command_list[item].replace("%t", fun_name + str(ctr))
        return command_list

    def label(self, label_name, function_name):
        """

        :param label_name:
        :return:
        """
        commands_list = ["// LABEL COMMAND\n", "(%s)" % (function_name + '$' + label_name.split()[-1]), " "]
        return commands_list

    def goto_label(self, label_name, function_name):
        """

        :param label_name:
        :return:
        """
        command_list = ['// GOTO COMMAND\n', '@%s' % (function_name + '$' + label_name.split()[-1]), 'D;JMP', " "]
        return command_list

    def if_goto_label_name(self, label_name, function_name):
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
        command_list = ['// if-goto COMMAND Name\n', '@SP', 'M=M-1', '@SP', 'A=M', 'D=M',
                        '@%s' % (function_name + '$' + label_name.split()[-1]),
                        'D;JNE', ]
        return command_list

    def return_command(self, instruction, unique):
        function_name = instruction.split()[1]
        with open("/home/sid597/Nand-To-Games/projects/08/return.vm", 'r') as return_commands_file:
            return_command_list = return_commands_file.read().splitlines()
        return_commands_file.close()
        return_list = []
        for ctr in range(len(return_command_list)):
            if '%s' in return_command_list[ctr]:
                return_list.append(return_command_list[ctr].replace('%s', function_name))
            elif '%ret' in return_command_list[ctr]:
                return_list.append(return_command_list[ctr].replace('%ret', function_name + str(unique)))
            else:
                return_list.append(return_command_list[ctr])
        return return_list

    def call_function_command(self, instruction, unique):
        function_name = instruction.split()[1]
        nargs = instruction.split()[-1]
        with open("/home/sid597/Nand-To-Games/projects/08/call.vm", 'r') as call_commands_file:
            call_command_list = call_commands_file.read().splitlines()
        call_commands_file.close()
        call_list = []
        for ctr in range(len(call_command_list)):
            if '%s' in call_command_list[ctr]:
                call_list.append(call_command_list[ctr].replace("%s", function_name))
            elif '%retur' in call_command_list[ctr]:
                call_list.append(call_command_list[ctr].replace("%retur", function_name + str(unique)))
            elif '%nargs' in call_command_list[ctr]:
                call_list.append(call_command_list[ctr].replace('%nargs', nargs))
            else:
                call_list.append(call_command_list[ctr])
        return call_list

    def function_command(self, command):
        keyword, function_name, how_many_times = command.split()
        function_list = ["//FUNCTION COMMAND", "(%s)" % function_name]
        for i in range(int(how_many_times)):
            function_list.extend(["@R0", 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', " "])
        return function_list

    def write_push_pop(self, command, ctr, fun_name):
        command = command.split()
        commandtype = ''.join(command[:2])
        i = command[-1]
        print commandtype, i, command
        d = {}
        push_pop_dir = "/home/sid597/Nand-To-Games/projects/08/pushpop_files_asm"
        for dirpath, dirnames, files in os.walk(push_pop_dir):
            # print files
            for file_name in files:
                with open(push_pop_dir + '/' + file_name, 'r') as ff:
                    file_name = file_name.split('.')[0]
                    file_ = ff.read().splitlines()
                    # print file_
                    d[file_name] = file_
                ff.close()
        command_list = d[commandtype]
        command_list = self.replace_with_i(command_list, i, ctr, fun_name)
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
                command_list = self.label(command)
            elif command_type == "C_GOTO":
                command_list = self.goto_label(command)
            for assembly_command in command_list:
                asm_file.write(assembly_command + "\n")
            print command, command_list
        asm_file.close()

    def get_function_from_class(self, class_dict, desired_function):
        """Find desired_function in class_dict

        How ?
        desired_function will be like :  Class_name.function_name
        split the desired_function and find class in class_dict
        in that class find the first occurence of function name
        from that(first function name) index onwards find index of next function declaration
        meanwhile updating the index of return statement

        Why ?
        Because this is how  a function is defined

        :param class_dict:
        :param desired_function:
        :return:
        """

        class_name = desired_function.split('.')[0]
        # NOTE : Not handling the case where class_name is not present in class_dict assuming it will
        #        always be there

        desired_class = class_dict[class_name]
        desired_function = "function " + desired_function
        first_occurence_index = len(desired_class) + 1
        return_index = len(desired_class) + 1
        for indx in range(len(desired_class)):
            instruction = desired_class[indx]

            if desired_function in instruction:
                first_occurence_index = indx
            elif instruction.split()[0] == 'function':
                break
            elif instruction == 'return':
                return_index = indx
        return desired_class[first_occurence_index:return_index + 1]

    def write_to_directory_file(self, class_dict, write_to_file):
        print " write to file "
        open(write_to_file, 'a').close()
        with open(write_to_file, 'w') as vm_file:
            print 'sdf', class_dict
            set_sp = ["@261", "D=A", "@SP", "M=D"]
            call_sysinit = ["@Sys.init", "D;JMP"]
            for sp in set_sp:
                vm_file.write(sp + "\n")
            for call in call_sysinit:
                vm_file.write(call + "\n")
            for clas in class_dict:
                print clas, '============================================================'
                fun_nam = ''
                for ctr in range(len(class_dict[clas]['asm_commands'])):
                    command = class_dict[clas]['asm_commands'][ctr]
                    command_type = class_dict[clas]['command_type'][ctr]
                    if command_type == "C_ARITHMETIC":
                        command_list = self.write_arithmetic(command, ctr, fun_nam)
                    elif command_type == "C_PUSH" or command_type == "C_POP":
                        command_list = self.write_push_pop(command, ctr, fun_nam)
                    elif command_type == "C_IF":
                        command_list = self.if_goto_label_name(command, fun_nam)
                    elif command_type == "C_LABEL":
                        print fun_nam, command
                        command_list = self.label(command, fun_nam)
                    elif command_type == "C_GOTO":
                        command_list = self.goto_label(command, fun_nam)
                    elif command_type == "C_FUNCTION":
                        command_list = self.function_command(command)
                        fun_nam = command.split()[1].split('.')[0]
                        print command, fun_nam
                    elif command_type == "C_CALL":
                        command_list = self.call_function_command(command, ctr)
                    elif command_type == "C_RETURN":
                        command_list = self.return_command(class_dict[clas]['asm_commands'][0], ctr)
                    for assembly_command in command_list:
                        vm_file.write(assembly_command + "\n")

        vm_file.close()


from pprint import pprint
from collections import deque


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
            parser = Parser(vm_file_code="vm_file_code", file_path="file_path")
            parsed_file, command_type_list = parser.parse_asm()
            code_writer = Code_Writer(file_path, parsed_file, command_type_list)
            code_writer.open_file_and_write()
        vm_file_code.close()

    # If the argv is a dir
    elif os.path.isdir(file_or_dir):
        dir_path = os.path.abspath(file_or_dir)
        print 'IS a directory', file_or_dir

        dir_name = file_or_dir.split('/')[-1]

        parser = Parser(dir_path=dir_path)
        class_dict = parser.parse_directory()
        asm_file_path = (os.getcwd() + "/" + dir_name + "/" + dir_name + '.asm')
        print asm_file_path
        code_writer = Code_Writer()
        code_writer.write_to_directory_file(class_dict, asm_file_path)
        # print class_dict
        # pprint(class_dict)


    else:
        print "Pass a valid file or dir"

    # for file in  os.walk(file_or_dir):
    #     print file


if __name__ == "__main__":
    main()
