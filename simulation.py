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
        #os.mkdir(str(self.current_stl))
        shutil.copytree(self.initial_stl, self.current_stl)
        os.system(f"sudo chmod 777 {str(self.current_stl)}")

    def tick(self, commands: Commands) -> Sensors:
        self.change_model(commands)
        self.compute_model()
        sensors = self.form_sensors()
        return sensors

    def change_model(self, commands: Commands) -> None:
        r_c = "_".join('0.119277 0.0585911 -0.012426'.split())
        l_c = "_".join('0.119277 -0.0585911 -0.012426'.split())
        r_v = "_".join('0.000188 0.0540462 0.0029555'.split())
        l_v = "_".join('0.000188 0.0540462 -0.0029555'.split())
        right_cur = str(Path(self.current_stl, 'right.stl'))
        left_cur = str(Path(self.current_stl, 'left.stl'))
        right_init = str(Path(self.initial_stl, 'right.stl'))
        left_init = str(Path(self.initial_stl, 'left.stl'))
        os.system(f"./transform {right_init} {right_cur} {r_c} {r_v} {commands.second_motor} {left_init} {left_cur} {l_c} {l_v} {commands.first_motor}")
    def compute_model(self) -> None:
        os.system(f'pvpython render2.py -p {self.current_stl}')

    def form_sensors(self) -> Sensors:
        return Sensors(0)
