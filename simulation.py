from support import Commands, Sensors, Settings


class Simulation:
    def __init__(self, _settings: Settings):
        self.settings = _settings

    def tick(self, commands: Commands) -> Sensors:
        self.change_model(commands)
        self.compute_model()
        sensors = self.form_sensors()
        return sensors

    def change_model(self, commands: Commands) -> None:
        pass

    def compute_model(self) -> None:
        pass

    def form_sensors(self) -> Sensors:
        pass
