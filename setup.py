from setuptools import find_packages,setup

def get_requirements():
    file_name = 'requirements.txt'
    with open(file_name) as req_file:
        req_list = req_file.readlines()
        req_list = [req_name.strip('\n') for req_name in req_list]

        remove = "-e ."
        if remove in req_list:
            req_list.remove(remove)
        
        return req_list

setup(
    naem = 'Sensor',
    version = '0.0.1',
    author = 'nv',
    author_email = 'nv220597@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
)

