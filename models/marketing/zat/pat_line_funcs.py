# -*- coding: utf-8 -*-
"""
	Patient Line Funcs - Dep !

	Done by Patient Line

	Created: 	11 Dec 2019
	Updated: 	13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Line Analysis - Dep -----------------------
#def macro_line_analysis(self, line):
def macro_line_analysis_dep(self, line):
	"""
	New - 2019
	Marketing
	Analyses Line to update counters
	"""
	#print()
	#print('X - Macro Line Analysis')

	#print(patient_line)
	#print(self)
	#print(line)
	#print()


	# Patient Line Macros	

	# Init
	qty = line.product_uom_qty


	# Doctor
	if self.doctor.name in [False]:
		self.doctor = line.doctor



# Family Analysis


	# Increase Sales
	if line.state in ['sale']:

		# Consultation
		if line.family in ['consultation']:
			self.inc_nr_consultation(qty)

		# Procedure
		elif line.family in ['procedure']:
			self.inc_nr_procedure(qty)
			
			# All
			self.add_procedure_treatment(line.product_id)
			self.add_procedure_pathology(line.product_id)
			self.add_procedure_zone(line.product_id)

		# Product
		elif line.family in ['product']:
			self.inc_nr_product(qty)

		# Increase Sales
		self.inc_nr_sale(qty)



	# Increase Drafts
	elif line.state in ['draft']:
		self.inc_nr_draft(qty)


