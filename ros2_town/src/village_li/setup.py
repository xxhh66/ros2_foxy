from setuptools import setup

package_name = 'village_li'

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
    maintainer='ubuntu20',
    maintainer_email='ubuntu20@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "li1_node = village_li.li1:main",
            "li2_node = village_li.li2:main",
            "li3_node = village_li.li3:main",
            # 话题发布和订阅
            "li4_node = village_li.li4:main",
            "li5_node = village_li.li5:main",
            "li6_node = village_li.li6:main",
            # 服务接口:服务端和客户端，li7是服务端，li8是客户端
            "li7_node = village_li.li7:main",
            "li8_node = village_li.li8:main",
        ],
    },
)
