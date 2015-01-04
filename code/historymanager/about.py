#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009-2011 TUBITAK/UEKAE, 2014 Pisi Linux (Anka) Team
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

# PDS Stuff
import context as ctx

# Application Data
PACKAGE     = "History Manager"
appName     = "history-manager"
modName     = "historymanager"
version     = "0.2.7.1"
homePage    = "http://www.pardus.org.tr/eng/projects"
bugEmail    = "bugs@pardus.org.tr"
icon        = "history-manager.png"
catalog     = appName

if ctx.Pds.session == ctx.pds.Kde4:

    # PyKDE4 Stuff
    from PyKDE4.kdecore import KAboutData, ki18n, ki18nc

    programName = ki18n(PACKAGE)
    description = ki18n(PACKAGE)
    license     = KAboutData.License_GPL
    copyright   = ki18n("(c) 2009-2010 TUBITAK/UEKAE")
    text        = ki18n(None)
    aboutData   = KAboutData(appName, catalog, programName, version, description, license, copyright, text, homePage, bugEmail)

    # Authors
    aboutData.addAuthor(ki18n("İşbaran Akçayır"), ki18n("Old Maintainer"))
    aboutData.addAutho(ki18n("Ayhan Yalçınsoy"), ki18n("Current Maintainer"))
    aboutData.setTranslator(ki18nc("NAME OF TRANSLATORS", "Your names"), ki18nc("EMAIL OF TRANSLATORS", "Your emails"))

    # Use this if icon name is different than appName
    aboutData.setProgramIconName(icon)
