#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

n = 0

def cb(message): #コールバック関数
    global n
    #n = (((1+root_five)/2)**message.data-((1-root_five)/2)**message.data)/root_five
    n = n + message.data

rospy.init_node('fibonacci')
sub = rospy.Subscriber('count_up', Int32, cb) #型はInt32
pub = rospy.Publisher('sum', Int32, queue_size=1)
#rospy.spin() #動き続ける
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()

