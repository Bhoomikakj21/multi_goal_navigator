cmake_minimum_required(VERSION 3.0.2)
project(multi_goal_navigator)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  turtlesim
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/multi_goal_navigator.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
