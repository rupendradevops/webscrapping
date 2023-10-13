def read_10th_character_second_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                second_line = lines[1].strip()
                if len(second_line) >= 10:
                    tenth_character = second_line[9]
                    return tenth_character
                else:
                    return "The second line does not have at least 10 characters."
            else:
                return "The file does not have at least two lines."
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    file_path = "example.txt"

    tenth_character = read_10th_character_second_line(file_path)

    print("The 10th character in the second line:", tenth_character)








