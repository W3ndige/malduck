# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

from roach import pe

def test_pe_header():
    img = pe("""
TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAEAAA4fug4AtAnNIbgBTM0hVGhpcyBwcm9ncmFtIGNhbm5vdCBiZSBydW4gaW4gRE9TIG1v
ZGUuDQ0KJAAAAAAAAACCixJ5xup8KsbqfCrG6nwqz5LpKsfqfCrhLBEqxOp8KuEsByrU6nwqxup9
KnjqfCoF5SEqxep8KgXlIyrH6nwqBeVzKsXqfCrPkvUq2ep8Kti46CrH6nwqz5LtKsfqfCpSaWNo
xup8KgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFBFAABMAQUAE5z9WAAAAAAAAAAA4AADAQsBCQAA
bgAAACoAAAAAAADnEAAAABAAAACAAAAAAEAAABAAAAACAAAFAAAAAAAAAAUAAAAAAAAAAJAEAAAE
AAAAAAAAAgAAgAAAEAAAEAAAAAAQAAAQAAAAAAAAEAAAAAAAAAAAAAAARIQAAMgAAAAAwAAAEAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAACAAACYAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALnRleHQAAADQ
bAAAABAAAABuAAAABAAAAAAAAAAAAAAAAAAAIAAAYC5yZGF0YQAA/hIAAACAAAAAFAAAAHIAAAAA
AAAAAAAAAAAAAEAAAEAuZGF0YQAAAGQKAAAAoAAAAAgAAACGAAAAAAAAAAAAAAAAAABAAADALmJz
cwAAAAARBwAAALAAAAAIAAAAjgAAAAAAAAAAAAAAAAAAQAAAwC5yc3JjAAAAANADAADAAAAAzAMA
AJYAAAAAAAAAAAAAAAAAAEAAAEAK
""".strip().decode("base64"))
    assert img.dos_header.e_magic == 0x5a4d
    assert img.nt_headers.Signature == 0x4550
    assert img.file_header.NumberOfSections == len(img.sections)
    assert img.sections[0].Name.strip("\x00") == ".text"
    assert img.sections[-1].get_file_offset() == 0x298
    assert img.is32bit is True
    assert img.is64bit is False
    assert img.section(".text").VirtualAddress == 0x1000
