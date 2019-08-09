# -*- coding: utf-8 -*-
"""
	Export

	Created: 			11 Sep 2018
	Last up: 	 		22 Jun 2019
"""
from __future__ import print_function  # Only needed for Python 2
import os
import shutil
import io
from openerp.addons.openhealth.models.containers import lib_exp
from . import pl_lib_exp


# -------------------------------------------------------------------------------------------------
def pl_export_txt(self, electronic_order, export_date):
	"""
	high level support for doing this and that.
	"""
	#print()
	#print('pl - Export Text')
	#print(os.environ['HOME'])


# Prepare
	# Init
	base_dir = os.environ['HOME']
	path = base_dir + "/mssoft/ventas/" + export_date

	# Make Dirs
	target = base_dir + "/mssoft/"
	if not os.path.isdir(target):
		os.mkdir(target)

	target = base_dir + "/mssoft/ventas/"
	if not os.path.isdir(target):
		os.mkdir(target)

	# Remove
	if os.path.isdir(path) and not os.path.islink(path):
		shutil.rmtree(path)		# If dir
	#elif os.path.exists(path):
	#	os.remove(path)			# If file

	# Create
	os.mkdir(path)



# Loop
	for order in electronic_order:

		# Get File Name
		file_name, id_serial_nr = pl_lib_exp.pl_get_file_name(order)		

		# Init Electronic
		order.pl_init(id_serial_nr, path, file_name)

		# Create Content 
		order.pl_create_txt()			# Object Oriented

		# Create File
		order.pl_create_file()			# Object Oriented



# Shut down and Clean
	# Compress and Remove
	source = path
	tarred = path + '.tar'
	ziped = path + '.tar.gz'
	os.system("rm -rf " + tarred + " " + ziped)
	os.system("tar cf " + tarred + " " + source)
	os.system("gzip " + tarred)

	return ziped

# export_txt

