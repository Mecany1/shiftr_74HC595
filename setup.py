from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='shiftr_74HC595',
      version='1.0.0',
      description='Dynamic class to manage Shift Register 74HC595 in Raspberry Pi using Python',
      long_description=readme(),
      url='https://github.com/marsminds/shiftr_74HC595',
      author='marsminds',
      author_email='hello@marsminds.com',
      license='GPL-2.0',
      packages=['shiftr_74HC595'],
      install_requires=[
          'RPi.GPIO',
      ],
      zip_safe=False)
