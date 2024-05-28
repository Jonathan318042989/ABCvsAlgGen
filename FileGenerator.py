import subprocess

#AG
""" arg1 = {"1", "2"}
for i in range(30):
    for f in arg1:
        subprocess.run(['python', 'AG.py', f, str(i+1)])
 """        
#ABC
arg1 = {"1", "2"}
for i in range(30):
    for f in arg1:
        subprocess.run(['python', 'ABC.py', f, str(i+1)])