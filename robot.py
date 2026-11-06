import wpilib
from wpilib import SmartDashboard
import phoenix5

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        self.top_left_motor = phoenix5.TalonSRX(24)
        self.top_right_motor = phoenix5.TalonSRX(6)
        self.bottom_left_motor = phoenix5.VictorSPX(26)
        self.bottom_right_motor = phoenix5.TalonSRX(28)

        self.top_right_motor.setInverted(True)
        self.bottom_right_motor.setInverted(True)

        self.controller = wpilib.XboxController(0)

        self.kV = 446.338


    def teleopPeriodic(self):
        left_stick_inputX = self.controller.getLeftX()
        right_stick_inputX = self.controller.getRightX()
        left_stick_inputY = self.controller.getLeftY()
        right_stick_inputY = self.controller.getRightY()

        left_velocity = ((left_stick_inputY * 3.5) - (right_stick_inputX * 2.5)) * 0.52
        right_velocity = ((left_stick_inputY * 3.5) + (right_stick_inputX * 2.5)) * 0.52

        left_input = left_velocity * (1 / self.kV) / 0.09
        right_input = right_velocity * (1 / self.kV) / 0.09

        SmartDashboard.putNumber("left_input", left_input)
        SmartDashboard.putNumber("right_input", right_input)

        self.top_left_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, left_input)
        self.top_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, right_input)
        self.bottom_left_motor.set(phoenix5.VictorSPXControlMode.PercentOutput, left_input)
        self.bottom_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, right_input)






