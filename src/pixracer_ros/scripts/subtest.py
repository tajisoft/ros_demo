#!/usr/bin/python

import rospy
from mavros_msgs.msg import Mavlink, State
import pyttsx

prev = False

def speech_arm(isArmed):
  global prev
  if isArmed != prev:
    tts = pyttsx.init()
    prev = isArmed
    msg = "armed." if isArmed else "disarmed."
    tts.say(msg)
    tts.runAndWait()

def mav_callback(data):
  rospy.loginfo(type(data))
  rospy.loginfo(data.sysid)

def state_callback(data):
  rospy.loginfo(type(data))
  print("connected:{0} armed:{1} guided:{2} mode:{3}".format(data.connected, data.armed, data.guided, data.mode))
  speech_arm(data.armed)

if __name__ == '__main__':
  rospy.init_node('arming')
  rospy.Subscriber('mavlink/from', Mavlink, mav_callback)
  rospy.Subscriber('mavros/state', State, state_callback)
  rospy.spin()
