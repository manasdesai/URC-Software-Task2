#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int64
             
def decreasing():
    pub = rospy.Publisher('dec', Int64, queue_size=10)
    rospy.init_node('decreasing', anonymous=True)
    count=0
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
                                     
                                             
        pub.publish(count)
        rospy.loginfo(count)
        count-=1
        rate.sleep()
                                             
if __name__ == '__main__':
    try:
        decreasing()
    except rospy.ROSInterruptException:
        pass
