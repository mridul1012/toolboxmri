import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.5',
    author='Mridul agrawal',
    author_email='mridul16011996@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mridul1012/toolboxmri',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    # },
    license='MIT',
    packages=['toolboxmri'],
    install_requires=['requests'],
)
