#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

from BalloonTip import BalloonTip

if __name__ == '__main__':
    balloon = BalloonTip("Example of BalloonTip class")
    balloon.create_tray_icon()
    
    number = raw_input("Podaj liczbe: ")
    if number.isdigit():
        balloon.show_tip("Podany ciag jest liczba!")
    else:
        balloon.show_tip("Podany ciag nie jest liczba!")
    
    raw_input("Nacisnij ENTER aby zakonczyc")

    balloon.destroy() 
        
        
        