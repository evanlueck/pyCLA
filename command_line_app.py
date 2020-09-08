#!/usr/bin/python3
import os, sys
import pwd, grp
import paramiko

import click

# click context settings
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def manage():
    """
    Initiate context settings
    """

@manage.group('users')
def user_group():
    """
    users command to interact with system users.

    collection of sub commands
    """

    pass

@user_group.command('ls')
def ls():
    click.echo(list_users())

def list_users():
    users: list = []

    for u in pwd.getpwall():
        users.append(u[0])
        users.append(u[3])
        users.append(u[4])
    return users

"""

# helper function to run command and wait for output
def run(client, command):
    _, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    if exit_status != 0:
        print(stderr.read().decode('utf-8'))
        client.close()
        sys.exit(-1)
    return stdout.read().decode('utf-8')


# assuming user has sudo permission
run(client, 'sudo /usr/sbin/useradd ' + args.username + ' ' + useraddOptions)

# get home directory so we can upload ssh public key
userHome = run(client, 'eval echo ~'+args.username).strip()

# upload ssh public key
if args.key:
    sftp = client.open_sftp()
    sshDir = userHome + '/.ssh'
    authorizedKeysPath = sshDir+'/authorized_keys'
    run(client, 'sudo mkdir ' + sshDir)
    run(client, 'sudo chown ' + args.username + ' ' + sshDir)
    run(client, 'sudo chmod 700 ' + sshDir)
    tmpPath = '/tmp/' + 'authorized_keys.'+args.username
    sftp.put(args.key, tmpPath)
    sftp.put(args.key, tmpPath)
    run(client, 'sudo mv ' + tmpPath + ' ' + authorizedKeysPath)
    run(client, 'sudo chown ' + args.username + ' ' + authorizedKeysPath)
    run(client, 'sudo chmod 600 ' + authorizedKeysPath)
"""
manage()