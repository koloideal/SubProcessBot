import asyncio
from aiogram import types
import paramiko
import html


async def connect_ssh(host, port, user, pswd):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host,
                username=user,
                password=pswd,
                port=port)

    return ssh


async def read_initial_output(chan):

    chan.send('')

    await asyncio.sleep(0.1)

    output = chan.recv(1024).decode('utf-8')

    return output


async def run_interactive_session(message: types.Message, ssh_entity):

    channel = ssh_entity.invoke_shell()
    channel.settimeout(0.0)

    initial_output = await read_initial_output(channel)
    await message.answer(f'<code>bash</code>'
                         f'<pre>{html.escape(initial_output)}</pre>',
                         parse_mode='HTML')

    while True:
        command = input('enter')
        if command.lower() == '?exit':
            break

        channel.send(command + '\n')
        await asyncio.sleep(0.3)

        while True:

            if channel.recv_ready():

                output = channel.recv(1024).decode('utf-8')

                print('\n'.join(output.split('\n')[1:]), end='')

                await message.answer(f"<code>bash</code>"
                                     f"<pre>{html.escape('\n'.join(output.split('\n')[1:-1]))}</pre>",
                                     parse_mode='HTML', end='')

                if output.strip().endswith(('>>>', '$', '#', '>', ':')):
                    break

            await asyncio.sleep(0.1)

    channel.close()


async def ssh_client(message: types.Message,
                     host,
                     port,
                     username,
                     password):

    object_ssh = await connect_ssh(
                             host,
                             port,
                             username,
                             password)

    await run_interactive_session(message, object_ssh)

    object_ssh.close()
