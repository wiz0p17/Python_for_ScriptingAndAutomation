##“Disk Filter Tool”

'''
It should:

Run df -h
Filter output using grep
Print only relevant lines'''


import subprocess

p1 = subprocess.Popen(["df","-h"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","/"],stdin=p1.stdout,stdout=subprocess.PIPE,text = True)

output = p2.communicate()[0]

print(output)