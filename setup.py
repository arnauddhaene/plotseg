import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='plotseg',
     version='0.1',
     author="Arnaud Dhaene",
     author_email="arnaud.dhaene@epfl.ch",
     description="Plotting tool for brain atlases, in Python.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/arnauddhaene/plotseg",
     packages=setuptools.find_packages(),
     include_package_data=True,
     install_requires=['numpy', 'pandas', 'plotnine'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )