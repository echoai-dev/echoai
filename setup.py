from setuptools import setup, find_packages

setup(
    name="echoai-dev",
    version="0.1.0",
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