# Collision-Avoidance-Robot
A reactive collision avoidance robot simulation on Gazebo
Youtube video link - https://youtu.be/1MVq4iFitB4

The collision avoidance robot is created using Python on ROS and Gazebo was used for the simulation. Listener.py is the python script to carry out the obstacle avoidance behavior and collision_avoidance.urdf is the urdf file created for my robot. The video shows the avoidance as well as the relative rotation, translation and absolute position on the terminal window

I have used a Roomba looking robot with 8 Hokuyo laser sensors attached at 45 degrees on the body of the robot. There are 2 wheels and a castor wheel to the robot. It drives around using a differential drive mechanism. The lasers have a horizontal FoV of 11.45 degrees.

The world contains of different kind of obstacles like walls, spheres, barricades, cylinders, etc.

The obstacle avoidance strategy :
1. Move robot with constant linear velocity in x-direction and scan from sensors 1 to 8 
2. Get the Euclidean distances onto a python dictionary
3. Threshold the dictionary of sensor values as per the defined threshold (1m)
4. If there is an obstacle in the 3 frontal sensors:
    a. Stop the linear motion
    b. Rotate robot around z axis
    c. Continue rotation till there are no obstacles in the front
    d. Resume constant velocity linear motion
5.Repeat from step 1 

The robot successfully navigates obstacles. It is also found to successfully avoid spherical obstacles but gets stuck on table edges.

1. Clone the project files onto a new directory within your catkin workspace 
    mkdir ~/catkin_ws/src/Obstacle_Avoidance_ROS
    cd ~/catkin_ws/src/Obstacle_Avoidance_ROS
    git clone https://github.com/akshay-iyer/Collision-Avoidance-Robot
    cd ~/catkin_ws
    catkin_make
2. Launch ROS CORE in a new terminal
    roscore 
3. Launch the Gazebo simulation in a new terminal window
    roslaunch Obstacle_Avoidance_ROS testbot_gazebo.launch
4. Run the python script in a new terminal
    rosrun Obstacle_Avoidance_ROS listener.py
    
The python code is well commented and can be easily followed along with the algorithm above

Happy Coding!


        

The simulator packages have been  based on https://github.com/vibhuthasak/Obstacle_Avoidance_ROS


