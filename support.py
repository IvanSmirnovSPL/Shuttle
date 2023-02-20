from dataclasses import dataclass


@dataclass
class Commands:
    first_motor: float
    second_motor: float
    third_motor: float


@dataclass
class Sensors:
    error: float


@dataclass
class Settings:
    time_tick: float
    initial_state: Commands
