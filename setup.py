from setuptools import find_packages, setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="project_name",
    version="0.0.1-alpha.1",
    author="D-Bhatta",
    author_email="email",
    description="project-description",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/D-Bhatta/**repo-name**.git",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: python-version",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
