from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    package_data={'saicinpainting': ["models/*/*.mat", "models/*/*.csv", "models/*/*.pth"]}
)
