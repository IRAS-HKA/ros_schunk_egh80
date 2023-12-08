#!/usr/bin/env python3
# license removed for brevity
import rospy
import time
import sys
from gripper import Gripper
from egh_80_iol_n.srv import set_position, grip, set_positionResponse


def handle_set_position(set_position):
    myGripper.set_position(target_position=set_position.position)
    return set_positionResponse(myGripper.get_position())

def handle_grip(grip):
    myGripper.grip(force=grip.force)

def egh_services():
    # rospy.init_node('egh_80_iol_n', anonymous=True)

    s_position = rospy.Service('egh_80_iol_n/set_position', set_position, handle_set_position)
    rospy.loginfo("egh_80_iol_n/set_position_service ready") 

    s_grip = rospy.Service('egh_80_iol_n/grip', grip, handle_grip)
    rospy.loginfo("egh_80_iol_n/grip ready")

    rospy.spin()


if __name__ == '__main__':
    myargv = rospy.myargv(argv=sys.argv)
    
    # if no ip_addr is used, print usage
    if len(myargv) < 2:
        print("usage: rosrun egh_80_iol_n egh_80_iol_n_service.py <ip_address>")
    else:
    	rospy.init_node('egh_80_iol_n')

    	myGripper = Gripper(ip_adress=myargv[1])
    	egh_services()

