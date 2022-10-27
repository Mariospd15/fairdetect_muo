from setuptools import setup

install_requires = [
    'shap>=0.41.0',
    'dalex>=1.4.1',
    'tabulate==0.9.0',
    'fairlearn==0.7.0',
    'matplotlib==3.6.1'
]

setup(name='fairdetect_muo',
      version='0.5',  # Development release
      description='Library to identify bias in pre-trained models!',
      url='https://github.com/manoelgadi/fairdetect',
      author='Prof. Manoel Gadi',
      author_email='mfalonso@faculty.ie.edu',
      license='MIT',
          packages=['fairdetect'],
      zip_safe=False,
      install_requires=install_requires)
