# egh_80_iol_n
ROS integration for [SCHUNK EGH 80-IOL-N](https://schunk.com/de/de/greiftechnik/parallelgreifer/egh/egh-80-iol-n-urek-starter/p/000000000001478176) gripper.

## Prerequisites


## How to setup
Clone the _egh_80_iol_n_ package into your catkin workspace.
In _egh_80_iol_n_service.py_ , set the IP-adress of your gripper.
Build and source your workspace.

## How to run
run the gripper node with
```bash
rosrun egh_80_iol_n egh_80_iol_n_service.py
```
or inside your custom launch file.

## How to use
Inside custom python script
```python
from egh_80_iol_n.srv import set_position, grip

# call grip service
grip_srv = rospy.ServiceProxy("egh_80_iol_n/grip", grip)
grip = grip()
grip.force = 4
grp_response = grip_srv(grip)

# call set_position service
pos_srv = rospy.ServiceProxy("egh_80_iol_n/set_position_service", set_position)
position = set_position()
position.position = 50 # percentage of max. stroke (0: closed, 100: opened)
pos_response = pos_srv(position)
```


## ToDo
- [ ] create launch file with args