from setuptools import setup, find_packages
setup(
    name='school',
    extras_requierd=dict(test=['pytest']),
    packages=find_packages(where='modules'),
    package_dir={"": "modules"},
)