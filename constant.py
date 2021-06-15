#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64
         
def callback1(integer_inc):

                       
def callback2(integer_dec):
                                
                                       # In ROS, nodes are uniquely named. If two nodes with the same
                                         # name are launched, the previous one is kicked off. The
def constant():                                           # anonymous=True flag means that rospy will choose a unique
                                             # name for our 'listener' node so that multiple listeners can
                                               # run simultaneously.
    rospy.init_node('constant', anonymous=True)
    rospy.Subscriber("inc",Int64,callback1)
    rospy.Subscriber("dec",Int64,callback2)
                                             
    rospy.spin()
if __name__ == '__main__':
    constant()

    
def result():

    rospy.init_node('result',anonymous=True)
    
    sum=integer_inc+integer_dec
    
    rate = rospy.Rate(1) # 1Hz
    while not rospy.is_shutdown():
        
        rospy.loginfo(sum)                                        
        pub.publish(sum)
         
        rate.sleep()
    
                                                         # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
                                                         
if __name__ == '__main__':
    try:
        result()
    except rospy.ROSInterruptException:
        pass
