import random
import time
import robot_motors
import range_finder
import robot_logging
import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="conf", config_name="config")
def main(cfg : DictConfig):
    #test_robot_movement()
    robot = robot_motors.Robot()
    robot.set_left_speed(200)
    robot.set_right_speed(200)
    #test_robot_distance(robot)  
    move_forward_until_obstacle(robot)
    

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

def move_forward_until_obstacle(robot):
    while True:
        distance = range_finder.get_range()
        if distance > 100 :
            robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))
            chosen_direction = None
            if robot.motor_state != "forward":
                robot_logging.format_logging("DEBUG", "set robot to move forward")
                robot.forward()

        else:
            if chosen_direction == None:
                chosen_direction = random.choice(["right","left","forward","backward"])
            if chosen_direction == "right":
                robot.right()
                robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))
            elif chosen_direction == "left":
                robot.left()
                robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))
            elif chosen_direction == "forward":
                robot.forward()
                robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))
            elif chosen_direction == "backward":
                robot.backward()
                robot_logging.format_logging("DEBUG", "Distance: " + str(distance) + " robot state: " + str(robot.motor_state))



def test_robot_movement():
    robot.set_left_speed(5)
    robot.set_right_speed(5)
    #robot.left()
    #time.sleep(13)
    #robot.forward()
    robot.right()
    time.sleep(13)
    #robot.backward()
    #robot.stop()

if __name__ == "__main__":
    main()