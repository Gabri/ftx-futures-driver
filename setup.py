from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = "FTX Futures driver for Jesse framework"

REQUIRED_PACKAGES = [
    'jesse'
]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='jesse-ftx-futures',
    version=VERSION,
    author="Gabri",
    author_email="stramaz.com@gmail.com",
    packages=find_packages(),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jesse.trade",
    project_urls={
        'Documentation': 'https://docs.jesse.trade',
        'Say Thanks!': 'http://jesse.trade/discord',
        'Source': 'https://github.com/Gabri/ftx-futures-driver',
        'Tracker': 'https://github.com/Gabri/ftx-futures-driver/issues',
    },
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
