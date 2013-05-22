#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  beast_seq.py v0.1
#  author: Diogo N Silva
#  last updated: 22/05/2013
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

import beast
import argparse

parser = argparse.ArgumentParser(description="Toolbox for processing outlier loci from Phylo-MCOA")

parser.add_argument("-in",dest="infile",help="The BEAST XML file")
parser.add_argument("-of",dest="output_format",nargs="+",default="nexus",choices=["fasta","phylip","nexus"],help="The format of the output file")
parser.add_argument("-o",dest="output_file",help="The nameof the output file")

args = parser.parse_args()

def main():
	# Arguments
	xml_file = "".join(args.infile)
	output_format = args.output_format
	output_file = "".join(args.output_file)
	
	print (output_format)
	
	# Initializing main class
	xml_handle = beast.AlignmetIO(xml_file)
	
	alignment_list = xml_handle.parser()
	
	# Write to file
	for alignment in alignment_list:
		for file_format in output_format:
			xml_handle.writeAlignment(alignment,output_file,output_format=file_format)

	return 0

if __name__ == '__main__':
	main()

