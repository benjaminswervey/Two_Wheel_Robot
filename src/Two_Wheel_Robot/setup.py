from setuptools import setup

package_name = 'Two_Wheel_Robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='benjamin',
    maintainer_email='benjaminservey@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
      'talker = Two_Wheel_Robot.publisher_member_function:main',
      'listener = Two_Wheel_Robot.subscriber_member_function:main',
      'encoder_reader = Two_Wheel_Robot.Encoder_Reader:main',
      'encoder_counter = Two_Wheel_Robot.Encoder_Counter:main'
      
        ],
    },
)
