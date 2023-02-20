from support import Commands, Sensors, Settings


class ControlSystem:
    def __init__(self, _settings: Settings):
        self.settings = _settings

    def tick(self, sensors: Sensors) -> Commands:
        commands = self.form_control(sensors)
        self.change_state(commands)
        return commands

    def form_control(self, sensors: Sensors) -> Commands:
        pass

    def change_state(self, commands: Commands) -> None:
        pass
