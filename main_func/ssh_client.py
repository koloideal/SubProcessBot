import asyncio
import re

from aiogram import types
import paramiko
import html


async def connect_ssh(host, port, user, pswd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(hostname=host,
                username=user,
                password=pswd,
                port=port,
                look_for_keys=False,
                allow_agent=False)

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

            await asyncio.sleep(0.5)

            if channel.recv_ready():

                output = channel.recv(1024).decode('utf-8')

                output = html.escape('\n'.join(output.split('\n')[1:-1]))

                output = re.sub('(\\[\\d{1,2};\\d{1,2}m)|(\\[\\dm)|(\\[\\?2004l)', '', output)

                output = output.strip()

                print(output, end='')

                if output:

                    await message.answer(f"<code>bash</code>"
                                         f"<pre>{output}</pre>",
                                         parse_mode='HTML', end='')
                else:

                    await message.answer(f'<pre>{html.escape(">>>")}</pre>',
                                         parse_mode='HTML')

                if output.strip().endswith(('>>>', '$', '#', '>', ':')):
                    break
            else:

                break

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
