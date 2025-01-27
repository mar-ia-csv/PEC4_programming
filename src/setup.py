from setuptools import setup, find_packages

setup(
    name="PEC4_Maria",
    version="1.0.0",
    description="Analysis of cyclist data using Python",
    author="Maria Femenias Hermida",
    author_email="mfemeniash@uoc.edu",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "matplotlib",
        "Faker"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.8',
)
