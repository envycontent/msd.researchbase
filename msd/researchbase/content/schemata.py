# -*- coding: utf-8 -*-
#
# File: Schemata.py

# Copyright (c) 2007 by ACDT
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """ACDT <acdt@oucs.ox.ac.uk>"""
__docformat__ = 'plaintext'


from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.CMFCore import permissions

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
#from Products.ATExtensions.widget.url import UrlWidget

from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn
from Products.DataGridField.CheckboxColumn import CheckboxColumn


classificationSchema = Schema((

    LinesField(
        name='keywords1',
        widget=PicklistWidget(
            label=('Keywords 1'),
        ),
        schemata="Keywords",
        multiValued=1,
        searchable=1,
        vocabulary='listThemeVocab1'
    ),

    LinesField(
        name='keywords2',
        widget=PicklistWidget(
            label=(u'Keywords 2'),
        ),
        schemata="Keywords",
        multiValued=1,
        searchable=1,
        vocabulary='listThemeVocab2'
    ),
    
    LinesField(
        name='keywords3',
        widget=PicklistWidget(
            label=(u'Keywords 3'),
        ),
        schemata="Keywords",
        multiValued=1,
        searchable=1,
        vocabulary='listThemeVocab3'
    ),
    
    LinesField(
        name='keywords4',
        widget=PicklistWidget(
            label=(u'Keywords 4'),
        ),
        schemata="Keywords",
        multiValued=1,
        searchable=1,
        vocabulary='listThemeVocab4'
    ),
    
    LinesField(
        name='keywords5',
        widget=PicklistWidget(
            label=(u"Keywords 5"),
        ),
        schemata="Keywords",
        multiValued=1,
        searchable=1,
        vocabulary='listThemeVocab5'
    ),

),
)


