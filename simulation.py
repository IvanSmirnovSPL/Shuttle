from support import Commands, Sensors, Settings
from pathlib import Path
import shutil
import os

class Simulation:
    def __init__(self, _settings: Settings):
        self.settings = _settings
        self.make_dir_for_render()


    def make_dir_for_render(self) -> None:
        self.initial_stl = Path(Path.cwd(), 'STL')
        self.current_stl = Path(Path.cwd(), 'STL_current')
        shutil.rmtree(self.current_stl, ignore_errors=True)
        shutil.copytree(self.initial_stl, self.current_stl)

    def tick(self, commands: Commands) -> Sensors:
        self.change_model(commands)
        self.compute_model()
        sensors = self.form_sensors()
        return sensors

    def change_model(self, commands: Commands) -> None:
        commands.first_motor = 10
        right_c = str(Path(self.current_stl, 'right.stl'))
        left_c = str(Path(self.current_stl, 'left.stl'))
        right = str(Path(self.initial_stl, 'right.stl'))
        left = str(Path(self.initial_stl, 'left.stl'))
        left_rotate = str(commands.second_motor)
        right_rotate = str(commands.first_motor)
        os.system(f'./transport {right_rotate} {right} {right_c} {right_rotate} {left} {left_c}')
        print(f'./transport {right_rotate} {right} {right_c} {right_rotate} {left} {left_c}')
    def compute_model(self) -> None:
        os.system(f'pvpython render2.py -p {self.current_stl}')

    def form_sensors(self) -> Sensors:
        return Sensors(0)
