#!/usr/bin/env python

"""This runs 'ls -l' on a remote host using SSH. At the prompts enter hostname,
user, and password.

$Id$
"""

import pexpect
import getpass, os, traceback

def ssh_command (user, host, password, command):

    """This runs a command on the remote host. This could also be done with the
pxssh class, but this demonstrates what that class does at a simpler level.
This returns a pexpect.spawn object. This handles the case when you try to
connect to a new host and ssh asks you if you want to accept the public key
fingerprint and continue connecting. """

    ssh_newkey = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh -l %s %s %s'%(user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_newkey, 'password: '])
    if i == 0: # Timeout
        die(child, 'ERROR!\nSSH could not login. Here is what SSH said:')
    if i == 1: # SSH does not have the public key. Just accept it.
        child.sendline ('yes')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0: # Timeout
            die(child, 'ERROR!\nSSH could not login. Here is what SSH said:')
    child.sendline(password)
    return child

def die(child, errstr):
    print errstr
    print child.before, child.after
    child.terminate()
    exit(1)

def main ():

    host = "v-sa2.nextagqa.com"#raw_input('Hostname: ')
    user = "skdeka"#raw_input('User: ')
    password = "Nextag11"#getpass.getpass('Password: ')
    child = ssh_command (user, host, password, 'mysql -e "select count(*) from click2" -ulogger -pnextag -hv-replaytest nextaglogs')

    i = child.expect([pexpect.TIMEOUT, 'Permission denied', pexpect.EOF])
    if i == 0:
        die(child, 'ERROR!\nSSH timed out. Here is what SSH said:')
    elif i == 1:
        die(child, 'ERROR!\nIncorrect password Here is what SSH said:')
    elif i == 2:
        print child.before

if __name__ == '__main__':
    try:
        main()
    except Exception, e:
        print str(e)
        traceback.print_exc()
        os._exit(1)