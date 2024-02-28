from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name="geoSearch",
      version="0.0.1",
      description="Program to find close atoms according to specific geometries",
      long_description=long_description,
      long_description_content_type='text/x-rst',
      classifier=[
          "Development Status :: Alpha",
          "Topic :: Molecule Database search"
          "Intended Audience :: Researchers",
          "Licence :: MIT Licence",
          "Programin Language :: Python :: 3.11",
          ],
      keywords="Database search, Database build",
      url="https://github.com/philipullmann/DescriptorNew.git",
      author="Philip Ullmann",
      author_email="philip.ullmann@icm.uu.se",
      licence="MIT",
      packages=find_packages(),
      install_requires=["numpy", "pandas", "rdkit", "scipy"],
      entry_points={
        'console_scripts': ['geoSearch=geoSearch.geoSearch:main'],
    },
      #python_requires">=3.8",
      zip_safe=False)

