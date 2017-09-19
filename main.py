import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
T = [] # Temperature
tau = [] # Relaxation time
with open('data.txt') as textfile:
    line = next(textfile)
    print(line)
    for line in textfile:
        line = line.split(',')
        T.append(float(line[0]))
        tau.append(float(line[1]))



T = np.asarray(T)
tau = np.asarray(tau)

# Assuming Vogel-Fulcher-Tamman model of super-cooled liquid
# tau = tau0*exp(B/(T-T0))
T0 = 177.5
tau0 = 10**(-13)  # Approximate relaxation time at infinite temperature
def relaxation_time(T, B):
    global T0
    return np.exp(B/(T-T0))


popt, pcov = curve_fit(relaxation_time, T, tau)
T_space = np.linspace(T0+1, 500, 500)
fig_tau_T = plt.figure()
ax_tau_T = fig_tau_T.add_subplot(111)
ax_tau_T.plot(T, tau, '.',color='black')
ax_tau_T.plot(T_space, relaxation_time(T_space, B=500), 'r-', label='fit')
ax_tau_T.grid(which='major', color='black', linestyle='solid')
ax_tau_T.grid(which='minor', color='gray', linestyle='dashed')
ax_tau_T.set_title('Relaxation time vs temperature in super-cooled liquid')
ax_tau_T.set_xlabel('Temperature [K]')
ax_tau_T.set_ylabel('Relaxation time [s]')
ax_tau_T.set_xlim([190, 240])
ax_tau_T.set_ylim([-20, 500])
ax_tau_T.minorticks_on()

T_space = np.linspace(190, 10000, 50000)
fig_inverseT_lntau = plt.figure()
ax_inverseT_lntau = fig_inverseT_lntau.add_subplot(111)
ax_inverseT_lntau.plot(T0/T, np.log(tau/tau0), '.',color='black')
#ax_inverseT_lntau.plot([0, T0/T[1]], [np.log(tau0), np.log(tau[1])], color='black')
#ax_inverseT_lntau.plot(T0/T_space, np.log(relaxation_time(T_space, B=800)), 'r-', label='fit')
ax_inverseT_lntau.grid(which='major', color='black', linestyle='solid')
ax_inverseT_lntau.grid(which='minor', color='gray', linestyle='dashed')
ax_inverseT_lntau.set_title('Arrhenius, Strong, Fragile behaviour')
ax_inverseT_lntau.set_xlabel('1/Temperature [K]')
ax_inverseT_lntau.set_ylabel('ln(Relaxation time/tau0) [-]')
ax_inverseT_lntau.set_xlim([0, 1])
ax_inverseT_lntau.set_ylim([0, 40])
ax_inverseT_lntau.minorticks_on()
plt.show()
