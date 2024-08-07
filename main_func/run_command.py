import subprocess


async def run_command(command):
    try:

        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout

    except subprocess.CalledProcessError as e:

        return e.stderr
