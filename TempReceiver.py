# Mathias Aschhoff 2018 - 
from subprocess import check_output
import shlex

def run():
#	try:
		#cmd="sudo cometblue device -p 0 "+MAC+" get temperatures | grep Current "
		cmd="cometblue device -p 0 FB:19:25:9F:3D:BA get temperatures"
		args=shlex.split(cmd)
		process=check_output(args) 
		#out=process.decode("utf-8")
		print process
		process_split=shlex.split(process)
		print str(process_split[2])
		return
#	except:
#		print("ERROR!")
#		return "Es ist ein Fehler aufgetreten!"

run()
