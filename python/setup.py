from setuptools import setup
import platform


setup(name="ict-messaging",
      maintainer="The OBNL Team",
      maintainer_email="gillian.basso@hevs.ch",
      url="https://github.com/IntegrCiTy/messaging",
      version="0.10.1",
      platforms=[platform.platform()],  # TODO indicate really tested platforms

      packages=["ict.protobuf"],
      install_requires="protobuf",

      # metadata

      description="Messaging for OBNL and IntegrCiTy",

      license="Apache License 2.0",

      keywords="Protobuf",

      classifiers=["Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: Apache License 2.0",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.5",
                   "Topic :: Software Development :: Code Generators",
                   "Topic :: Utilities"],
      zip_safe=False
      )
