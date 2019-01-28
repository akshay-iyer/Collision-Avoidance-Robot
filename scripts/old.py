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

    ranges = {}
    rangesThreshold = []
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    obstacleIndex = 0

    def __init__(self):
        print ("created object")

    def callback(self, data):
        #rospy.loginfo('Sensor 0 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range0 = data.range
        #self.ranges.append(range0)
        self.ranges[0] = range0
        #print ("ranges vector", self.ranges)
        print ("in 0")
    def callback1(self, data):
        #rospy.loginfo('Sensor 1 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range1 = data.range
        #self.ranges.append(range1)
        self.ranges[1] = range1
        #print ("ranges vector", self.ranges)
        print ("in 1")
    def callback2(self, data):
        #rospy.loginfo('Sensor 2 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range2 = data.range
        self.ranges[2] = range2
        #self.ranges.append(range2)
        #print ("ranges vector", self.ranges)
        print ("in 2")
    def callback3(self, data):
        #rospy.loginfo('Sensor 3 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range3 = data.range
        #self.ranges.append(range3)
        self.ranges[3] = range3
        #print ("ranges vector", self.ranges)
        print ("in 3")
    def callback4(self, data):
        #rospy.loginfo('Sensor 4 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range4 = data.range
        #self.ranges.append(range4)
        self.ranges[4] = range4
        #print ("ranges vector", self.ranges)
        print ("in 4")
    def callback5(self, data):
        #rospy.loginfo('Sensor 5 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range5 = data.range
        #self.ranges.append(range5)
        self.ranges[5] = range5
        #print ("ranges vector", self.ranges)
        print ("in 5")
    def callback6(self, data):
        #rospy.loginfo('Sensor 6 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range6 = data.range
        #self.ranges.append(range6)
        self.ranges[6] = range6
        #print ("ranges vector", self.ranges)
        print ("in 6")
    def callback7(self, data):
        #rospy.loginfo('Sensor 7 %s', data.range)
        if len(self.ranges) > 8:
            self.ranges = []
        range7 = data.range
        #self.ranges.append(range7)
        self.ranges[7] = range7
        #print ("ranges vector", self.ranges)
        print ("in 7")
        print ("ranges vector", self.ranges)
        l = range(len(self.ranges))
        for i in l:
            if self.ranges[i] > threshold:
                self.ranges [i] = 1
            else:
                self.ranges[i] = 0

        print ("after thresholding: ", self.ranges) 
        #self.ranges.clear()
        
        self.navigate(self.ranges)

    def listener(self):

        rospy.init_node('listener', anonymous=True)

        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

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

        print ("ranges vector", self.ranges)
        #self.ranges.clear()
        self.ranges = []
        # to keep python from exiting until this node is stopped
        rospy.spin()

    def navigate(self, ranges):
        print ("in navigate")
        global linx
        global angz
        rate = rospy.Rate(10) # 10hz
        print (ranges)

        #while not rospy.is_shutdown():
        index = 0
        a = ranges[0]
        b = ranges[1]
        c = ranges[2]

        if (a==0 or b==0 or c==0):
            
        for i in ranges:
            angz = 0
            self.obstacleIndex += 1
            print ("obstacleIndex, ",self.obstacleIndex)
            print ("checking for obstacles")
            print (ranges)
            print (i==0)
            print (self.obstacleIndex>5)
            print (i == 0 and self.obstacleIndex > 5)
            if (i == 0 and self.obstacleIndex > 5):
                print ("stopping")
                self.obstacleIndex = 0
                linx = 0.0
                angz += 1
                linx = 0.4
                break    
        print ("lin vel: ", linx)
        print ("ang vel: ", angz)
        print("sending controls")
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

# convert vector into 0s and 1s. do and/or to detect the obstacle position. use weighted vector scheme to detect obstacle position. change angular velocities by a fixed amt 