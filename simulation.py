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
        r_v = "_".join('0.036011 0 0.0579403'.split())
        l_v = "_".join('-0.000188 0.0540462 -0.0029555'.split())
        os.system(f"./transform {str(Path(self.initial_stl, 'right.stl'))} {str(Path(self.current_stl, 'right.stl'))} {r_v} {commands.first_motor} {str(Path(self.initial_stl, 'left.stl'))} {str(Path(self.current_stl, 'left.stl'))} {l_v} {commands.second_motor}")
    def compute_model(self) -> None:
        os.system(f'pvpython render2.py -p {self.current_stl}')

    def form_sensors(self) -> Sensors:
        return Sensors(0)
