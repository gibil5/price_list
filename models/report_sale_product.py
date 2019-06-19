# -*- coding: utf-8 -*-
"""
		ReportSaleProduct
 		Created: 			   	9 Mar 2019
		Last up: 	 		 	9 Mar 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from openerp.addons.openhealth.models.management import mgt_funcs

class ReportSaleProduct(models.Model):
	
	_inherit = 'openhealth.report.sale.product'
	


# ----------------------------------------------------------- Relational -----------------
	management_id = fields.Many2one(
			'openhealth.management',
		)


# ----------------------------------------------------------- Create Lines - 2019 -----------------

	# Create Lines 
	def create_lines(self, orders):  
		print()
		print('Create Lines - 2019')

		# Loop
		for order in orders: 
			for line in order.order_line: 
				#if line.product_id.categ_id.name == 'Cremas':
				#if line.product_id.pl_family in ['topical']:
				if line.product_id.pl_family in ['topical', 'card', 'kit']:
					
					print('Create !')

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

