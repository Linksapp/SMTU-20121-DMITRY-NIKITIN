if __name__ == '__main__':
    brackets = input()
    right_sequence = ['']*len(brackets)
    buffer = ''
    indexes = ''
    step = 1
    last = 0
    result = True
    max_right_sequence = ''
    if len(brackets) % 2 == 0 and brackets[0] != ']' and brackets[0] != ')' and brackets[0] != '}':
        buffer += brackets[0]
        for x in range(1, len(brackets)):
            if brackets[x] == '(' or brackets[x] == '[' or brackets[x] == '{':
                buffer += brackets[x]
            else:
                if buffer == '':
                    result = False
                    last = x
                    break
                elif (buffer[-1] == chr(ord(brackets[x]) - 2)) or (buffer[-1] == chr(ord(brackets[x]) - 1)):                    
                    right_sequence[brackets.rindex(buffer[-1], 0, x)] = buffer[-1]  
                    right_sequence[x] = brackets[x]
                    buffer = buffer[:-1]
                else:
                    buffer = ''
                    result = False
                    last = x
                    break
    else: result = False

    if not result:
        for j in range(last, len(brackets)):
            if len(''.join(right_sequence)) > len(''.join(max_right_sequence)):
                max_right_sequence = ''.join(right_sequence)
            if brackets[j] == '(' or brackets[j] == '[' or brackets[j] == '{':
                buffer += brackets[j]
            else:
                if buffer == '':
                    continue
                elif (buffer[-1] == chr(ord(brackets[j]) - 2)) or (buffer[-1] == chr(ord(brackets[j]) - 1)):
                    right_sequence[brackets.rindex(buffer[-1], 0, j)] = buffer[-1]  
                    intermediate = list(brackets)
                    intermediate[brackets.rindex(buffer[-1], 0, j)] = '.'
                    brackets = ''.join(intermediate)
                    right_sequence[j] = brackets[j]
                    buffer = buffer[:-1]
                else:
                    buffer = ''
                    right_sequence = ['']*len(brackets)
            if len(''.join(right_sequence)) > len(''.join(max_right_sequence)):
                max_right_sequence = ''.join(right_sequence)
        if max_right_sequence != '': print(max_right_sequence)
        else: print(result)    
    else:
        if len(buffer) == 0:
            print(True)
        else:
            print(False)       
    



