#!/usr/bin/python

import os
import rospy
from mavros_msgs.srv import SetMode, CommandBool

path = "/home/kawamura/missions"

def handle_mission(file):
  mode = SetMode()
  mode.base_mode = 0
  mode.custom_mode = 'GUIDED'
  setmode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
  setmode(0, 'GUIDED')
  # arm
  armsrv = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
  armsrv(True)

def mission_monitor():
  try:
    while not rospy.is_shutdown():
      files = os.listdir(path)
      for file in files:
        if file == "auto.mission":
          handle_mission(file)
  except IOError:
    rospy.logger("monitor error")
  

if __name__ == '__main__':
  rospy.init_node('pubtest')
  mission_monitor()
  rospy.spin()
