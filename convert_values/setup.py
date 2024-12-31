# setup.py

from setuptools import setup, find_packages

setup(
    name='convert_values',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add dependencies if any
    description='A module for converting values to their correct types.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/convert_values',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Set the required Python version
)
