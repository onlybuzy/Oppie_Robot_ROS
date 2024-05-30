from setuptools import find_packages, setup

package_name = 'oppie_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='only_buzy',
    maintainer_email='only_buzy@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = oppie_bot.publisher:main',
            'subscriber_node = oppie_bot.subscriber:main',
        ],
    },
)
