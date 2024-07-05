from setuptools import setup, find_packages

setup(
    name='convertisseur-de-devise',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'python 3'
    ],
    entry_points={
        'console_scripts': [
            'convertisseur = convertisseur.main:main',
        ],
    },
    author='Harold C.A. CHANWIN',
    author_email='chanwinharold@gmail.com',
    description='Convertisseur de devise en Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/...',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
