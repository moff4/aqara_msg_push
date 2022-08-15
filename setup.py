import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='aqara_msg_push',
    version='1.0.2',
    author='Komissarov Andrey',
    author_email='Komissar.off.andrey@gmail.com',
    description='Aqara Message Push SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/moff4/aqara_capi',
    install_requires=[
        'pydantic>=1.9.0',
        'rocketmq-client-python>=2.0.0',
        'mapping-shortcuts>=1.1.0',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)
