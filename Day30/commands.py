import subprocess

def runCommand(cmd):
    try:
        result = subprocess.run(cmd,capture_output=True,check=True,text=True)

        return result.stdout
    
    except subprocess.CalledProcessError as e:
        return("An error occoured",e)

