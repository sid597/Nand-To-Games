# arithmetic_commands = set()
# for i in range(9):
#     arithmetic_commands.add(raw_input())
# print arithmetic_commands


# with open("/home/sid597/Nand-To-Games/projects/07/MemoryAccess/BasicTest/BasicTest.vm", 'r') as fm:
#     print fm.readlines()


# for i in range()
import os
# def arithematic(command_type):
#     d = {}
#     for dirpath, dirnames, files in os.walk("./arithmetic"):
#         for file_name in files:
#             with open("./arithmetic/" + file_name, 'r') as ff:
#                 file_name = file_name.split('.')[0]
#                 file_ = ff.read().splitlines()
#                 d[file_name] = file_
#
#     return d
# print arithematic("or")

print "dfgdfgdfg%s"%"sddfg"
# with open("./arithmetic/dummy.asm",'a') as jj:
#     jj.write(ff.read())
# print open("./arithmetic/dummy.asm",'r').read()

def replace_with_i( command_list, i):
    for item in range(len(command_list)):
        if "%s" in command_list[item]:
            command_list[item] = command_list[item].replace("%s", i)

    return command_list
def write_push_pop(  command):
    command = command.split()
    commandtype = ''.join(command[:2])
    i = command[-1]
    print commandtype,i
    d = {}
    for dirpath, dirnames, files in os.walk("./pushpop"):
        for file_name in files:
            with open("./pushpop/" + file_name, 'r') as ff:
                file_name = file_name.split('.')[0]
                file_ = ff.read().splitlines()
                d[file_name] = file_
    command_list = d[commandtype]
    command_list = replace_with_i(command_list,i)
    return command_list
print write_push_pop("push static 1")