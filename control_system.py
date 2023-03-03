from support import Commands, Sensors, Settings
from RS232 import Servos

class ControlSystem:
    def __init__(self, _settings: Settings):
        self.settings = _settings
        self.motors = Servos(
            angle1=_settings.initial_state.first_motor,
            angle2=_settings.initial_state.second_motor,
            angle3=_settings.initial_state.third_motor,
        )
        self.count = 0
        self.sign = 1

    def tick(self, sensors: Sensors) -> Commands:
        self.sign = - int(self.count / 60) if abs(self.count / 60) == 1 else self.sign
        self.count += 20 * self.sign
        commands = self.form_control(sensors)
        self.change_state(commands)
        return commands

    def form_control(self, sensors: Sensors) -> Commands:
        return Commands(0, 0, 0)

    def change_state(self, commands: Commands) -> None:
        print(commands.first_motor, commands.second_motor)
        self.motors.rotate(int(commands.first_motor), n=1)
        self.motors.rotate(int(commands.second_motor), n=2)
        self.motors.rotate(int(commands.third_motor), n=3)
