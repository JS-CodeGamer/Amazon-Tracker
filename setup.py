import sys, subprocess
import pkg_resources

if __name__ == "__main__":
    print("Installing requirements...")

    def install(name):
        subprocess.run(['pip', 'install', name])

    installed = {pkg.key for pkg in pkg_resources.working_set}

    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', '-q', '--upgrade', 'pip'], stdout=subprocess.DEVNULL)
    subprocess.run([python, '-m', 'pip', 'install', '-qr', 'requirements.txt'])

    print("Requirements installed.")
    print("Remember to install matching version of chtrome driver for this project.")
