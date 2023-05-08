from setuptools import setup, find_packages

setup(
    name="videopack",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "videopack = videopack.__main__:main",
        ],
    },
    install_requires=[
        "moviepy",
    ],
)