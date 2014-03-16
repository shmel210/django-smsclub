from distutils.core import setup

long_description = open('README.rst').read()

setup(
    name='django-smsclub',
    version="0.0.1",
    package_dir={'smsclub': 'smsclub'},
    packages=['smsclub'],
    description='Django smsclub gateway integration',
    author='shmel',
    author_email='alecranon@gmail.com',
    license='BSD License',
    url='https://github.com/shmel210/django-smsclub.git',
    platforms=["any"],
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Environment :: Web Environment',
    ],
)