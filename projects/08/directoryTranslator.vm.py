import os
import inspect
class Parser:

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def parse_directory(self):
        for dirpath, dirnames, files in os.walk(self.dir_name):
            dir_name = dirpath.split('/')[-1]
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