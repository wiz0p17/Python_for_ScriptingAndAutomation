##Advanced Subprocess (Pipes & Chaining)

#Method 1 (Simple but Less Safe)

import subprocess

'''result = subprocess.run("ps aux | grep python3",shell=True,capture_output=True,text=True)

print(result.stdout)'''

'''p1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","python3"],stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

output = p2.communicate()[0]

print(output)'''


#Chaining Multiple Commands

'''p1 = subprocess.Popen(["df","-h"],stdout = subprocess.PIPE,text = True)

p2 = subprocess.Popen(["grep","/"],stdin = p1.stdout, stdout = subprocess.PIPE,text=True)

output = p2.communicate()[0]

print(output)


#Capture & Process Output

for line in output.splitlines():
    print("filtered ",line )'''


#Mini Practice (DO THIS)

"""👉 Find Python processes:"""

'''p1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","python3"],stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

output = p2.communicate()[0]

print(output)'''


#Real Automation Script

import subprocess

p1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","python3"],stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

outupt = p2.communicate()[0]


if outupt:
    print("\nPython Process Running")
    print(outupt)
else:
    print("No python Process Found")


