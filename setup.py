from setuptools import setup, find_packages
import subprocess
import shutil
import os

# added clean function
def cleanechoai():
    shutil.rmtree("dist")
    shutil.rmtree("build")
    shutil.rmtree("echoai.egg-info")

if os.path.exists("echoai.egg-info"):
    print("Removing old builds")
    cleanechoai()

# get current git commit sha
commit_sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="echoai-dev",
    version=f"0.2.0rc1",
    author="Fabio Dr.No Nonato",
    author_email="echoaidev@gmail.com",
    description="The command line tool to interface with Generative AI.",
    long_description=long_description,
    long_description_content_type='text/markdown',
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
        "pygments",
        "langchain"
    ]
)

