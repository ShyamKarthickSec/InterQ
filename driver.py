import subprocess
import datetime

def get_tool_info():
    command = input("Enter the tool/command that needs to be ran along with the input: ")
    return command

def parse_input():
    print("Enter the list of inputs that needs to be concurrently executed along with the above command.")
    in_file = input("Enter the full file Path: ")
    return in_file

def powershell():
    print("In powershell terminal...")
    cmd = get_tool_info()
    in_file = parse_input()
    timestamp = datetime.datetime.now().isoformat(timespec='seconds').replace(':','-')
    output_file = f"output-{timestamp}.txt"
    output = ""
    error = ""
    with open(in_file,'r') as infile:
        arg2 = infile.readlines()
    for i in arg2:
        powershell_command = cmd + ' ' + i
        result = subprocess.run(
            ["powershell", "-ExecutionPolicy", "Bypass", powershell_command],
            capture_output=True,
            text=True)
        print("The output will be printed into output.txt file as well.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return Code:", result.returncode)
        output += result.stdout 
        error += result.stderr 
    with open(output_file,'w') as outfile:
        outfile.write("Output:" + output)
        outfile.write("Errors:" + error)
    

def linux():
    print("In linux terminal...")
    cmd = get_tool_info()
    in_file  = parse_input()
    timestamp = datetime.datetime.now().isoformat(timespec='seconds').replace(':','-')
    output_file = f"output-{timestamp}.txt"
    output = ""
    error = ""
    with open(in_file,'r') as infile:
        arg2 = infile.readlines()
    for i in arg2:
        linux_terminal = cmd + ' ' + i
        result = subprocess.run(
            linux_terminal,
            shell=True,
            capture_output=True,
            text=True
        )
        print("The output will be printed into output.txt file as well.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return Code:", result.returncode)
        output += result.stdout 
        error += result.stderr 
    with open(output_file,'w') as outfile:
        outfile.write("Output:" + output)
        outfile.write("Errors:" + error)

def command_prompt():
    print("In Command Prompt...")
    cmd = get_tool_info()
    in_file  = parse_input()
    timestamp = datetime.datetime.now().isoformat(timespec='seconds').replace(':','-')
    output_file = f"output-{timestamp}.txt"
    output = ""
    error = ""
    with open(in_file,'r') as infile:
        arg2 = infile.readlines()
    for i in arg2:
        cmd_prompt = './/'+cmd + ' ' + i
        result = subprocess.run(
            cmd_prompt,
            shell=True,
            capture_output=True,
            text=True
        )
        print("The output will be printed into output.txt file as well.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        output += result.stdout 
        error += result.stderr 
    with open(output_file,'w') as outfile:
        outfile.write("Output:" + output)
        outfile.write("Errors:" + error)


if __name__ == "__main__":
    print("Select Either of the following shell/terminals in which the command needs to be executed, Give input when prompted: ")
    print("1. linux terminal\n")
    print("2. powershell\n")
    print("3. command prompt\n")
    preferred_os = input("Enter the terminal in which you would like the command to be executed: ")
    preferred_os = preferred_os.lower()
    if ((preferred_os == "linux terminal") or (preferred_os == "linux") or (preferred_os == '1')):
        linux()
    elif ((preferred_os == "powershell") or (preferred_os == '2')):
        powershell()
    else:
        command_prompt()
    

    


