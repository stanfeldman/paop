from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "paop",
    version = "0.1.0",
    author = "Stanislav Feldman",
    description = ("Python AOP framework"),
    url = "https://github.com/stanislavfeldman/paop",
    keywords = "aop",
    packages=['paop'],
    classifiers=[
        "Topic :: Software Development"
    ],
)
