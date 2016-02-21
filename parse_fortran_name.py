"""
This is a function that parses the fortran-output filenames.

"""

from __future__ import division

import re

def parse_17_name(filename):

    raise NotImplemented("This code isn't implemented yet. We're still learning about regexes.")

    # example string: 17.l1.0.rho1.e-13.rc20.tsc.etad0.6.test2

    pattern_string = "17.l1.0.rho1.e-13.rc20.tsc.etad0.6.test2"

    pattern = re.compile("17.l(?P<luminosity>).rho(?P<rho>).rc(?P<rc>).tsc.etad(?P<etad>).(?P<name>)")

    

