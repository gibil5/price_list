# -*- coding: utf-8 -*-
#
# 	Patient Line
# 
# 	Created: 				16 May 2018
#
from __future__ import print_function
from openerp import models, fields, api
#from . import pat_vars
from openerp.addons.openhealth.models.libs import eval_vars
from openerp.addons.openhealth.models.emr import prodvars

class PatientLine(models.Model):

	_order = 'date_create asc'

	_inherit = 'openhealth.patient.line'



# ----------------------------------------------------------- Natives ------------------------------------------------------

	proc_treatment = fields.Char(
			'Proc Tratamiento',
		)

	proc_pathology = fields.Char(
			'Proc Patologia',
		)

	proc_zone = fields.Char(
			'Proc Zona',
		)


	proc_zone = fields.Char(
			'Proc Zona',
		)




# ----------------------------------------------------------- Update Fields Proc ------------------------------------------------------

	# Update fields Proc
	@api.multi
	def update_nrs(self):  
		#print()
		#print('Pl - Update Nrs')
		#print 


		# Sales 
		for line in self.sale_line: 
			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		# Budgets
		self.budget_amount = ''
		self.budget_prod = ''
		for line in self.budget_line: 


			# Doctor 
			if self.doctor.name == False: 
				self.doctor = line.doctor.id 



		
			# Budget Amount 
			self.budget_amount = self.budget_amount + str(line.price_total) + ', '

			# Budget Flag 
			if line.price_total >= 1500: 
				self.budget_flag = True



			# Budget Prod
			if line.product_id.x_treatment != False: 
				if line.product_id.x_treatment in prodvars._h_subfamily: 
					self.budget_prod = self.budget_prod + prodvars._h_subfamily[line.product_id.x_treatment] + ', '
				else: 
					self.budget_prod = self.budget_prod + line.product_id.x_treatment + ', '




		# Amount and Prod 
		self.budget_amount = self.budget_amount[:-2]
		self.budget_prod = self.budget_prod[:-2]




		# Nr Budgets
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_budget_id','=', self.id),
																			]) 
		self.nr_budget = count




		# Nr Sale
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_sale_id','=', self.id),
																			]) 
		self.nr_sale = count




		# Nr Consultations
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_consu_id','=', self.id),
																			]) 
		self.nr_consu = count




		# Nr Product
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_product_id','=', self.id),
																			]) 
		self.nr_products = count





		# Nr Proc 
		count = self.env['openhealth.marketing.order.line'].search_count([
																				('patient_line_proc_id','=', self.id),
																			]) 
		self.nr_proc = count





		# Nr Reco 
		count = self.env['openhealth.marketing.recom.line'].search_count([
																				('patient_line_id','=', self.id),
																			]) 
		self.nr_reco = count

	# update_nrs

