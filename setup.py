from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="warzone-battle-of-cards",
    version="1.0.0",
    author="Kashaf Ahmed",
    author_email="kashaf.ahmed@example.com",
    description="A Python implementation of the card game Warzone: The Battle of Cards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kashaf12/Warzone-The-Battle-of-Cards",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=8.0.0",
    ],
    entry_points={
        "console_scripts": [
            "warzone=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "src": ["static/images/DECK/*.png"],
    },
)