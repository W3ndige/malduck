# Copyright (C) 2018 Jurriaan Bremer.
# This file is part of Roach - https://github.com/jbremer/roach.
# See the file 'docs/LICENSE.txt' for copying permission.

import click

from roach import cuckoomem


@click.group()
def main():
    pass


@main.command("cuckoomem.list")
@click.argument("mempath", type=click.Path(exists=True))
def cuckoomem_list(mempath):
    with open(mempath, "rb") as f:
        p = cuckoomem.from_file(f)
        for region in p.regions:
            print "0x%08x .. 0x%08x" % (region.addr, region.addr + region.size),
            print repr(p.readv(region.addr, 16))
