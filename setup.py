from setuptools import setup, find_packages

setup(
    name='randhasher', 
    version='1.0.0',
    description='Generates structured hash comparison tables from a given input',
    url='https://github.com/mhamzaib/libplayground-randhasher',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'randhasher=randhasher.cli:main',
        ],
    },
    python_requires='>=3.7',
)