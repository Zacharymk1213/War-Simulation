import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "include_files": ["music.mp3"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
"""if sys.platform == "win32":
    base = "Win32GUI"
"""
setup(
    name = "Bar Kochba Game",
    version = "1.2",
    description = "Can you defeat the Romans?",
    options = {"build_exe": build_exe_options},
    executables = [Executable("bar-kochba-game.py",icon="bar-kochba.ico", base=base)]
)
