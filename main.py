from simulation import Simulation
from control_system import ControlSystem
from support import Settings, Commands

initial_state = Commands(0, 0, 0)
settings = Settings(1, initial_state)

simulation = Simulation(_settings=settings)
control_system = ControlSystem(settings)

commands = initial_state
while(True):
    sensors = simulation.tick(commands)
    commands = control_system.tick(sensors)

