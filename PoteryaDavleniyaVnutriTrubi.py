import sys

from math import *


def e2_1(Ln,h1,ht,l1):
    return (round(ceil(Ln-h1-ht)/10)*10-l1)


def E1(t0,dv,p,n,e,e2,Km):
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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*e*Km/((pi**2)*(dv**5))/1000000,3)
      return Pv


def E2(t0,dv,p,n,e2,Km,Ln,h1,ht,l1):
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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*e2_1(Ln,h1,ht,l1)*Km/((pi**2)*(dv**5))/1000000,3)
      return Pv

def E3(t0,dv,p,n,e2,Km,Ln,h1,ht,l1):
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
      Pv=round(Lv*8*((RQ.MaxQr()/1000)**2)*p*e2_1(Ln,h1,ht,l1)*Km/((pi**2)*(dv**5))/1000000,3)
      return Pv


def uchastokZa(t0,p,dn,):
   VkKr=25*((t0/p)**0.5)
   QkKr=pi/4*((D**2)-(dn**2))*VkKr
    if (RQ.MaxQr() > Qvkr):
	  Pk=((128*Q*n*e)/(pi*((D-dn)**3)*(D+dn)))+(16*t0*e)/(3(D-dn))
      return Pk


def uchastokZaZamkami(t0, p, dn, ):
    VkKr = 25 * ((t0 / p) ** 0.5)
    QkKr = pi / 4 * ((D ** 2) - (dm ** 2)) * VkKr
    Pkmm = (8 *(Q ** 2) * p /(((pi ** 2) * ((D ** 2) - (dm ** 2))) ** 2)) * (1.25 + (((D ** 2) - (dm ** 2)) / ((D ** 2) - (dn ** 2))) * (0.75 * (((D ** 2) - (dm ** 2)) / ((D ** 2) - (dn ** 2))) - 2))
    if (RQ.MaxQr() > Qvkr):
    Pk = (((128 * Q * n * lm) / (pi * ((D - dm) ** 3) * (D + dm))) + (16 * t0 * lm) / (3(D - dn)) + Pkmm) * e / lo




