import sys
import RashodQr as RQ
import UBTS10 as UBTS
import LBTS311 as LBT

from math import *


def e2_1(Ln,h1,ht,l1):
    return (round(ceil(Ln-h1-ht)/10)*10-l1)


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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*75*UBTS.Km/((pi**2)*(dv**5))/1000000,3)
      return Pv


def E2(t0,dv,p,n,e2,Ln,h1,ht,l1):
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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*e2_1(Ln,h1,ht,l1)*LBT.Km/((pi**2)*(dv**5))/1000000,3)
      return Pv

def E3(t0,dv,p,n,e2,Ln,h1,ht,l1):
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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*e2_1(Ln,h1,ht,l1)*LBT.Km/((pi**2)*(dv**5))/1000000,3)
      return Pv


print (E2(6,0.125,1200,0.016,2100,3800,75,24.950,1600))


