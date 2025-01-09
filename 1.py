import subprocess

command = input("type pyfile name: ")
li1 = (command+".py")

subprocess.run(["nvim", li1])
