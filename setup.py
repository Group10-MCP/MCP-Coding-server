import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install requirements. Please run manually: pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    install_requirements()