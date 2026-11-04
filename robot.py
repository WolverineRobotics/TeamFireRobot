import wpilib
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


    def teleopPeriodic(self):
        left_stick_inputX = self.controller.getLeftX()
        right_stick_inputX = self.controller.getRightX()
        left_stick_inputY = self.controller.getLeftY()
        right_stick_inputY = self.controller.getRightY()

        if (left_stick_inputY != 0):
            self.top_left_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, left_stick_inputY * 0.25)
            self.top_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, left_stick_inputY * 0.25)
            self.bottom_left_motor.set(phoenix5.VictorSPXControlMode.PercentOutput, left_stick_inputY * 0.25)
            self.bottom_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, left_stick_inputY * 0.25)

        if (right_stick_inputX != 0):
            self.top_left_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, right_stick_inputX * 0.25)
            self.top_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, right_stick_inputX * -0.25)
            self.bottom_left_motor.set(phoenix5.VictorSPXControlMode.PercentOutput, right_stick_inputX * 0.25)
            self.bottom_right_motor.set(phoenix5.TalonSRXControlMode.PercentOutput, right_stick_inputX * -0.25)




