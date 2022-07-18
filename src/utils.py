import os
from subprocess import PIPE, Popen


class Computer:
    """
    Simple class to interact with your computer
    """

    def __init__(self):
        pass

    def is_locked(self):
        """changer de langue possiblement"""
        cmd = "gnome-screensaver-command -q"
        process = Popen(cmd.split(), stdout=PIPE, stderr=PIPE)
        stdout, _ = process.communicate()
        msg = stdout.decode()
        mode = msg.split("\n")[0].split(" ")[-1]

        if mode == "actif" or mode == "active":
            return True
        else:
            return False

    def lock(self):
        """doc"""
        os.system('gnome-screensaver-command --lock')

    def unlock(self, pwd):
        """doc"""
        os.popen(
            f'xdotool key Return && xdotool type {pwd} && xdotool key Return')
