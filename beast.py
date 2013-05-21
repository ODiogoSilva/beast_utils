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

class AlignmetIO ():
	def __init__ (self, xml_file):
		""" The sequence class is initialized by providing the XML input file that will be parser/manipulated """
		self.xml_file = xml_file
		
	def getIDSeq (self, dom_alignment_obj):
		""" Retrieves a dictionary with the taxon id as key and its sequence as value from a single DOM element. The DOM element must contain a set of sequence tags, which will be parsed for the taxon id and sequence """
		alignment_storage = {}
		
		for sequence_element in dom_alignment_obj.getElementsByTagName("sequence"):
			taxon_id = sequence_element.childNodes.item(1).getAttribute("idref")
			sequence = sequence_element.childNodes.item(2).toxml().strip()
			alignment_storage[taxon_id] = sequence
			
		return alignment_storage
		
	def parser (self):
		""" This will parse the XML input file and return a dictionary with the taxa names as keys and sequences as values """
		#import easy to use xml parser called minidom:
		from xml.dom.minidom import parseString
		
		file_handle = open(self.xml_file)
		
		xml_beast = parseString(file_handle.read())
		file_handle.close()
		
		alignmentTag = xml_beast.getElementsByTagName("alignment")
		
		for alignment_obj in alignmentTag:
			if alignment_obj.childNodes != []:
				current_alignment = self.getIDSeq (alignment_obj)
				

		
						
		


