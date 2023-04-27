

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name='acm_tools',
    version='1.0.2',
    author='hhqx',
    author_email='weiwushaonian@foxmail.com',
    description='This is a package help you to run algorithm problems with acm in/out format in local python IDE .',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hhqx/acm_tools',
    project_urls={
        "Bug Tracker": "https://github.com/hhqx/acm_tools/issues"
    },
    license='MIT',
    packages=['acm_tools'],
    install_requires=requirements,
)



