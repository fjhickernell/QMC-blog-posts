import setuptools
from setuptools import Extension

# define package API
packages = [
    'qmcpy',
    'qmcpy.discrete_distribution',
    'qmcpy.discrete_distribution.halton']

setuptools.setup(
    name="qmcpy",
    packages=packages,
    include_package_data=True,
    ext_modules=[
        Extension(
            name='qmcpy.discrete_distribution.c_lib.c_lib',
            sources=[
                'qmcpy/discrete_distribution/c_lib/halton_owen.c',
                'qmcpy/discrete_distribution/c_lib/MRG63k3a.c'],
            )],)
    