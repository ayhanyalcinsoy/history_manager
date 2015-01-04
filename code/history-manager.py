#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2011 TUBITAK/UEKAE, 2014 Pisi Linux Team
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# System
import sys
import dbus
# Pds Stuff
import historymanager.context as ctx

# Application Stuff
import historymanager.about as about

# Qt Stuff
from PyQt4.QtCore import SIGNAL

#from historymanager.about import aboutData, catalog
#from historymanager.window import MainManager

# Enable plugin if session is Kde4
if ctx.Pds.session == ctx.pds.Kde4:
    def CreatePlugin(widget_parent, parent, component_data):
        from historymanager.kcmodule import HistoryManager
        return HistoryManager(component_data, parent)

    if not dbus.get_default_main_loop():
        from dbus.mainloop.qt import DBusQtMainLoop
        DBusQtMainLoop(set_as_default = True)

        # Pds vs KDE
    if ctx.Pds.session == ctx.pds.Kde4:

        # PyKDE4 Stuff
        from PyKDE4.kdeui import *
        from PyKDE4.kdecore import *

        # Application Stuff
        from historymanager.window import HistoryManager
        from historymanager.about import aboutData

        # Set Command-line arguments
        KCmdLineArgs.init(sys.argv, aboutData)

        # Create a Kapplitcation instance
        app = KApplication()

        # Create Main Widget
        mainWindow = HistoryManager(None, aboutData.appName)
        mainWindow.show()

    else:

        # Application Stuff
        from historymanager.window import MainManager

        # Pds Stuff
        from pds.quniqueapp import QUniqueApplication
        from historymanager.context import KIcon, i18n

        # Create a QUniqueApllication instance
        app = QUniqueApplication(sys.argv, catalog=about.appName)

        # Create Main Widget and make some settings
        mainWindow = MainManager(None)
        mainWindow.show()
        mainWindow.resize(640, 480)
        mainWindow.setWindowTitle(i18n(about.PACKAGE))
        mainWindow.setWindowIcon(KIcon(about.icon))

    # Run the applications
    app.exec_()
