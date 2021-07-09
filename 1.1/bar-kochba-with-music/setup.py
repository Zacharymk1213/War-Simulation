import cx_Freeze

executables = [cx_Freeze.Executable("bar-kochba-game.py")]

cx_Freeze.setup(
    name="Bar Kochba was his name",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["music.mp3"]}},
    executables = executables

    )
