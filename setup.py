from distutils.core import setup

setup(name='bdb_kafka_configuration',
      version='0.1',
      description='kafka connection',
      url='https://github.com/anjana-bijilesh/bdb_kafka_',
      download_url='https://github.com/anjana-bijilesh/bdb_kafka_/archive/refs/tags/v1.0.0.tar.gz',
      author='Anjana',
      author_email='anjana.v@bdb.ai',
      keywords=['kafka'],
      license='MIT',
      install_requires=['requests', 'confluent_kafka', 'logger', ],

      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10'
      ],
      )
