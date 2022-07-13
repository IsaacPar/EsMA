from sys import argv

def parse(a, x, y, stack):

    argvs = argv[1:]

    # first, loop throug the argvs
    for arg in argvs:
        # if the arg is -i, then we get the next argument and save it as input file
        if arg == '-i':
                input_file = argvs[argvs.index(arg) + 1]
                # if the input file is a file, then we open it and read it
                with open(input_file, 'r') as f:
                    # we read the file and save it as a string
                    input_string = f.read()

                    # we split the string into a list of lines
                    input_lines = input_string.split('\n')

                    # we loop through the lines
                    for line in input_lines:
                        # if the line is empty, then we skip it
                        if line == '':
                            continue
                        # if the line is a comment, then we skip it
                        if line[0] == '#':
                            continue

                        # replace (#a) with a's value
                        line = line.replace('#a', str(a))
                        # replace (#x) with x's value
                        line = line.replace('#x', str(x))
                        # replace (#y) with y's value
                        line = line.replace('#y', str(y))

                        # we get the first character of the line
                        first_char = line[0]
                        # we get everything from the third char to the end of the line -1
                        rest_of_line = line[2:len(line)-1]

                        # print(rest_of_line)

                        line_args = rest_of_line.split(',')

                        if first_char == 'p':

                            # print the first argument of line_args that is a ascii char
                            print(chr(int(line_args[0])))
                        elif first_char == 'P':
                            # print the first argument of line_args that is a ascii char
                            print(chr(int(line_args[0])), end='')

                        elif first_char == 'm':

                            # if the first argument is 1, then we set a to the second argument
                            if line_args[0] == '1':
                                a = int(line_args[1])
                            # if the first argument is 2, then we set x to the second argument
                            elif line_args[0] == '2':
                                x = int(line_args[1])
                            # if the first argument is 3, then we set y to the second argument
                            elif line_args[0] == '3':
                                y = int(line_args[1])

                        elif first_char == 'i':

                            # if the first argument is 1, then we set a to a+1
                            if line_args[0] == '1':
                                a += 1
                            # if the first argument is 2, then we set x to x+1
                            elif line_args[0] == '2':
                                x += 1
                            # if the first argument is 3, then we set y to y+1
                            elif line_args[0] == '3':
                                y += 1

                        elif first_char == 'd':

                            # if the first argument is 1, then we set a to a-1
                            if line_args[0] == '1':
                                a -= 1
                            # if the first argument is 2, then we set x to x-1
                            elif line_args[0] == '2':
                                x -= 1
                            # if the first argument is 3, then we set y to y-1
                            elif line_args[0] == '3':
                                y -= 1

                        elif first_char == 'a':

                            # add the first argument to the a register and save the result on the a register
                            a = a + int(line_args[0])

                        elif first_char == 's':

                            # subtract the first argument from the a register and save the result on the a register
                            a = a - int(line_args[0])

                        elif first_char == 'u':

                            # if the first argument is 1, then we psuh the a register on the stack
                            if line_args[0] == '1':
                                stack.append(a)
                            # if the first argument is 2, then we push the x register on the stack
                            elif line_args[0] == '2':
                                stack.append(x)
                            # if the first argument is 3, then we push the y register on the stack
                            elif line_args[0] == '3':
                                stack.append(y)

                            print(stack)

                        elif first_char == 'o':

                            # if the first argument is 1, then we pop the a register from the stack
                            if line_args[0] == '1':
                                print(stack.pop())
                            # if the first argument is 2, then we pop the x register from the stack
                            elif line_args[0] == '2':
                                print(stack.pop())
                            # if the first argument is 3, then we pop the y register from the stack
                            elif line_args[0] == '3':
                                print(stack.pop())

                            print(stack)
                        elif first_char == 'j':
                            # it gets the first argument, as the number of the line we want to jump to
                            jump_to = int(line_args[0]) - 1
                            # we need to jump to the desired line
                            # we loop through the lines
                            for line in input_lines:
                                # if the line is empty, then we skip it
                                if line == '':
                                    continue
                                # if the line is a comment, then we skip it
                                if line[0] == '#':
                                    continue
                                # if the line is the line we want to jump to, then we break the loop
                                if input_lines.index(line) == jump_to:
                                    print("jumped to line " + str(jump_to))
                                    parse(a, x, y, stack)
                                    break
                            # we continue the loop
                            continue
                        else:
                            custom_exception('Unknown command: ' + first_char)

                    # we close the file
                    f.close()

def custom_exception(message):
    print(message)
    exit(0)