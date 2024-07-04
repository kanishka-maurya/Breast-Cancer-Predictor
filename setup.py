from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT  = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''This is code for getting the list of required modules.'''
   
    requirements = []
    with open(file_path) as req_file:
        requirements = req_file.readlines()

    requirements = [req.replace("\n","") for req in requirements]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(

        name = "Breast-Cancer-Predictor",
        version = "0.0.1",
        author = "kanishka Maurya",
        author_email = "kanishkamauryaofficial@gmail.com",
        packages = find_packages(),
        py_modules = get_requirements("requirements.txt")
)
