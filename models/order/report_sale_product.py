# -*- coding: utf-8 -*-
"""
	ReportSaleProduct
	
	Only functions. Not the data model. 
 	
 	Created: 			   	 9 Mar 2019
	Last up: 	 		 	10 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.management import mgt_funcs

import datetime

class ReportSaleProduct(models.Model):
	"""
	Report Sale Product
	"""	
	_inherit = 'openhealth.report.sale.product'
	

# ----------------------------------------------------- Django Interface --------------------------
	@api.multi
	def get_name(self):
		"""
		Django interface
		"""
		print()
		print('Get name')
		return self.title



	@api.multi
	def get_total(self):
		"""
		Django interface
		"""
		print()
		print('Get total')

		if self.total not in [False]:
			return self.total

		else:
			return 0


	@api.multi
	def get_count(self):
		"""
		Django interface
		"""
		print()
		print('Get count')
		if self.total_qty not in [False]:
			return self.total_qty
		else:
			return 0




# ----------------------------------------------------------- Create Lines - 2019 -----------------
	# Create Lines 
	def create_lines(self, orders):  
		#print()
		#print('X - Create Lines')

		# Loop
		for order in orders: 
			for line in order.order_line: 


				#if line.product_id.pl_family in ['topical', 'card', 'kit']:   		# This is a Trainwreck !
				if line.product_id.is_product():

					#print('Create !')

					# Create Order Line 
					ret = self.order_line_ids.create({
															'name': line.name,
															'product_id': line.product_id.id,
															'patient': order.patient.id,
															'price_unit': line.price_unit,
															'product_uom_qty': line.product_uom_qty,
															'x_date_created': line.create_date,
															'state': order.state,

															'report_sale_product_id': self.id,
													})
	# create_lines


# ----------------------------------------------------------- Update ------------------------------------------------------
	# Update 
	@api.multi
	def update(self):  
		"""
		Update RSP
		"""
		print()
		print('X - Report Sale Product - Update')

		# Clean 
		self.order_line_ids.unlink()
		self.item_counter_ids.unlink()


		# Init
		self.date_begin = self.name


		# Get Orders 

		# One Date
		if not self.several_dates:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_begin)

		# Several Dates
		else:
			orders, count = mgt_funcs.get_orders_filter_fast(self, self.date_begin, self.date_end)

		print(orders)
		print(count)


		# Create Order lines
		self.create_lines(orders)



		# Item Counter 
		total_qty = 0
		total = 0 
		for order_line in self.order_line_ids: 

			# Init 
			name = order_line.product_id.name

			qty = order_line.product_uom_qty

			subtotal = order_line.price_total 

			total_qty = total_qty + qty
			total = total + subtotal
			#print(name)
			#print(qty)
			#print(subtotal)
			#print()


			# Search 
			prod_ctr = self.env['openhealth.item.counter'].search([
																		('name', '=', name),
																		('report_sale_product_id', '=', self.id),
																	],
																	#order='x_serial_nr asc',
																	limit=1,
																)
			#print prod_ctr


			# Create or update 
			if prod_ctr.name != False: 				
				
				#prod_ctr.increase_qty(qty)
				prod_ctr.qty = prod_ctr.qty + qty 

				#prod_ctr.increase_total(subtotal)
				prod_ctr.total = prod_ctr.total + total 





			else:		# Create 
				ret = self.item_counter_ids.create({
															'name': name,
															'qty': qty, 
															'total': subtotal, 
															'report_sale_product_id': self.id,
													})
				#print ret 


		# Update Descriptors 
		self.total_qty = total_qty
		self.total = total
		#print 


		# For Django
		self.date_test = datetime.datetime.now() 
		return 1
	# update
