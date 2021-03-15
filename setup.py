import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = 'Test du tuto package'

setuptools.setup(
    name='project_api_sncf',
    version='1.0.0',
    author='Mouny',
    author_email='keomouny@simplon.com',
    url='https://github.com/keomouny',
    description='manipulation api sncf',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
        entry_points={
            'console_scripts': [
                'start_api_sncf = api_sncf.main:main'
            ],
    },
    classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ),
    python_requires='>=3.6'
)
