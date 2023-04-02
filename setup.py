from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='kraken-wsclient-py',
      version='0.0.8',
      description='Sample Kraken WebSockets client',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/krakenfx/kraken-wsclient-py',
      author='Kraken',
      author_email='engineering@kraken.com',
      license='MIT',
      packages=['kraken_wsclient_py'],
      python_requires='>=3',
      install_requires=[
          'asn1crypto==0.24.0',
          'attrs==^19.2.0',
          'autobahn==20.12.3',
          'Automat==^0.8.0',
          'cffi==1.14.0',
          'constantly==15.1.0',
          'cryptography==3.3.2',
          'hyperlink==^20.0.1',
          'idna==2.8',
          'incremental==21.3.0',
          'pyasn1==0.4.5',
          'pyasn1-modules==0.2.3',
          'pycparser==2.19',
          'PyHamcrest==1.9.0',
          'pyOpenSSL==18.0.0',
          'service-identity==18.1.0',
          'six==1.12.0',
          'Twisted==22.4.0',
          'txaio==18.8.1',
          'zope.interface==4.6.0',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      keywords='kraken websockets',
      zip_safe=False)
