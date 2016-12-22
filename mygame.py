import platform

import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from pico2d import *

import game_framework

import logo

open_canvas()

game_framework.run(logo)