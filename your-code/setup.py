import sys
from cx_Freeze import setup, Executable

from pygame import mixer # used on mixed, sound
import thorpy
import os
from io import BytesIO
import time
from gtts import gTTS 
#for images:
from PIL import Image 
import psutil

#base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

executables = [
        Executable("last_version.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ["pygame","os","io","time","gtts","PIL","psutil","thorpy"],
        include_files = [],
        excludes = []
)


setup(
    name = "Scape Room",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
