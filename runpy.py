import subprocess

command = input("type code name: ")
inp1 = command + ".py"

subprocess.run(["python",inp1])
