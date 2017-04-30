import subprocess, shlex
def cmdLine():
	cmd = shlex.split("cplus2asp adaptiveSystem query=0 > out.txt")
	p = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
	out, err = p.communicate()
	print out