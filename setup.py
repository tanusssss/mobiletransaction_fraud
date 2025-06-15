from setuptools import setup, find_packages
from typing import List
HYPEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIREMENTS
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n" , "")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = 'Mobile_Fraud_Detection',
    version = '0.0.1',
    author= 'Tanvi',
    author_email='tanvivishwanath95@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')

)





#This file includes metadata about the package (such as name, version, author, and license) and instructions on installing it and its dependencies. 
#Here's a breakdown of what setup.py does:
#Package Configuration:
#It defines the project's metadata, including name, version, author, and license.
#Installation Instructions:
#It provides instructions on how to install the package and its dependencies.
#Command-Line Interface:
#It serves as a command-line interface for running various commands related to packaging tasks.