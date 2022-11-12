import subprocess

def get_branch():
	proc = subprocess.Popen(('git', 'branch', '--show-current'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = (str(i, 'utf-8') for i in  proc.communicate())
	assert proc.returncode == 0, f'git branch failed with exit status {proc.returncode}: {stderr}'
	return stdout.strip()