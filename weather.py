# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:37:05 2020

@author: Win10Pro
"""

from sources import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
 print(number, outlook)