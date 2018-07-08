import sys
import RashodQr as RQ
from UBTS10 import dn
from math import pi


def uchastokZa(t0,p,dn,):
	VkKr=25*((t0/p)**0.5)
	QkKr=pi/4*((D**2)-(dn**2))*VkKr
	Pk=((128*Q*n*e)/(pi*((D-dn)**3)*(D+dn)))+(16*t0*e)/(3(D-dn))