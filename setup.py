import cx_Freeze

executables = [cx_Freeze.Executable("pygame_tutorial.py")]

cx_Freeze.setup(
    name="Chas's Trash Adventure",
    options={"build_exe": {"packages": ["pygame"], "included_files": ["catfood.png", "chase1.png", "chase200.png",
                                                                      "chasehover.png", "coca.png", "coffee.png",
                                                                      "frame.png", "speedup1.png", "speedup2.png",
                                                                      "speedup3.png", "speedup4.png", "speedup5.png",
                                                                      "start1.png", "start2.png", "starthover.png",
                                                                      "tampon.png", "trash.png", "warn1.png",
                                                                      "warn2.png",
                                                                      "warn3.png", "warn4.png", "warn5.png", "yum1.png",
                                                                      "yum2.png", "yum3.png", "yum4.png"]}},
    executables=executables
)
