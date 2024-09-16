filename = r"C:\Users\Administrator\Desktop\virt\flag"
string_to_replace = '0x'
replacement_string = ''

with open(filename, 'r') as f:
    file_content = f.read()

new_content = file_content.replace(string_to_replace, replacement_string)

with open(r"C:\Users\Administrator\Desktop\virt\flag1", 'w') as f:
    f.write(new_content)