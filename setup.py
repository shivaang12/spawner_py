from setuptools import setup

package_name = 'spawner_py'

setup(
    name=package_name,
    version='0.8.2',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Shivang Patel',
    author_email='shivaang14@gmail.com',
    maintainer='Shivang Patel',
    maintainer_email='shivaang14@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='spawner_py',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn = spawner_py.spawn:main',
        ],
    },
)
