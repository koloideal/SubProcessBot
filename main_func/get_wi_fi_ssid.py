import re
import subprocess
import platform


def get_ssid():
    os_name = platform.system()

    if os_name == "Windows":
        result = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True)
        output = result.stdout.decode('utf-8', errors='ignore')

        for line in output.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
                return ssid
        return None

    elif os_name == "Linux":
        result = subprocess.run(["/sbin/iwgetid", "-r"], capture_output=True)
        ssid = result.stdout.decode('utf-8', errors='ignore').strip()
        return ssid

    else:
        raise NotImplementedError(f"OS '{os_name}' is not supported.")
