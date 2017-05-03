import subprocess, shlex


folder_path = "/home/local/ASUAD/jchakra1/jaydeep/software/cplus2asp-3-1_x86_64/bin/"
sw = "cplus2asp"
in_file = "adaptiveSystem"
out_file = "out.txt"

def cmdLine():
	command = [folder_path+sw,folder_path+in_file,folder_path+'query','query=0']#,folder_path+out_file]
	#command = folder_path+sw+" "+ folder_path+in_file
	#command = ['vi','out.txt']
	print(command)
	p = subprocess.Popen(command , stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
	out, err = p.communicate()
	f = open('out.txt','wb')
	f.write(out)
	print(out)