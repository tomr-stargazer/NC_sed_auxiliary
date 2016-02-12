"""
This is a (experimental) module to load data from the Fortran codes.

We're starting with the output of the "17.*" files.

"""

from __future__ import division

import numpy as np

import astropy.table
import astropy.units as u
import astropy.constants as c

class SED_output(object):

    def __init__(self):
        self.table = None

        # Put in a friendly error message to make sure nobody confuses the
        # static methods with instance methods:

        def static_warning(self, *args, **kwargs):
            err = "Invalid use of static method. Try sed=SED_output.load(file)"
            raise AttributeError(err)
        self.load = static_warning

    @staticmethod
    def load(filename):

        data = np.loadtxt(filename)
        table = astropy.table.Table()

        # the columns were defined by Nuria to me on 8 Feb, see research notes
        table['index'] = data[:,0]
        table['frequency'] = data[:,1] * u.Hz
        table['wavelength'] = data[:,2] * u.um
        table['luminosity'] = data[:,-1] * u.erg/u.s

        self = SED_output()

        self.table = table

        return self