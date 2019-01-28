#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import sensor_msgs.msg
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist


threshold = 1.5
linx = 0.4  
angz = 0.0

class Robot:

    # creating a dictionary to collect sensor values
    ranges = {}
    
    # the dictionary contains 8 elements corresponding to the 8 sensors
    for i in range(8):
        ranges[i] = None
    
    # creating a puclisher for the topic /cmd_vel
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    def __init__(self):
        print ("created object")

    # defining 8 callback functions, one for each sensor
    def callback(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range0 = data.range
        self.ranges[0] = range0
        print ("in 0")
    def callback1(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range1 = data.range
        self.ranges[1] = range1
        print ("in 1")
    def callback2(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range2 = data.range
        self.ranges[2] = range2
        print ("in 2")
    def callback3(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range3 = data.range
        self.ranges[3] = range3
        print ("in 3")
    def callback4(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range4 = data.range
        self.ranges[4] = range4
        print ("in 4")
    def callback5(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range5 = data.range
        self.ranges[5] = range5
        print ("in 5")
    def callback6(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range6 = data.range
        self.ranges[6] = range6
        print ("in 6")
    def callback7(self, data):
        if len(self.ranges) > 8:
            self.ranges = {}
        # recording sensor values to the dictionary
        range7 = data.range
        self.ranges[7] = range7
        print ("in 7")
        
        # modifying the dict as per the threshold for the proximity of obstacle
        l = range(len(self.ranges))
        for i in l:
            if self.ranges[i] > threshold:
                self.ranges [i] = 1
            else:
                self.ranges[i] = 0

    
        # call the navigate function
        self.navigate(self.ranges)

    def listener(self):

        # creating a listener 
        rospy.init_node('listener', anonymous=True)

        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # subscribing to the 8 topics corresponding to the 8 sensor values
        print ("calling 0")
        rospy.Subscriber('scan',  Range, self.callback)
        print ("calling 1")
        rospy.Subscriber('scan1', Range, self.callback1)
        print ("calling 2")
        rospy.Subscriber('scan2', Range, self.callback2)
        print ("calling 3")
        rospy.Subscriber('scan3', Range, self.callback3)
        print ("calling 4")
        rospy.Subscriber('scan4', Range, self.callback4)
        print ("calling 5")
        rospy.Subscriber('scan5', Range, self.callback5)
        print ("calling 6")
        rospy.Subscriber('scan6', Range, self.callback6)
        print ("calling 7")
        rospy.Subscriber('scan7', Range, self.callback7)
    
        self.ranges = {}
        # to keep python from exiting until this node is stopped
        rospy.spin()

    def navigate(self, ranges):
        print ("in navigate")
        global linx
        global angz
        rate = rospy.Rate(10) # 10hz
        
        a = ranges[0]
        b = ranges[2]
        c = ranges[3]

        # checking the presence of obstacles
        if (a==0 or b==0 or c==0):
            # stop and rotate robot till there is no obstacle 
            linx = 0.0
            angz = 0.5
        else:
            linx = 0.4
            angz = 0

        command = Twist()
        command.linear.x = linx
        command.angular.z = angz
        self.pub.publish(command)
        rate.sleep()

def main():
    r2d2 = Robot ()
    print ("in main")
    r2d2.listener()

if __name__ == '__main__':
    main()
