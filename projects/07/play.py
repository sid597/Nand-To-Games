# # # # # arithmetic_commands = set()
# # # # # for i in range(9):
# # # # #     arithmetic_commands.add(raw_input())
# # # # # print arithmetic_commands
# # # #
# # # #
# # # # # with open("/home/sid597/Nand-To-Games/projects/07/MemoryAccess/BasicTest/BasicTest.vm", 'r') as fm:
# # # # #     print fm.readlines()
# # # #
# # # #
# # # # # for i in range()
# # # # import os
# # # # # def arithematic(command_type):
# # # # #     d = {}
# # # # #     for dirpath, dirnames, files in os.walk("./arithmetic_files_asm"):
# # # # #         for file_name in files:
# # # # #             with open("./arithmetic_files_asm/" + file_name, 'r') as ff:
# # # # #                 file_name = file_name.split('.')[0]
# # # # #                 file_ = ff.read().splitlines()
# # # # #                 d[file_name] = file_
# # # # #
# # # # #     return d
# # # # # print arithematic("or")
# # # #
# # # # print "dfgdfgdfg%s"%"sddfg"
# # # # # with open("./arithmetic_files_asm/dummy.asm",'a') as jj:
# # # # #     jj.write(ff.read())
# # # # # print open("./arithmetic_files_asm/dummy.asm",'r').read()
# # # #
# # # # def replace_with_i( command_list, i):
# # # #     for item in range(len(command_list)):
# # # #         if "%s" in command_list[item]:
# # # #             command_list[item] = command_list[item].replace("%s", i)
# # # #
# # # #     return command_list
# # # # def write_push_pop(  command):
# # # #     command = command.split()
# # # #     commandtype = ''.join(command[:2])
# # # #     i = command[-1]
# # # #     print commandtype,i
# # # #     d = {}
# # # #     for dirpath, dirnames, files in os.walk("./pushpop_files_asm"):
# # # #         for file_name in files:
# # # #             with open("./pushpop_files_asm/" + file_name, 'r') as ff:
# # # #                 file_name = file_name.split('.')[0]
# # # #                 file_ = ff.read().splitlines()
# # # #                 d[file_name] = file_
# # # #     command_list = d[commandtype]
# # # #     command_list = replace_with_i(command_list,i)
# # # #     return command_list
# # # # print write_push_pop("push static 1")
# # #
# # # # command_list = ["// Label", "@%s"]
# # # #
# # # # for i in range(len(command_list)):
# # # #      command_list[i] = command_list[i] + "\n"
# # # # print command_list\
# # # import os
# # # import inspect
# # #
# # #
# # # def remove_comments(command):
# # #     """Remove comments from command received
# # #
# # #     :param command: the command whose comments have to be removed
# # #     :return: command with comments removed
# # #     """
# # #     split_command = command.split("//")
# # #     # print split_command,command, "---------"
# # #     if not len(split_command):
# # #         return ''
# # #     else:
# # #         return split_command[0].strip()
# # #
# # #
# from pprint import  pprint
# # # def parse_directory(directory):
# # # #
# # # #         """
# # # #         This method does 3 things:
# # # #         1. Create a .asm file with the same name as the directory
# # # #         2. Create a dictionary with all the content in different vm files( i.e different classes) in the directory
# # # #         3. Remove comments from all the classes
# # # #         :return:
# # # #         """
# # # #         classes = {}
# # # #         for dirpath, dirnames, files in os.walk(directory):
# # # #             print dirpath, dirnames, files
# # # #             for file_name in files:
# # # #                 if file_name.endswith('.vm'):
# # # #                     file_path = (os.getcwd() + "/" + dirpath + "/" + file_name)
# # # #                     print file_path
# # # #                     with open(file_path, 'r') as vm_file_code:
# # # #                         instructions = vm_file_code.read().splitlines()
# # # #                         class_name = file_name.split('.')[0]
# # # #                         classes[class_name] = instructions
# # # #                     vm_file_code.close()
# # # #
# # # #         # remove comments
# # # #         for cls in classes:
# # # #             for indx in range(len(cls)):
# # # #                 instruction = remove_comments(cls[indx])
# # # #                 if instruction:
# # # #                     classes[cls[indx]] = instruction
# # # #
# # # #         # create_dir_asm()
# # # #         return classes
# # #
# # # # parse_directory("../08/FunctionCalls/StaticsTest")
# # #
# # # classd =['function Sys.init 0',
# # #  'push constant 4000',
# # #  'pop pointer 0',
# # #  'push constant 5000',
# # #  'pop pointer 1',
# # #  'call Sys.main 0',
# # #  'pop temp 1',
# # #  'label LOOP',
# # #  'goto LOOP',
# # #  'function Sys.main 5',
# # #  'push constant 4001',
# # #  'pop pointer 0',
# # #  'push constant 5001',
# # #  'pop pointer 1',
# # #  'push constant 200',
# # #  'pop local 1',
# # #  'push constant 40',
# # #  'pop local 2',
# # #  'push constant 6',
# # #  'pop local 3',
# # #  'push constant 123',
# # #  'call Sys.add12 1',
# # #  'pop temp 0',
# # #  'push local 0',
# # #  'push local 1',
# # #  'push local 2',
# # #  'push local 3',
# # #  'push local 4',
# # #  'add',
# # #  'add',
# # #  'add',
# # #  'add',
# # #  'return',
# # #  'function Sys.add12 0',
# # #  'push constant 4002',
# # #  'pop pointer 0',
# # #  'push constant 5002',
# # #  'pop pointer 1',
# # #  'push argument 0',
# # #  'push constant 12',
# # #  'add',
# # #  'return']
# # #
# # #
# # #
# # # def command_type(command):
# # #     command_and_its_types = {"//": "", 'and': 'C_ARITHMETIC', 'gt': 'C_ARITHMETIC', 'sub': 'C_ARITHMETIC',
# # #                              'neg': 'C_ARITHMETIC',
# # #                              'lt': 'C_ARITHMETIC', 'add': 'C_ARITHMETIC', 'not': 'C_ARITHMETIC',
# # #                              'eq': 'C_ARITHMETIC',
# # #                              'or': 'C_ARITHMETIC', 'push': 'C_PUSH', 'pop': 'C_POP', 'if-goto': 'C_IF',
# # #                              'label': 'C_LABEL', 'goto': "C_GOTO", 'call': "C_CALL", 'function': "C_FUNCTION",
# # #                              'return': "C_RETURN"}
# # #     split_command = command.split()
# # #     command_typ = split_command[0]
# # #     has_comments = False
# # #     if "//" in command:
# # #         has_comments = True
# # #     return command_and_its_types[command_typ], has_comments
# # #
# # #
# # # from pprint import pprint
# # #
# # #
# # # def get_function_from_class(class_dict, desired_function):
# # #     class_name = desired_function.split('.')[0]
# # #     desired_class = class_dict[class_name]
# # #     desired_function = "function " + desired_function
# # #     first_occurence_index = len(desired_class) + 1
# # #     return_index = len(desired_class) + 1
# # #
# # #     for indx in range(len(desired_class)):
# # #         instruction = desired_class[indx]
# # #         # print instruction,desired_function
# # #
# # #         if desired_function in instruction:
# # #
# # #             first_occurence_index = indx
# # #         elif (instruction.split()[0] == 'function') and (return_index != len(desired_class) + 1):
# # #             break
# # #         elif instruction == 'return':
# # #             return_index = indx
# # #     # print first_occurence_index, return_index
# # #     # pprint(desired_class[first_occurence_index:return_index + 1])
# # #     return return_index
# #
# # from collections import deque
# #
# # classd = ['function Sys.init 0',
# #           'push constant 4000',
# #           'pop pointer 0',
# #           'push constant 5000',
# #           'pop pointer 1',
# #           'call Sys.main 0',
# #           'pop temp 1',
# #           'label LOOP',
# #           'goto LOOP',
# #           'function Sys.main 5',
# #           'push constant 4001',
# #           'pop pointer 0',
# #           'push constant 5001',
# #           'pop pointer 1',
# #           'push constant 200',
# #           'pop local 1',
# #           'push constant 40',
# #           'pop local 2',
# #           'push constant 6',
# #           'pop local 3',
# #           'push constant 123',
# #           'call Sys.add12 1',
# #           'pop temp 0',
# #           'push local 0',
# #           'push local 1',
# #           'push local 2',
# #           'push local 3',
# #           'push local 4',
# #           'add',
# #           'add',
# #           'add',
# #           'add',
# #           'return',
# #           'function Sys.add12 0',
# #           'push constant 4002',
# #           'pop pointer 0',
# #           'push constant 5002',
# #           'pop pointer 1',
# #           'push argument 0',
# #           'push constant 12',
# #           'add',
# #           'return']
# #
# #
# # def find_index(commands, command):
# #     for i in range(len(commands)):
# #         if command in commands[i]:
# #             return i
# #     return None
# #
# #
# # def find_last_index(commands, command, start_index):
# #     index = None
# #     for i in range(start_index + 1, len(commands)):
# #
# #         if command in commands[i]:
# #             index = i
# #         if 'function' in commands[i]:
# #             return index
# #     return index
# #
# #
# # def convert(classd):
# #     """Think of the file to be translated a big file of all the functions needed so just need to jump to function
# #         location after saving the current ctr location in stack
# #     :param classd:
# #     :param which_class:
# #     :return:
# #     """
# #     call_stack = []
# #     # print classd
# #     ctr = 0
# #     l = []
# #     ptr = 0
# #     vm_commands = classd
# #     s = set(i for i in range(1, len(vm_commands)))
# #     last_return = None
# #     current_clas = ''
# #     while s:
# #
# #         ptr += 1
# #         instruction = vm_commands[ctr]
# #
# #         if "call" in instruction:
# #             function_class = instruction.split()[1]
# #             print ctr, function_class, current_clas
# #             if function_class == current_clas:
# #                 l.append(instruction)
# #                 ctr += 1
# #                 try:
# #                     s.remove(ctr)
# #                 except:
# #                     pass
# #             else:
# #
# #                 l.append(instruction)
# #                 instruction_index = find_index(vm_commands, "function " + instruction.split()[1])
# #                 call_stack.append(ctr)
# #                 ctr = instruction_index
# #                 try:
# #                     s.remove(ctr)
# #                 except:
# #                     pass
# #         elif 'function' in instruction:
# #             l.append(instruction)
# #             strt_index = find_index(vm_commands, instruction)
# #             current_clas = instruction.split()[1]
# #             return_indx = find_last_index(vm_commands, 'return', strt_index)
# #             last_return = return_indx
# #             ctr += 1
# #             try:
# #                 s.remove(ctr)
# #             except:
# #                 pass
# #
# #
# #         elif "return" in instruction:
# #             print ptr, ctr, last_return, call_stack
# #             l.append(instruction)
# #             # print last_return
# #             if len(call_stack) != 0 and last_return == ctr:
# #                 ctr = call_stack.pop() + 1
# #                 print s
# #                 try:
# #                     s.remove(ctr)
# #                 except:
# #                     pass
# #             elif last_return == ctr:
# #                 return l
# #             # elif  last_return == ctr:
# #             #     return l
# #             else:
# #                 ctr += 1
# #             try:
# #                 s.remove(ctr)
# #             except:
# #                 pass
# #         else:
# #             l.append(instruction)
# #             ctr += 1
# #             try:
# #                 s.remove(ctr)
# #             except:
# #                 pass
# #     return l
# #
# #
# # print convert(classd)
# # print len(classd)
#
# ls = ['function Sys.init 0',
#  'push constant 6',
#  'push constant 8',
#  'call Class1.set 2',
#  'pop temp 0',
#  'push constant 23',
#  'push constant 15',
#  'call Class2.set 2',
#  'pop temp 0',
#  'call Class1.get 0',
#  'call Class2.get 0',
#  'label WHILE',
#  'goto WHILE',
#  'function Class2.set 0',
#  'push argument 0',
#  'pop static 0',
#  'push argument 1',
#  'pop static 1',
#  'push constant 0',
#  'return',
#  'function Class2.get 0',
#  'push static 0',
#  'push static 1',
#  'sub',
#  'return',
#  'function Class1.set 0',
#  'push argument 0',
#  'pop static 0',
#  'push argument 1',
#  'pop static 1',
#  'push constant 0',
#  'return',
#  'function Class1.get 0',
#  'push static 0',
#  'push static 1',
#  'sub',
#  'return']
#
#
#
#
# def find_function_ending(from_class, start_index):
#     """A function can end in 2 ways :
#         1. Hit the end
#         2. Another function def starts
#     """
#
#     for i in range(start_index+1,len(from_class)):
#         if from_class[i].split()[0] == 'function':
#             return i
#     return i+1
#
# def extract_functions(from_class):
#     """
#     Give a list (which represents some class implemented in vm) find all the functions in the list
#     :param from_class:
#     :return: dict containing all the lists
#     """
#
#     # Get index of each functions from where they start
#     functions_starting_indexes =[]
#     functions_list = []
#     d = {}
#
#     for indx in range(len(from_class)):
#          if from_class[indx].split()[0] == "function":
#             functions_starting_indexes.append(indx)
#
#     # for each indx in functions_list find their ending
#     for start_index in functions_starting_indexes:
#
#         end_index = find_function_ending(from_class, start_index)
#
#         function_name = from_class[start_index].split()[1]
#         functions_list.append(function_name)
#         d[function_name] = {}
#         d[function_name]['func'] = from_class[start_index:end_index]
#         d[function_name]['start_index'] = start_index
#         d[function_name]['end_index'] =end_index
#     # add the function from start index to end in dict stating functions name and the function itself
#     return d,functions_list
#
#
#
# def function_calls_another(caller_function):
#     """
#     See what other functions this function is calling and where
#     :param caller_function:
#     :return:
#     """
#     calling = []
#     this_function = caller_function[0].split()[1]
#     for command_indx in range(len(caller_function)):
#         if caller_function[command_indx].split()[0] == 'call' and caller_function[command_indx].split()[1] != this_function:
#             calling.append([caller_function[command_indx].split()[1], command_indx])
#     return calling
#
#
# def find_functions_dependency(functions_dict):
#     """
#
#     :param functions_dict:  A dict of all the individual functions in this class
#     :return:
#     """
#     dependency_functions = {}
#     for func in functions_dict:
#         dependents = function_calls_another(functions_dict[func]['func'])
#         dependency_functions[func] = dependents
#     return dependency_functions
#
# all_functions_dict, functions_list =  extract_functions(ls)
# # pprint (all_functions_dict)
# l= find_functions_dependency(all_functions_dict)
#
# # print l
# # print functions_list
# # ['Sys.add12','Sys.init', 'Sys.main']
#
# # for i in all_functions_dict:
# #     print all_functions_dict[i]['start_index'], all_functions_dict[i]['end_index']
# #     print i,ls[all_functions_dict[i]['start_index']: all_functions_dict[i]['end_index']]
#     # print all_functions_dict[i]['start_index']
#
#
#
# def combine_all(functions_dict, functions_call_order_list):
#     start_stack = []
#     end_stack = []
#     function_stack = []
#     current_function = functions_call_order_list[0]
#     functions_dependencies = find_functions_dependency(functions_dict)
#     combined_list = []
#     current_function_end = functions_dict[current_function]['end_index']
#     current_function_starts = functions_dict[current_function] ['start_index']
#     current_function_instructions = functions_dict[current_function]['func']
#     current_function_dependency_ctr = functions_dependencies[current_function]
#     # print current_function_dependency_ctr
#     ctr = 0
#     while ctr < current_function_end:
#         print ctr,current_function_dependency_ctr,current_function
#         if len(current_function_dependency_ctr) != 0:
#             if ctr != current_function_dependency_ctr[0][1]:
#                 combined_list.append(current_function_instructions[ctr])
#                 ctr+=1
#             else:
#                 combined_list.append(current_function_instructions[ctr])
#                 print combined_list,'--------------'
#                 start_stack.append(ctr)
#                 end_stack.append(current_function_end)
#                 function_stack.append(current_function)
#                 current_function = current_function_dependency_ctr[0][0]
#                 current_function_end = functions_dict[current_function]['end_index']
#                 current_function_starts = functions_dict[current_function]['start_index']
#                 current_function_instructions = functions_dict[current_function]['func']
#                 current_function_dependency_ctr = functions_dependencies[current_function]
#                 print current_function_dependency_ctr,current_function
#                 ctr = 0
#
#         else:
#
#             combined_list.extend(current_function_instructions)
#             ctr = current_function_end
#
#     if len(start_stack) != 0 :
#         print start_stack,end_stack,function_stack
#         for i in range(len(start_stack)):
#             start = start_stack.pop()
#             end = end_stack.pop()
#             c_fun = function_stack.pop()
#             current_function_ = functions_dict[c_fun]['func'][start+1:end]
#             print current_function_
#             combined_list.extend(current_function_)
#     # return combined_list
#
# pprint (combine_all(all_functions_dict,functions_list ))
def return_command( function_name):
    with open("./return.vm", 'r') as return_commands_file:
        return_command_list = return_commands_file.read().splitlines()
    return_commands_file.close()
    return_list = []
    for command in return_command_list:
        if '%s' in command:

            return_list.append(command.replace('%s', function_name))
        else:
            return_list.append(command)
    return return_list


def call_function_command( function_name):
    with open("./call.vm", 'r') as call_commands_file:
        call_command_list = call_commands_file.read().splitlines()
    call_commands_file.close()
    call_list = []
    for command in call_commands_file:
        if '%s' in command:
            call_list.append(command.replace("%s", function_name))
        else:
            call_list.append(command)
    return call_list


def function_command(command):
    keyword,function_name,how_many_times = command.split()
    function_list = ["(%s)" % function_name]
    for i in range(int(how_many_times)):

        function_list.extend(["@R0",'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1'])
    return function_list

print function_command('function Sys.init 0')
print call_function_command("call Class1.set 2")