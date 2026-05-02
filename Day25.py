##📅 Day 25 – Advanced Process Handling (Multiple Processes & Pipes)
'''
From your roadmap :

✅ Run multiple processes
✅ Connect processes (pipes)
✅ Build complex workflows'''

"""ps aux | grep python | sort
Command A → Command B → Command C
"""

"""import subprocess

p1 = subprocess.Popen(["ps","aux"], stdout = subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","python"],stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

p3 = subprocess.Popen(["sort"],stdin=p2.stdout,stdout=subprocess.PIPE,text= True)

output = p3.communicate()[0]

print(output)"""


#🔄 6. Real-Time Multi Process Flow

"""import subprocess

p1 = subprocess.Popen(["df","-h"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","/"], stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

for line in p2.stdout:
    print("Filtered:",line.strip())"""


##🔄 6. Real-Time Multi Process Flow
"""
import subprocess

p1 = subprocess.Popen(["df","-h"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","/"], stdin=p1.stdout,stdout=subprocess.PIPE,text=True)

process = p2.communicate()[0]

print(process)"""


import subprocess

p1 = subprocess.Popen(["ps","aux"],stdout=subprocess.PIPE,text=True)

p2 = subprocess.Popen(["grep","python"],stdin = p1.stdout, stdout = subprocess.PIPE,text=True)

p3 = subprocess.Popen(["sort"], stdin = p2.stdout, stdout = subprocess.PIPE, text = True)

output = p3.communicate()[0]

print(output)
