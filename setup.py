from setuptools import setup, find_packages

setup(
    name = 'mypackage',
    version= '0.1',
    packages = find_packages(exclude=['test*']),
    license = 'MIT',
    description = 'EDSA example python packages',
    long_description= open('README.MD').read(),
    install_requires=['numpy'],
    url= 'https://github.com/<Jeremiahilusecsnr>/<git-practice>',
    author= '<Nwamini_Jeremiah>',
    author_email= '<jeremiahilusecsnr@gmail.com>'
)
