import sys

def transpile_line(line):
    line = line.replace("jhitta", "for")
    line = line.replace(":", "{")
    if line.strip() == "end":
        return "}"
    return line

def transpile_file(input_path, output_path):
    with open(input_path, 'r') as f:
        lines = f.readlines()

    transpiled = [transpile_line(line) for line in lines]

    print("Transpiled output:")
    for line in transpiled:
        print(line.rstrip())

    with open(output_path, 'w') as f:
        f.write('#include <stdio.h>\n\nint main() {\n')
        for line in transpiled:
            f.write("    " + line)
        f.write("    return 0;\n}\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python language.py <input.jh> <output.c>")
        sys.exit(1)

    transpile_file(sys.argv[1], sys.argv[2])
