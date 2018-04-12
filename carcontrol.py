import sys, time
import rospy
import numpy as np
from rc_node.msg import car_input
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped

class CarControl:

    def __init__(self):
        #Publish the car input data
        self.car_pub = rospy.Publisher("car_input", car_input, queue_size = 10)

        #For moving the rc car at fixed velocity
        # elapsed_time = 0.0
        # start_time = time.time()
        # while elapsed_time < 1.5:
        # 	elapsed_time = time.time() - start_time
        # 	Z = car_input()
        # 	Z.steer_angle = 0
        # 	Z.power = 0.5
        # 	print "publishing"
        # 	self.car_pub.publish(Z)

        #Subscribing to position data from vicon 
        self.vicon_sub = rospy.Subscriber("/vrpn_client_node/rc_car/pose", PoseStamped, self.callback, queue_size = 10)

        text = raw_input("Start vehicle motion? (Y/n)")
        if text  == 'n':
            print "No demo recorded"
        else:
            self.move()

    def callback(self,data):
        self.pos = data.pose.position
        self.coordinates = np.append(self.coordinates, np.matrix([self.pos.x, self.pos.y, self.pos.z]), axis=0)
        np.savetxt("src/py_test/data.csv", self.coordinates, delimiter=",")

    def move(self):
        Z.steer_angle = 0
        Z.power = 0.5
        self.car_pub.publish(Z)

def main(args):
    rospy.init_node('CarControl', anonymous=True, disable_signals=True)
    print "here"
    cc = CarControl()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print ("Shutting down")

if __name__ == '__main__':
main(sys.argv)