from setuptools import setup

setup(name='randhasher', 
    version = '0.1',
    description = 'Generates entire table of different types of hashes from a given input',
    url='https://github.com/mhamzaib/libplayground-randhasher',
    author='mhamzaib',
    packages=['randhasher'],
    install_requires=[
        'hashlib',
        'markdown',
    ],
    zip_safe=False)