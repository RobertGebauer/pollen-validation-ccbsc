from setuptools import find_packages, setup
setup(
    name='ccbsc-api',
    packages=find_packages(),
    version='0.0.4',
    description='Framework to apply new algorithms on images of pollen.',
    author='Robert Gebauer',
    url="https://github.com/RobertGebauer/pollen-validation-ccbsc",
    license='MIT',
    platforms=["any"],

    install_requires= [
        "pillow == 8.0.1"
    ]
)
