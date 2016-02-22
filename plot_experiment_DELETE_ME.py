import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(np.arange(10))
ax.set_xlabel(r"Wavelength ($\mu$m)")
ax.set_ylabel("Luminosity (erg/s)")

ax.set_xscale('log')
ax.set_yscale('log')

model_params = {'luminosity':1,
                'rc':1,
                'rho':1,
                'eta_disk':1,
                'name':1}

if model_params is not None:
    text_string = (
        "Name: {4}\n"
        r"$L = {0}$ $L_{{\odot}} $"
        "\n"
        "$R_c = {1}$ AU\n"
        "$\\rho_1 = {2}$ g cm$^{{-3}}$\n"
        r"$\eta_{{disk}}$ = {3}"
        .format(model_params['luminosity'], model_params['rc'], model_params['rho'], model_params['eta_disk'], model_params['name'])
        )
    ax.text(0.6, 0.1, text_string, transform=ax.transAxes, fontsize=18)

plt.show()