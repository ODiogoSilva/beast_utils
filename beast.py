#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  beast.py
#  
#  Copyright 2013 Unknown <diogo@UltraArch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

class SequenceIO ():
	def __init__ (self, xml_file):
		""" The sequence class is initialized by providing the XML input file that will be parser/manipulated """
		self.xml_file = xml_file
	def parser (self):
		""" This will parse the XML input file and return a dictionary with the taxa names as keys and sequences as values """
		#import easy to use xml parser called minidom:
		from xml.dom.minidom import parseString
		
		file_handle = open(self.xml_file)
		
		xml = parseString(file_handle.read())
		file_handle.close()
		
		xmlTag = xml.getElementsByTagName('alignment')[0].toxml()
		
		print (xmlTag)
		
		


