"""
This is a (experimental) module to load data from the Fortran codes.

We're starting with the output of the "17.*" files.

"""

from __future__ import division

import os
import numpy as np
import matplotlib.pyplot as plt

import astropy.table
import astropy.units as u
import astropy.constants as c

from NC_sed_auxiliary.parse_fortran_name import parse_17_name

class SED_output(object):

    def __init__(self):
        self.table = None
        self.model_params = None

        # Put in a friendly error message to make sure nobody confuses the
        # static methods with instance methods:

        def static_warning(self, *args, **kwargs):
            err = "Invalid use of static method. Try sed=SED_output.load(file)"
            raise AttributeError(err)
        self.load = static_warning

    @staticmethod
    def load(filename):

        try:
            data = np.loadtxt(filename)
        except ValueError:

            num_lines = sum(1 for line in open(filename))

            i = 1
            while i < num_lines:
                try:
                    data = np.loadtxt(filename, skiprows=i)
                    break
                except ValueError:
                    i += 1                    

        table = astropy.table.Table()

        # the columns were defined by Nuria to me on 8 Feb, see research notes
        table['index'] = data[:,0]
        table['frequency'] = data[:,1] * u.Hz
        table['wavelength'] = data[:,2] * u.um
        table['luminosity'] = data[:,-1] * u.erg/u.s

        self = SED_output()

        self.table = table

        try: 
            absolute_path, relative_filename = os.path.split(filename)
            self.model_params = parse_17_name(relative_filename)
        except Exception, e:
            print "Failed to read model params"
            raise e

        return self

    def plot(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(self.table['wavelength'], self.table['luminosity'])
        ax.set_xlabel(r"Wavelength ($\mu$m)")
        ax.set_ylabel("Luminosity (erg/s)")

        ax.set_xscale('log')
        ax.set_yscale('log')

        if self.model_params is not None:
            text_string = (
                "Name: {4}\n"
                r"$L = {0}$ $L_{{\odot}} $"
                "\n"
                "$R_c = {1}$ AU\n"
                "$\\rho_1 = {2}$ g cm$^{{-3}}$\n"
                r"$\eta_{{disk}}$ = {3}"
                .format(self.model_params['luminosity'], self.model_params['rc'], self.model_params['rho'], self.model_params['eta_disk'], self.model_params['name'])
                )
            ax.text(0.6, 0.1, text_string, transform=ax.transAxes, fontsize=18)

        return fig