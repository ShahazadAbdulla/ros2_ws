import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    #get the path to the launch files
    publisher_launch_file = os.path.join(get_package_share_directory('publisher'), 'launch', 'publisher_launch.py')
    subscriber_launch_file = os.path.join(get_package_share_directory('subscriber'), 'launch', 'subscriber_launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource(publisher_launch_file)),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(subscriber_launch_file)),
    ])