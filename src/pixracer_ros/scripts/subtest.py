#!/usr/bin/python

import rospy
from mavros_msgs.msg import Mavlink, State
import pyttsx

prev = False
prev_mode = ''

def speech_arm(isArmed):
  global prev
  if isArmed != prev:
    tts = pyttsx.init()
    prev = isArmed
    msg = "armed." if isArmed else "disarmed."
    tts.say(msg)
    tts.runAndWait()

def speech_mode(mode):
  global prev_mode
  if mode != prev_mode:
    prev_mode = mode
    tts = pyttsx.init()
    tts.say(mode)
    tts.runAndWait()

def mav_callback(data):
  pass
  #rospy.loginfo(type(data))
  #rospy.loginfo(data.sysid)

def state_callback(data):
  print("connected:{0} armed:{1} guided:{2} mode:{3}".format(data.connected, data.armed, data.guided, data.mode))
  speech_arm(data.armed)
  speech_mode(data.mode)

if __name__ == '__main__':
  rospy.init_node('subtest')
  rospy.Subscriber('mavlink/from', Mavlink, mav_callback)
  rospy.Subscriber('mavros/state', State, state_callback)
  rospy.spin()
