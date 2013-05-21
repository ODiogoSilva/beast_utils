#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  beast_seq.py
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

parser.add_argument("-in",dest="infile",help="The alignment files")

args = parser.parse_args()

def main():

	return 0

if __name__ == '__main__':
	main()

