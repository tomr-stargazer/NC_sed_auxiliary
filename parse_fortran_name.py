"""
This is a function that parses the fortran-output filenames.

"""

from __future__ import division

import os

def parse_17_name(filename):
    """
    Returns a dict of parameters extracted from a "17*" filename.

    """

    if not filename[:4] == '17.l':
        raise ValueError("`filename` must begin with '17.l'.")

    # example string: 17.l1.0.rho1.e-13.rc20.tsc.etad0.6.test2

    parameter_dict = {}

    # I feed a `1` to str.split() so it only splits on the first match
    rho_left, rho_right = filename.split(".rho", 1)

    luminosity_s = rho_left[4:]
    parameter_dict['luminosity'] = float(luminosity_s)

    rho_s, rc_right = rho_right.split('.rc', 1)
    parameter_dict['rho'] = float(rho_s)

    rc_s, tsc_right = rc_right.split('.tsc.etad', 1)
    parameter_dict['rc'] = float(rc_s)

    # the name is everything after the last period
    name = tsc_right.split('.', 1)[-1]
    parameter_dict['name'] = name

    # etadisk is everything in this last fragment before "."+name
    etadisk_s = tsc_right[:-len("."+name)]
    parameter_dict['eta_disk'] = float(etadisk_s)

    return parameter_dict
