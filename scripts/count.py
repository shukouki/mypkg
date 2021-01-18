#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32 #型をインポート

rospy.init_node('count') #nodeを初期化
pub = rospy.Publisher('count_up', Int32, queue_size=1) 
rate = rospy.Rate(10) #10Hzで実行
n = 0
while not rospy.is_shutdown():
    n += 2
    pub.publish(n)
    rate.sleep()
