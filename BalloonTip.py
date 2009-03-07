#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-

import os.path

import win32api
import win32con
import win32gui


class BalloonTip():
    """Class which makes easier to show Balloon Tips and create tray icon (Windows)"""
    tray = False
        
    def __init__(self, className, windowName="Python", icon=None):
        """Initialize all needed things"""
        wndclass = win32gui.WNDCLASS()
        hinst = wndclass.hInstance = win32api.GetModuleHandle(None)
        if icon is None or not os.path.isfile(icon):
            self.icon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        else:
            self.icon = win32gui.LoadImage(hinst, icon, win32con.IMAGE_ICON, 0,
                                           0, win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE)

        self.flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_INFO  

        wndclass.lpszClassName = className
        wndclass.style = win32con.CS_VREDRAW | win32con.CS_HREDRAW
        wndclass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wndclass.hbrBackground = win32con.COLOR_WINDOW
        wndclass.lpfnWndProc = { win32con.WM_DESTROY : self.destroy }

        guiclass = win32gui.RegisterClass(wndclass)
        self.window = win32gui.CreateWindow(guiclass, windowName,
                                       win32con.WS_OVERLAPPED | win32con.WS_SYSMENU,
                                       0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                                       0, 0, hinst, None)
        win32gui.UpdateWindow(self.window)

    def destroy(self):
        """Destroy all stuff"""
        if self.tray:
            self.remove_tray_icon()
        win32gui.PostQuitMessage(0)

        return True       
    
    def create_tray_icon(self):
        """Create an icon in tray"""
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, (self.window, 0, self.flags, 0, self.icon))
        self.tray = True
        
        return True        

    def remove_tray_icon(self):
        """Remove an icon from tray"""
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, (self.window, 0, self.flags, 0, self.icon))
        self.tray = False
        
        return True

    def show_tip(self, message, title="Python"):
        """Show balloon tip!"""
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, (self.window, 0, self.flags, 0, self.icon,
                                                        "", message, 10, title, win32gui.NIIF_INFO))

        return True

