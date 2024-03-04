import random
import numpy as np

def obfuscate(code, alphabet, sets_num, min_name_length):
    name_vars = ["I", "l", "L", "J", "i"]
    mixed_alphabet = ''.join(random.sample(alphabet, len(alphabet)))

    alphabets = []
    sets = []
    for x in range(sets_num):
        name = ''.join(random.choices(name_vars, k=min_name_length))
        while name in sets:
            min_name_length += 1
            name = ''.join(random.choices(name_vars, k=min_name_length))
        sets.append(name)

    for l in np.array_split(list(mixed_alphabet), sets_num):
        li = []
        for i in l:
            li.append(i)
        alphabets.append(li)

    new_code = "@echo off\nREM Obfuscator Made By Gib\n"
    for x in range(len(sets)):
        new_code = new_code + "Set " + sets[x] + "=" + ''.join(alphabets[x]) + " &"
        print("Generating Names For Vars")
    new_code = new_code + "\nREM Set lILJliL\ncls\nREM Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set \nREM Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set \nREM Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set Set \n"

    for c in code:
        last = False
        for x in range(len(alphabets)):
            if c in alphabets[x]:
                if last:
                    new_code = new_code[:-1]
                new_code = new_code + "%" + sets[x] + ":~" + str(''.join(alphabets[x]).find(c)) + ",1%"
                break
            else:
                if not last:
                    new_code = new_code + c
                    last = True

    return new_code

alphabet_chars = "0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

with open("Example.bat", "r") as f:
    code = f.read()

obfuscated_code = obfuscate(code, alphabet_chars, 200, 150)

with open("Example_Protected.bat", "w") as protected_file:
    protected_file.write(obfuscated_code)

print("Obfuscated code written to Example_Protected.bat")