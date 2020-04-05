import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='django-gaston',
    version='0.2.0',
    url='https://github.com/Hyde-Tek/django-gaston/',
    author='Hyde Tek',
    description='A django menu generator',
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
)
