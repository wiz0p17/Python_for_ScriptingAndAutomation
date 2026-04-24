##Day 17 – Handling Output, Errors & Return Codes

import subprocess

'''result = subprocess.run(["ls","-l"],capture_output=True,text=True)


print(result.stdout)
print(result.stderr)
#print(result.returncode)'''


#Check Command Success (VERY IMPORTANT 🔥)

'''if result.returncode == 0:
    print("Command Successful")
else:
    print("Command Failed")'''




'''try:
    subprocess.run(["ls","-l"],check=True)
except subprocess.CalledProcessError as e:
    print("Command Failed: ",e)'''


try:
    subprocess.run(["ls","no_folder"],capture_output=True,text=True,check=True)

except subprocess.CalledProcessError as e:
    print("Error Occoured!")
    print(e)


#👉Safe Command Runner

import subprocess

commands = [["whoami"],["pwd"],["ls","hero"]]


for cmd in commands:
    try:
        result = subprocess.run(cmd,capture_output=True,check=True,text=True)

        print(f"\nCommand : {" ".join(cmd)}")
        print(result.stdout)

    except Exception as e:
        print(f"\nCommand Failed : {" ".join(cmd)}")
        print("Error : ",e.stderr)
