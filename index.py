import os
import requests
import sys

# load version from VERSION file
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "VERSION")) as f:
    __version__ = f.read().strip()
    # convert to list of ints
    __version__ = [int(v) for v in __version__.split(".")]

# create a function which will check a github link for a VERSION file and return the version number
def check_for_updates():
    # check https://raw.githubusercontent.com/unconst/ImageSubnet/main/VERSION
    # for latest version number
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/unconst/ImageSubnet/main/VERSION"
        )
        response.raise_for_status()
        latest_version = response.text.strip()
        latest_version = [int(v) for v in latest_version.split(".")]
        print(f"Current version: {__version__}")
        print(f"Latest version: {latest_version}")
        if latest_version > __version__:
            print("A newer version of ImageSubnet is available. Downloading...")
            # download latest version with git pull
            os.system("git pull")
            # checking local VERSION
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "VERSION")) as f:
                new__version__ = f.read().strip()
                # convert to list of ints
                new__version__ = [int(v) for v in new__version__.split(".")]
                if new__version__ == latest_version:
                    print("ImageSubnet updated successfully.")
                    print("Restarting...")
                    print(f"Running: {sys.executable} {sys.argv}")
                    os.execv(sys.executable, [sys.executable] + sys.argv)
                else:
                    print("ImageSubnet git pull failed you will need to manually update and restart for latest code.")
    except Exception as e:
        print("Failed to check for updates: {}".format(e))

# check for updates
check_for_updates()