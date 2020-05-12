"""
This will be a 2 pass algorithm in 1st pass I will remove all the comments and whitespace.
In the 2nd pass will convert the input to tokens.

How to implement this ?
Can be done by procedural programming or by object oriented style

1. Procedure programming :
    a) Will make a function to remove the comments from original passed list and output the list without comm
    -ents and whitespace
    b) Then this removed_comments_list will be passed to a function to tokenize all the expression in list
        This will out put a list which is a tokenised list containing all the tokens. Also write to an xml
        file all the tokens
2. OOP :
    I think this will not be a very good implementation using classes many static functions would have to
    be implemented so I think I should just use Procedure programming instead

Consider the input as a stream of inputs i.e consider the following input file. So instead of reading all
the lines one by one we can do processing  without worrying about the unseen data

    Problems to solve :
     How to find comments : single line and multiple line both ?
        Based on how I solve this problem the representation of data will be decided
        1. Read line from file if the line contains /** remove all words after /** and continue parsing till find */


Token can be one of the following 5 :
1. Keyword
2. Symbol
3. Integer Constant
4. String Constant
5. Identifier
"""

import os
import sys
from pprint import pprint


# pprint(read_and_return_input_list(args[-1]))


def keyword(token_name):
    return '<keyword> %s </keyword>' % token_name


def symbol(token_name):
    special_chars = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    if token_name in special_chars:
        return '<symbol> %s </symbol>' % special_chars[token_name]
    else:
        return '<symbol> %s </symbol>' % token_name


def string_constant(token_name):
    return '<stringConstant> %s </stringConstant>' % token_name[1:-1]


def identifier(token_name):
    return '<identifier> %s </identifier>' % token_name


def integer_constant(token_name):
    return '<integerConstant> %s </integerConstant>' % token_name


def is_int(token):
    if token.isdigit():
        if int(token) in xrange(0, 32768):
            return True
    return False


def is_string(token):
    if token[0] == '"' and token[-1] == '"':
        if '"' not in token[1:-1] and '\n' not in token:
            return True
    return False


def is_identifier(token):
    if not (token[0].isdigit()):
        token = token.replace('_', '')
        if token.isalnum():
            return True
    return False


def token_type(token):
    keywords_dict = {'class', 'constructor', 'function',
                     'method', 'field', 'static', 'var',
                     'int', 'char', 'boolean', 'void', 'true',
                     'false', 'null', 'this', 'let', 'do',
                     'if', 'else', 'while', 'return'}
    symbols_dict = {'{', '}', '(', ')', '[', ']', '.',
                    ',', ';', '+', '-', '*', '/', '&',
                    '|', '<', '>', '=', '~'}
    if token in keywords_dict:
        return "KEYWORD"
    elif token in symbols_dict:
        return "SYMBOL"
    elif is_string(token):
        return "STRING"
    elif is_int(token):
        return "INT"
    elif is_identifier(token):
        return "IDENTIFIER"
    else:
        return None


# l = 'let a[i] = Keyboard.readInt("ENTER THE NEXT NUMBER: ");'.split()
# print l
# for i in l:
#     print i,token_type(i)

def splitter(line):
    """Consider the following line :
        -->   while (i<j) ;
        We want to know what are the different types of tokens in the above and to do that we will parse it
        we can't simply split by white space because then we will classify '(i<j)' as 1 token but it is made
        of several tokens not one.
        So to solve this issue we will go 1 by 1 over each character and check if the char is alphanumeric type or not
        if its not we wil check if this is a symbol and add it as a different token
    :param line:
    :return:
    """
    split_list = []
    s = ""
    char_ctr = 0
    while char_ctr < len(line):
        char = line[char_ctr]
        if char == " ":
            if s:
                split_list.append(s)
            s = ""
            char_ctr += 1
        elif char == '"':
            end_string = line[char_ctr + 1:].index('"') + char_ctr + 1
            string = '"' + line[char_ctr + 1:end_string] + '"'
            split_list.append(string)
            char_ctr = end_string + 1

        elif not char.isalnum() and char != '_':
            if s:
                split_list.append(s)
            if char:
                split_list.append(char)
            s = ''
            char_ctr += 1
        else:
            s += char
            char_ctr += 1
    return split_list


