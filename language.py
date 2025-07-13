import sys

def replace_colon_outside_strings(line):
    result = ""
    in_string = False

    for i, char in enumerate(line):
        if (char == '"' or char == "''") and (i == 0 or line[i - 1] != '\\'): # Ignore comments too
            in_string = not in_string  # Toggle in string flag
        if char == ':' and not in_string:
            result += " {"
        else:
            result += char

    return result

def transpile_line(line):
    line = line.replace("jhitta", "for")
    line = line.replace("luhu", "while")
    line = line.replace("spittin", "printf")
    line = line.replace("jawn", "int")
    if line.strip() == "end":
        return "}"
    
    line = replace_colon_outside_strings(line)
    return line

def transpile_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    transpiled_main = []
    transpiled_header = []

    for line in lines:
        if line.strip().startswith("#include"):
            transpiled_header.append(line.strip())
        else:
            transpiled_main.append(transpile_line(line)) 

    print("Transpiled output:")
    for line in transpiled_header + transpiled_main:
        print(line.rstrip())


    with open(output_path, 'w') as f:
        for line in transpiled_header:
            f.write(line + "\n")

        f.write("\nint main() {\n")
        for line in transpiled_main:
            f.write("    " + line)
        f.write("    return 0;\n}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python language.py <input.jh> <output.c>")
        sys.exit(1)

    transpile_file(sys.argv[1], sys.argv[2])
