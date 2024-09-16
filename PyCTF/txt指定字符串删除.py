filename = r"C:\Users\Administrator\Desktop\virt\flag"
string_to_remove = '0x'

with open(filename, 'r') as f:
    lines = f.readlines()

with open(filename, 'w') as f:
    for line in lines:
        if string_to_remove not in line:
            f.write(line)