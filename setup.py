from setuptools import setup, find_packages
import subprocess

# get current git commit sha
commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="echoai-dev",
    version=f"0.1.1.{commit_sha[:5]}",
    author="Fabio Dr.No Nonato",
    author_email="echoaidev@gmail.com",
    description="The command line tool to interface with Generative AI.",
    long_description=long_description,
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
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