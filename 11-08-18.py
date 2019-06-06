"""

import subprocess
subprocess.call("dir",shell=True)
# import paramico
# for Linux
c = subprocess.Popen("grep -rin a",stdin=open("a.out"),stdout=open("imp1","w"),shell=True)

"""
def process():
    import subprocess
    import time
    while True:
        subprocess.call("tasklist",shell=True)
        time.sleep(10)

def main():
    process()

if __name__ == '__main__':
    main()

