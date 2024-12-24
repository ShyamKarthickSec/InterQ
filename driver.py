import subprocess

def get_tool_info():
    command = input("Enter the tool/command that needs to be ran along with the input: ")
    return command

def parse_input():
    print("Enter the list of inputs that needs to be concurrently executed along with the above command.")
    in_file = input("Enter the full file Path: ")
    return in_file

if __name__ == "__main__":
    cmd = get_tool_info()
    in_file = parse_input()
    with open(in_file,'r') as infile:
        arg2 = infile.readlines()
    for i in arg2:
        powershell_command = cmd + ' ' + i
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", powershell_command],
            capture_output=True,
            universal_newlines=True)
        print(result)

    


