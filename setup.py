from setuptools import setup

dist = setup(name="covariance_diagnostic",
             author="Thomas McClintock",
             author_email="mcclintock@bnl.gov",
             description="Tool for diagnosing covariance matrices.",
             license="MIT",
             url="https://github.com/tmcclintock/covariance_diagnostic",
             packages=['covariance_diagnostic'],
             long_description=open("README.md").read()
)
