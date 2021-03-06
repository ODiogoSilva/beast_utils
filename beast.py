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
		import collections
		
		alignment_storage = collections.OrderedDict()
		
		for sequence_element in dom_alignment_obj.getElementsByTagName("sequence"):
			taxon_id = sequence_element.childNodes.item(1).getAttribute("idref")
			sequence = sequence_element.childNodes.item(2).toxml().strip()
			alignment_storage[taxon_id] = sequence
			
		return alignment_storage
		
	def parser (self):
		""" This will parse the XML input file and return a list of dictionaries with the taxa names as keys and sequences as values. The size of the list will correspond to the number of loci in the xml file """
		#import easy to use xml parser called minidom:
		from xml.dom.minidom import parseString
		
		loci_storage = []
		
		file_handle = open(self.xml_file)
		
		# Read and make inital parsing of the xml file using the xml module
		xml_beast = parseString(file_handle.read())
		file_handle.close()
		
		# Get only the XML part that contains the sequence alignment
		alignmentTag = xml_beast.getElementsByTagName("alignment")
		
		# Iterate over the alignment field(s) and retrieve a dictionary from each one
		for alignment_obj in alignmentTag:
			if alignment_obj.childNodes != []:
				current_alignment = self.getIDSeq (alignment_obj)
				loci_storage.append(current_alignment)
			
		return loci_storage

	def guess_code (self,sequence):
		""" Function that guesses the code of the molecular sequences (i.e., DNA or Protein) based on the first sequence of a reference file """
		sequence = sequence.upper().replace("-","") # Removes gaps from the sequence so that the frequences are not biased
		DNA_count = sequence.count("A") + sequence.count("T") + sequence.count("G") + sequence.count("C") + sequence.count("N")
		DNA_proportion = float(DNA_count)/float(len(sequence))
		if DNA_proportion > 0.9: # The 0.9 cut-off has been effective so far
			code = ("DNA","N")
		else:
			code = ("Protein","X")
		return code
	
	def writeAlignment (self, alignment_dictionary, output_file, output_format="fasta"):
		""" Write an alignment to a file in a specified format. The alignment dictionary must contain the taxon id as keys and their sequences as values """
		
		output_handle = open(output_file, "w")
		
		if "fasta" in output_format:
			for taxon, sequence in alignment_dictionary.items():
				output_handle.write(">%s\n%s\n" % (taxon, sequence))

		elif "nexus" in output_format:
			
			sequence_length = len(next(iter(alignment_dictionary.values())))
			coding = self.guess_code(next(iter(alignment_dictionary.values())))
			
			output_handle.write("#NEXUS\n\nBegin data;\n\tdimensions ntax=%s nchar=%s ;\n\tformat datatype=%s interleave=no gap=- missing=%s ;\n\tmatrix\n" % (len(alignment_dictionary), sequence_length, coding[0], coding[1]))
			
			for taxon, sequence in alignment_dictionary.items():
				output_handle.write("%s %s\n" % (taxon[0:24].ljust(25),sequence))
			else:
				output_handle.write(";\n\tend;")
			
		elif "phylip" in output_format:
			sequence_length = len(next(iter(alignment_dictionary.values())))
			sequence_number = len(alignment_dictionary)
			
			output_handle.write("%s %s\n" % (sequence_number, sequence_length))
			
			for taxon, sequence in alignment_dictionary.items():
				output_handle.write("%s %s\n" % (taxon[:24].ljust(25), sequence))
			
		output_handle.close()
		
		return 0
						
		


