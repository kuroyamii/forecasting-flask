from setuptools import setup, find_packages

setup(
    name='forecasting-flask',
    version='1.0',
    scripts=['app.py'],
    packages= find_packages(),
    install_requires=[
        'flask',
        'flask',
        'flask_expects_json',
        'python-dotenv',
        'pandas',
        'numpy',
        'scikit-learn',
        'waitress'
    ]
)