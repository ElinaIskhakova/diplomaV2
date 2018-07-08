import sys
import RashodQr as RQ
from UBTS10 import Km
from math import *

def E1(t0,dv,p,n,e2):
    Hev=(t0*(dv**2*p/(n**2)))
    Revkr=e2+7.3*pow(Hev,0.58)
    Vvkr=round(Revkr*n/(dv*p),3)
    Qvkr=round(pi/4*(dv**2)*Vvkr,3)*1000
    if (RQ.MaxQr()>Qvkr):
      Vb=round(4*RQ.MaxQr()/1000/(pi*(dv**2)),3)
      Rev=(Vb*dv*p/n)
      Senv=round(t0*dv/(Vb*n),3)
      Rev1=Rev/(1+Senv/6)
      Lv=round(0.075/(Rev1**0.125),3)
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*75*Km/((pi**2)*(dv**5))/1000000,3)
      print(Hev,Revkr,Vvkr,Qvkr,Vb,Rev,Senv,Rev1,Lv,Pv)
      return Pv


def E1(t0, dv, p, n, e2):
    Hev = (t0 * (dv ** 2 * p / (n ** 2)))
    Revkr = e2 + 7.3 * pow(Hev, 0.58)
    Vvkr = round(Revkr * n / (dv * p), 3)
    Qvkr = round(pi / 4 * (dv ** 2) * Vvkr, 3) * 1000
    if (RQ.MaxQr() > Qvkr):
        Vb = round(4 * RQ.MaxQr() / 1000 / (pi * (dv ** 2)), 3)
        Rev = (Vb * dv * p / n)
        Senv = round(t0 * dv / (Vb * n), 3)
        Rev1 = Rev / (1 + Senv / 6)
        Lv = round(0.075 / (Rev1 ** 0.125), 3)
        Pv = round(Lv * 8 * ((RQ.MaxQr() / 1000) ** 2) * p * 75 * Km / ((pi ** 2) * (dv ** 5)) / 1000000, 3)
        print(Hev, Revkr, Vvkr, Qvkr, Vb, Rev, Senv, Rev1, Lv, Pv)
        return Pv
#print (E1(6,0.09,1200,0.016,2100))

print (E1(6,0.125,1200,0.016,2100))
