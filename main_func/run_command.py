import subprocess


async def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if len(result.stdout) > 4000:
            return result.stdout[:4000]
        return result.stdout

    except subprocess.CalledProcessError as e:
        return e.stderr
