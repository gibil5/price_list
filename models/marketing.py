# -*- coding: utf-8 -*-
"""
 	Report Marketing
 
 	Created: 				19 May 2018
 	Last up: 	 			27 Nov 2018
"""
from __future__ import print_function
#import datetime
from timeit import default_timer as timer
#import collections
from openerp import models, fields, api
#from . import mkt_funcs
#from . import lib_marketing

from openerp.addons.openhealth.models.order import ord_vars

class Marketing(models.Model):

	_inherit = 'openhealth.marketing'



# ----------------------------------------------------------- Natives ----------------------
	owner = fields.Selection(
			[
				('week', 'Week'),
				('month', 'Month'),
				('year', 'Year'),
			],
			required=True,
		)


# ----------------------------------------------------------- Update Sales ------------------------
	# Update Sales
	@api.multi
	def update_sales(self):  
		print()
		print('Pl - Update Sales')

		# QC
		t0 = timer()

		# Clean Macros 
		self.patient_budget_count = 0 
		self.patient_sale_count = 0 
		self.patient_consu_count = 0 
		self.patient_proc_count = 0 


		# Loop - Patient Lines 
		for pat_line in self.patient_line: 

			# Update Line
			pat_line.update_fields_mkt()




			# Budgets
			budgets = self.env['sale.order'].search([
															('state', '=', 'draft'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)

			# Clean 
			pat_line.budget_line.unlink()


			# Create
			for budget in budgets:

				doctor = budget.x_doctor

				for line in budget.order_line: 
					
					if True: 

						# Budgets 
						budget_line = pat_line.budget_line.create({
																	'name': line.name,
																	'doctor': doctor.id,
																	'product_id': line.product_id.id, 
																	'x_date_created': budget.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit,
																	'patient_line_budget_id': pat_line.id, 
																	'marketing_id': self.id,
							})

			# Count
			self.patient_budget_count = self.patient_budget_count + len(pat_line.budget_line)

			# Update Nrs
			pat_line.update_nrs()





			# Orders 
			orders = self.env['sale.order'].search([
															('state', '=', 'sale'),
															('patient', '=', pat_line.patient.name),
													],
														order='date_order asc',
														#limit=1,
												)

			# Clean 
			pat_line.sale_line.unlink()
			pat_line.consu_line.unlink()
			pat_line.procedure_line.unlink()


			# Create
			for order in orders: 

				doctor = order.x_doctor

				for line in order.order_line: 
					
					prod = line.product_id

					# Sale
					sale_line = pat_line.sale_line.create({
															'name': line.name,
															'doctor': doctor.id,
															'product_id': line.product_id.id,
															'x_date_created': order.date_order,
															'product_uom_qty': line.product_uom_qty,
															'price_unit': line.price_unit,
															'patient_line_sale_id': pat_line.id, 
															'marketing_id': self.id, 
						})



					# Consultation
					#if prod.x_family in ['consultation']:
					#if prod.pl_subfamily in ['consultation']:
					if prod.pl_subfamily in ['consultation'] or prod.x_family in ['consultation']:
						consu_line = pat_line.consu_line.create({
																	'name': line.name, 
																	'product_id': line.product_id.id, 
																	'x_date_created': order.date_order, 
																	'product_uom_qty': line.product_uom_qty, 
																	'price_unit': line.price_unit, 
																	'patient_line_consu_id': pat_line.id, 
																	'marketing_id': self.id, 
																})


					# Procedure
					#if 	(prod.type not in ['product'])   and   (prod.x_family not in ['consultation']):
					#if 	(prod.type not in ['product']) and (prod.pl_subfamily not in ['consultation']):
					if 	(prod.type not in ['product']) and (prod.pl_subfamily not in ['consultation']) or (prod.type not in ['product']) and (prod.x_family not in ['consultation']):
						procedure_line = pat_line.procedure_line.create({
																			'name': line.name, 
																			'product_id': line.product_id.id, 
																			'x_date_created': order.date_order, 
																			'product_uom_qty': line.product_uom_qty, 
																			'price_unit': line.price_unit, 
																			'patient_line_proc_id': pat_line.id, 
																			'marketing_id': self.id, 
																		})


			# Update Counts
			self.patient_sale_count = self.patient_sale_count + len(pat_line.sale_line)
			self.patient_consu_count = self.patient_consu_count + len(pat_line.consu_line)
			self.patient_proc_count = self.patient_proc_count + len(pat_line.procedure_line)

			# Update Nrs
			pat_line.update_nrs()


		# QC
		t1 = timer()
		self.delta_sales = t1 - t0

	# update_sales



# ----------------------------------------------------------- QC ----------------------------------

	year = fields.Selection(

			selection=ord_vars._year_order_list,
		
			string='Año',
			#default='2019',
			required=True,
		)

	month = fields.Selection(

			selection=ord_vars._month_order_list,
		
			string='Mes',
			#required=True,
		)




# ----------------------------------------------------------- Sex  ----------------------------------
	# Sex 
	sex_male_per = fields.Float(
			'M %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_female_per = fields.Float(
			'F %',
			readonly=True, 
			digits=(16,1), 
		)

	sex_undefined_per = fields.Float(
			'Error %',
			readonly=True, 
			digits=(16,1), 
		)


# ----------------------------------------------------------- Education Level  ----------------------------------

	edu_fir_per = fields.Float(
			'Primaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_sec_per = fields.Float(
			'Secundaria %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_tec_per = fields.Float(
			'Instituto %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_uni_per = fields.Float(
			'Universidad %',
			readonly=True, 
			digits=(16,1), 
		)
	
	edu_mas_per = fields.Float(
			'Posgrado %',
			readonly=True, 
			digits=(16,1), 
		)

	edu_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
		)

# ----------------------------------------------------------- First Contact ----------------------------------

	# First Contact 
	how_u_per = fields.Float(
			'No Definido %',
			readonly=True, 
			digits=(16,1), 
		)

	how_none_per = fields.Float(
			'Ninguno %',
			readonly=True, 
			digits=(16,1), 
		)

	how_reco_per = fields.Float(
			'Recomendación %',
			readonly=True, 
			digits=(16,1), 
		)

	how_tv_per = fields.Float(
			'Tv %',
			readonly=True, 
			digits=(16,1), 
		)

	how_radio_per = fields.Float(
			'Radio %',
			readonly=True, 
			digits=(16,1), 
		)

	how_inter_per = fields.Float(
			'Internet %',
			readonly=True, 
			digits=(16,1), 
		)

	how_web_per = fields.Float(
			'Web %',
			readonly=True, 
			digits=(16,1), 
		)

	how_mail_per = fields.Float(
			'Mail %',
			readonly=True, 
			digits=(16,1), 
		)