def remove_api_comments(input_list):
    """"Remove api and inline comments from the input list

    ASSUMPTION : There are no nested comments inside another comment
    API comments : /** ...... */
    INLINE comments : // ........


    How does this work ?
        Go through all the lines in the input using a ctr
        if comment starts in the current line then check if it ends in current line itself ?
        if it does remove the comment
        else find in which line does the comment end and remove all the lines from input till that

        If there is an inline comment it will also be removed
    :param input_list:
    :return:
    """
    ctr = 0
    nl = []
    while ctr < len(input_list):
        current_input = input_list[ctr].strip()
        if '/t' in current_input:
            current_input = current_input.replace('/t', '')
        # print current_input
        if '/**' in current_input:
            #  If the comment ends in the current line itself
            if '*/' in current_input:
                current_input = (current_input[:current_input.index('/**')] + current_input[
                                                                              current_input.index('*/') + 2:]).strip()
                if current_input:
                    nl.append(current_input)
                ctr += 1
            #  else
            else:
                nl.append(current_input[:current_input.index('/**')])
                for ptr in range(ctr, len(input_list)):
                    if '*/' in input_list[ptr]:
                        ctr = ptr + 1
                        current_input = input_list[ptr]
                        current_input = current_input[current_input.index('*/') + 2:].strip()
                        if current_input:
                            nl.append(current_input)
                        break
        elif '//' in current_input:
            current_input = current_input[:current_input.index('//')]
            if current_input:
                nl.append(current_input)
            ctr += 1
        else:

            if current_input:
                nl.append(current_input)
            ctr += 1
    return nl


# print remove_api_comments(['while ctr //ptr:',
#                            '  ',
#                            'sdf //sdf/** sdfsd/ dfg ',
#                            '    ',
#                            '    ',
#                            'sdfs',
#                            'gfdg;s',
#                            'sdfkj',
#                            'asdf',
#                            'asdasd */ helloworld',
#                            'hello'])


def remove_block_comments(input_list):
    """"Remove block comments from the input list

    ASSUMPTION : There are no nested comments inside another comment
    BLOCK comments : /*.......*/

    How does this work ?
        Same as above
    :param input_list:
    :return:
    """
    ctr = 0
    nl = []
    while ctr < len(input_list):
        current_input = input_list[ctr].strip()
        # print current_input
        if '/*' in current_input:
            #  If the comment ends in the current line itself
            if '*/' in current_input:
                current_input = (current_input[:current_input.index('/**')] + current_input[
                                                                              current_input.index('*/') + 2:]).strip()
                if current_input:
                    nl.append(current_input)
                ctr += 1
            #  else
            else:
                nl.append(current_input[:current_input.index('/*')])
                for ptr in range(ctr, len(input_list)):
                    if '*/' in input_list[ptr]:
                        ctr = ptr + 1
                        current_input = input_list[ptr]
                        current_input = current_input[current_input.index('*/') + 2:].strip()
                        if current_input:
                            nl.append(current_input)
                        break
        else:
            if current_input:
                nl.append(current_input)
            ctr += 1
    return nl


# print remove_block_comments(['while ctr //ptr:',
#                            '  ',
#                            'sdf //sdf/* sdfsd/ dfg ',
#                            '    ',
#                            '    ',
#                            'sdfs',
#                            'gfdg;s',
#                            'sdfkj',
#                            'asdf',
#                            'asdasd */ helloworld',
#                            'hello'])

def read_and_return_input_list(file_name):
    file_path = os.path.abspath(file_name)

    input_list = []
    with open(file_path, 'r') as input_stream:
        input_list = input_stream.read().splitlines()
    return input_list


# pprint (read_and_return_input_list(args[-1]))


def main():
    """
    Main function to handle the circus
    :return:
    """
    args = sys.argv
    # Get the file name
    input_list = read_and_return_input_list(args[-1])
    # Remove api and inline comments
    rem_api_comments = remove_api_comments(input_list)
    # Remove block comments
    rem_block_comments = remove_block_comments(rem_api_comments)
    # Create a xml file with the same name as the passed one and to it tokenized commands
    with open(args[-1].split('.')[0] + 'TT.xml', 'w') as write_to_xml:
        write_to_xml.write('<tokens> \n')
        for line in rem_block_comments:
            splitted_line = splitter(line)
            for token in splitted_line:
                tokn_type = token_type(token)
                if tokn_type == "KEYWORD" :
                    output = keyword(token)
                elif tokn_type == "SYMBOL":
                    output = symbol(token)
                elif tokn_type == "STRING":
                    output = string_constant(token)
                elif tokn_type == "INT":
                    output = integer_constant(token)
                elif tokn_type == "IDENTIFIER":
                    output = identifier(token)
                write_to_xml.write(output + '\n')
        write_to_xml.write('</tokens> \n')
        write_to_xml.close()


if __name__ == "__main__":
    main()