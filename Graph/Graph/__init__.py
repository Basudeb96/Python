from setuptools import setup

setup(name = "Graph_project",
    version = "0.0.4",
    author = "Basudeb Roy",
    author_email = "basudebroy82@gmail.com",
    description = ("An demonstration of Creating graph."),
    license = "BSD",
    keywords = "Graph tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],)