import paramiko
import time


def connect_ssh(host, user, pswd):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host,
                username=user,
                password=pswd)

    return ssh


def read_initial_output(chan):
    output = ""
    while True:
        if chan.recv_ready():
            output += chan.recv(1024).decode('utf-8')
        else:
            break
        time.sleep(0.1)
    return output


def run_interactive_session(ssh_entity):

    channel = ssh_entity.invoke_shell()
    channel.settimeout(0.0)

    initial_output = read_initial_output(channel)
    print(initial_output, end='')

    try:

        while True:
            command = input()
            if command.lower() == '?exit':
                break

            channel.send(command + '\n')
            time.sleep(0.3)

            while True:

                if channel.recv_ready():

                    output = channel.recv(1024).decode('utf-8')

                    print('\n'.join(output.split('\n')[1:]), end='')

                    if output.strip().endswith(('>>>', '$', '#', '>')):
                        break

                time.sleep(0.1)

    except KeyboardInterrupt:

        print("Close session")

    channel.close()


if __name__ == "__main__":

    hostname = "hostname"
    username = "username"
    password = "password"

    object_ssh = connect_ssh(hostname, username, password)
    run_interactive_session(object_ssh)
    object_ssh.close()
