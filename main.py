import time
import robot_motors
import range_finder
import robot_logging

def main():
    #test_robot_movement()

    robot = robot_motors.Robot()
    robot.set_left_speed(999)
    robot.set_right_speed(999)
    test_robot_distance(robot)  

def test_robot_distance(robot):
    while True:
        distance = range_finder.get_range()
        if distance > 100 :
            robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))
            if robot.motor_state != "forward":
                robot_logging.format_logging("DEBUG", "set robot to move forward")
                robot.forward()
        else :
            robot_logging.format_logging("DEBUG", "Distance: " + str(distance))
            if robot.motor_state != "off":
                robot.stop()

def test_robot_movement():
    robot = robot_motors.Robot() 
    robot.set_left_speed(999)
    robot.set_right_speed(999)
    #robot.left()
    #time.sleep(13)
    #robot.forward()
    robot.right()
    time.sleep(13)
    #robot.backward()
    #robot.stop()

if __name__ == "__main__":
    main()