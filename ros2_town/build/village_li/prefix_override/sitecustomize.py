import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubuntu20/code/markdown/ros2_foxy/ros2_town/install/village_li'
