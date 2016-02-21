"""
This is a function that parses the fortran-output filenames.

"""

from __future__ import division


def parse_17_name(filename):

    # raise NotImplemented("This code isn't implemented yet. We're still learning about regexes.")

    # example string: 17.l1.0.rho1.e-13.rc20.tsc.etad0.6.test2

    input_string = "17.l1.0.rho1.e-13.rc20.tsc.etad0.6.test2"

    # hey... let's just do a thing where we split it by dots and piece the rest together.

    split_string = input_string.split(".")

    if len(split_string) == 10:

        lum_s = split_string[1] + "." + split_string[2]
        lum = float(lum_s.lstrip("l"))
        print "Luminosity: {0}".format(lum)

    else:

        raise NotImplemented("We haven't learned how to deal with subtle cases yet")




    # pattern = re.compile("17.l(?P<luminosity>).rho(?P<rho>).rc(?P<rc>).tsc.etad(?P<etad>).(?P<name>)")

    

