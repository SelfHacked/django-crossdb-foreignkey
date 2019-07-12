from setuptools import setup, find_packages


extra_test = [
    'pytest>=4',
    'pytest-runner>=4',
    'pytest-cov>=2',
    'pytest-django>=3',
    'psycopg2',
]
extra_dev = extra_test

extra_ci = extra_test + [
    'python-coveralls',
]

setup(
    name='django-crossdb-foreignkey',

    version='0.1.0',

    python_requires='>=3.6',

    install_requires=[
        'Django>=2',
    ],

    extras_require={
        'test': extra_test,
        'dev': extra_dev,
        'ci': extra_ci,
    },

    packages=find_packages(),

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Varuna Bamunusinghe',
    author_email='varuna@selfdecode.com',
)
