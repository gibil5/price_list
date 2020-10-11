# -*- coding: utf-8 -*-
"""
    TimeFuncs - Dep - 11 Aug 2020

    Created:                 1 Nov 2016
    Last updated:           25 Apr 2019
"""

from datetime import datetime,tzinfo,timedelta


#------------------------------------------------ Time ---------------------------------------------------
class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
