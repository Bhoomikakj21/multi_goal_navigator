# Multi Goal Navigator

This ROS package moves the turtle in **Turtlesim** through a series of **(x, y)** waypoints using **proportional control**.

---

## How to Run

```bash
roscore
rosrun turtlesim turtlesim_node
roslaunch multi_goal_navigator navigate.launch
```

---

## Dependencies

- rospy  
- turtlesim  
- geometry_msgs  
- std_msgs
