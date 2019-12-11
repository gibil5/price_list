# -*- coding: utf-8 -*-
"""
	Patient Line Funcs 

	Created: 	11 Dec 2019
	Updated: 	11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
import datetime



# ----------------------------------------------------------- Line Analysis - PL -----------------------
def macro_line_analysis(self, line):
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

	qty = line.product_uom_qty


	# Vip Analysis
	if line.product_id.type in ['product']:
		if line.product_id.pl_family in ['card']:
			#print()
			#print('Macro Line Analysis')
			#print('Gotcha Vip')
			self.set_vip(True)
			self.vip_date = line.date



	# Doctor
	if self.doctor.name in [False]:
		self.doctor = line.doctor



	# Family Analysis
	if line.state in ['sale']:

		# Consultation
		if line.family in ['consultation']:
			self.inc_nr_consultation(qty)


		# Procedure
		elif line.family in ['procedure']:
			self.inc_nr_procedure(qty)

			# 2019
			#self.add_procedure_treatment(line.product_id.pl_treatment)
			#self.add_procedure_pathology(line.product_id.pl_pathology)
			#self.add_procedure_zone(line.product_id.pl_zone)
			
			# All
			self.add_procedure_treatment(line.product_id)
			self.add_procedure_pathology(line.product_id)
			self.add_procedure_zone(line.product_id)



		# Product
		elif line.family in ['product']:
			self.inc_nr_product(qty)


		# Sale
		self.inc_nr_sale(qty)



	# Draft
	elif line.state in ['draft']:
		self.inc_nr_draft(qty)
