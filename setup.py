from setuptools import find_packages, setup
from typing import List

# This function returns the list of requirements..
def get_package_requirements()->List[str]:
    req_list = []
    with open("requirements.txt", "r") as f:
        req_list = f.readlines()

    req_list = [line.rstrip('\n') for line in req_list]
    req_list = req_list[:-1]
    print("Packages from requirements.txt file: ", req_list)
    
    return req_list

setup(
    name = "sensor",
    version="0.0.1",
    author="venunitt-ds",
    author_email="venuplla@gmail.com",
    packages=find_packages(),
    install_requires=get_package_requirements(),        #["pymongo==4.2.0"],

)
