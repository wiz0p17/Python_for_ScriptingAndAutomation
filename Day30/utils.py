import time

from commands import runCommand

output = ""

def retry_logic(cmd,retry = 3):
    for attemps in range(retry):
        try:
            result = runCommand(cmd)

            return result
        
        except Exception as e:
            time.sleep(2)
            attemps = attemps + 1
            output = "An error occoured"+str(attemps)

    return output
        
    

            