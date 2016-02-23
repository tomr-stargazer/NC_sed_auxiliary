#!/Users/tsrice/anaconda/bin/python

"""
This is a python tool to generate a simple .png file of a given SED at the command line.

"""

from __future__ import division

import os, sys, glob

from NC_sed_auxiliary.sed_output import SED_output


def inspect_seds():

    # first let's identify what file(s) to read
    cwd = os.getcwd()

    # if there were no command line arguments passed, then do all of the 17* files.
    if len(sys.argv)<2:
        preliminary_file_list = glob.glob(os.path.join(cwd, "17*"))
        file_list = [file_ for file_ in preliminary_file_list if file_[-1] != "~"]
    else:
        preliminary_file_list = sys.argv[1:]
        file_list = [os.path.join(cwd,file_) for file_ in preliminary_file_list if ~os.path.isabs(file_)]


    for file_ in file_list:

        path, filename_without_path = os.path.split(file_)
        png_filename = filename_without_path.lstrip("17.") + ".png"

        print "Saving PNG as: {0}".format(png_filename)

        sed = SED_output.load(file_)
        fig = sed.plot()
        fig.savefig(os.path.join(cwd,png_filename))


    return file_list


if __name__ == "__main__":

    inspect_seds()
    sys.exit()
