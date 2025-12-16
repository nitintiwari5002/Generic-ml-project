# Used so as to create the code as a package and deploy it for other people to use

from setuptools import find_packages, setup
from typing import List

a = '-e .'
def get_requirements(file_path:str)->List:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if a in requirements:
            requirements.remove(a)

    return requirements        

setup(
    name="ml_project",
    version="0.0.1",
    author="Nitin",
    author_email="nitin.tiwari.5002@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)