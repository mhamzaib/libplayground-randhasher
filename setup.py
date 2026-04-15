from setuptools import setup, find_packages

setup(
    name='randhasher', 
    version='0.2.0',
    description='Generates structured tables of multiple hash types from a single input',
    author='mhamzaib'
    url='https://github.com/mhamzaib/libplayground-randhasher'
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'randhasher=randhasher.__main__:main',
        ],
    },
    python_requires='>=3.7',
)