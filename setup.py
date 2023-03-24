from setuptools import setup, find_packages
import subprocess

# get current git commit sha
commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()

setup(
    name="echoai-dev",
    version=f"0.1.0+{commit_sha[:5]}",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "echoai=echoai.main:main",
        ],
    },
    install_requires =[
        "openai",
        "pygments"
    ]
)