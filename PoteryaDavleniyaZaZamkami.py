import sys
import RashodQr as RQ
from UBTS10 import dn
from math import pi


def uchastokZa(t0,p,dn,):
	VkKr=25*((t0/p)**0.5)
	QkKr=pi/4*((D**2)-(dm**2))*VkKr
    Pkmm=(8*(Q**2)*p/(((pi**2)*((D**2)-(dm**2)))**2))*(1.25+(((D**2)-(dm**2))/((D**2)-(dn**2)))*(0.75*(((D**2)-(dm**2))/((D**2)-(dn**2)))-2))
	Pk=(((128*Q*n*lm)/(pi*((D-dm)**3)*(D+dm)))+(16*t0*lm)/(3(D-dn))+Pkmm)*e/lo