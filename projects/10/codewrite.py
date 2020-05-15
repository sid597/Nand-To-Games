def write_string(string):
    l = len(string)
    print 'push constant %s' %l
    print 'call String.new 1'
    for i in range(l):
        print 'push constant %s' %ord(string[i])
        print 'call String.append 2'
    print 'call Output.printString 1'
# print write_string('abc')

def string_constant(xml_command):
    print xml_command.split()
    tokens =xml_command.replace('<stringConstant> ', '').replace('</stringConstant>', '')
    print tokens

    return False

print string_constant('<stringConstant> How many numbers? </stringConstant>')