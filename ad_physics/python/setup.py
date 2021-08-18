import sys

from setuptools import setup
from setuptools.command.install import install as _install
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(self):
        return True


class Install(_install):
    def finalize_options(self):
        _install.finalize_options(self)
        if self.distribution.has_ext_modules():
            self.install_lib = self.install_platlib

programming_language_classifier = "Programming Language :: Python :: {}".format(sys.version_info.major)

setup(
    name="ad-physics",
    packages=["ad_physics"],
    package_dir={"": sys.argv.pop(-1)},
    package_data={"ad_physics": ["*.so"]},
    version="2.4.7",
    author='CARLA Simulator Team',
    author_email='carla.simulator@gmail.com',
    license="MIT",
    classifiers=[
        programming_language_classifier,
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://ad-map-access.readthedocs.io/en/latest/",
    description="python binding of the C++ library for Automated Driving physics data types",
    long_description="*ad-physics* provides the python binding of a C++ implementation for common data types to be used in the context of automated driving (AD).\
This includes type safe implemenations of e.g. Distance, Speed, Duration and Acceleration and operations on those.\
In addition, the types define AD specific precision, minima, maxima and input range values.\
\
See [project webpage](https://ad-map-access.readthedocs.io/en/latest/) or [doxygen docu](https://ad-map-access.readthedocs.io/en/latest/ad_physics/apidoc/html/index.html) for a full interface description.",
    long_description_content_type="text/markdown",
    distclass=BinaryDistribution,
    cmdclass={'install': Install}
)
