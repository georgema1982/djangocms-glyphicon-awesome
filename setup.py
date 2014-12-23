from setuptools import setup, find_packages


setup(
    name="djangocms-glyphicon-awesome",
    version="0.1.0",
    url='http://github.com/georgema1982/djangocms-glyphicon-awesome',
    license='MIT',
    description="A plugin to incorporate Glyphicon and Font Awesome into djangocms-text-ckeditor",
    long_description=open('README.rst').read(),
    author='George Ma',
    author_email='george.ma1982@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe=False,
)
