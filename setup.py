from setuptools import setup, find_packages

setup(
    name="warzone-battle-of-cards",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.5.0",
    ],
    entry_points={
        "console_scripts": [
            "warzone=src.main:main",
        ],
    },
)
