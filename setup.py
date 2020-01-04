import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='django-gaston',
    version='0.0.5',
    author='Hyde Tek',
    description='A django menu generator',
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
