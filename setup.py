import setuptools
import os

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='pygwbl',
    version='1.9',
    py_modules=['pygwbl'],  # 这个要跟发布的模块名一致
    author='Dagwbl',
    author_email='Dagwbl@qq.com',
    url='https://github.com/Dagwbl/pygwbl',
    project_urls={
        "Bug Tracker": "https://github.com/Dagwbl/pygwbl/issues",
    },
    description="Dagwbl's personal tool set.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    )
