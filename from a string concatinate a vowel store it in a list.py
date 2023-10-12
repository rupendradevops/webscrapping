def extractvowels(inputstring):
    vowels = "aeiouAEIOU"
    vowel_list = []
    for char in inputstring:
        if char in vowels:
            vowel_list.append(char)
    return vowel_list
if __name__ == "__main__":
    input_string = input("enter a string:")
    vowels_list = extractvowels(input_string)
    if vowels_list:
        print("vowelsfound in the string:")
        print(vowels_list)
    else:
        print("no vowels found in the string.")

########

import os
os.chdir("c:/BinaryFilesDemo")
fp = open("c:/BinaryFilesDemo/readLine.txt", "r")

currentLine = 1

expectLine = 3
for i in fp:
    if currentLine == expectLine:
        print(i)
        fp.seek(39)
        a = fp.readline(11)
        print(a)
        break

    else:
        currentLine = currentLine+1