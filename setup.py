# setup.py
from setuptools import setup

setup(
    name="md-dlp",
    version="1.0.0",
    py_modules=["md_dlp"],
    install_requires=[
        "requests>=2.25.1",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'md-dlp=md_dlp:main',
        ],
    },
)
