# -*- coding: utf-8 -*-
#
# 		*** Product Selector 
# 
# 		Created: 			25 Jan 2018
# 		Last updated: 	 	28 Aug 2018 
#
from openerp import models, fields, api
import openerp.addons.decimal_precision as dp

from . import px_vars
from . import px_vars_ext

class ProductSelector(models.Model):
	
	_name = 'price_list.product.selector'

	_description = 'Product Selector'



# ----------------------------------------------------------- Native ------------------------------------------------------
	# Product 
	product_id = fields.Many2one(
			'product.product', 
			string='pl - Product', 
			
			domain=[
						('sale_ok', '=', True),
						('pl_price_list', '=', '2019'),
			], 
			
			change_default=True, 
			ondelete='restrict', 
			required=False,
			#create_edit=False, 
		)



# ----------------------------------------------------------- Categories ------------------------------------------------------
	
	family = fields.Selection(

			selection=px_vars_ext._ser_family_list,
		
			required=True,
		)

	@api.onchange('family')
	def _onchange_family(self):
		if self.family != False: 
			if self.x_type == 'service': 
				return { 'domain': { 
										'product_id': [			
														('type', '=', 'service'),
														('pl_family', '=', self.family),
														('pl_price_list', '=', '2019'),
													],
									},
						}

	treatment_laser = fields.Selection(

			selection=px_vars_ext._treatment_list_laser,
		
			required=False,
		)

	@api.onchange('treatment_laser')
	def _onchange_treatment_laser(self):
		if self.treatment_laser != False: 
			if self.x_type == 'service': 
				return { 'domain': { 
										'product_id': [			
														('type', '=', 'service'),
														('pl_family', '=', self.family),
														('pl_treatment', '=', self.treatment_laser),
														('pl_price_list', '=', '2019'),
													],
									},
						}

	treatment_medical = fields.Selection(

			selection=px_vars_ext._treatment_list_medical,
		
			required=False,
		)

	@api.onchange('treatment_medical')
	def _onchange_treatment_medical(self):
		if self.treatment_medical != False: 
			if self.x_type == 'service': 
				return { 'domain': { 
										'product_id': [			
														('type', '=', 			'service'),
														('pl_family', '=', 		self.family),
														('pl_treatment', '=', 	self.treatment_medical),
														('pl_price_list', '=', '2019'),
													],
									},
						}


	treatment_cosmetology = fields.Selection(

			selection=px_vars_ext._treatment_list_cosmetology,
		
			required=False,
		)

	@api.onchange('treatment_cosmetology')
	def _onchange_treatment_cosmetology(self):
		if self.treatment_cosmetology != False: 
			if self.x_type == 'service': 
				return { 'domain': { 
										'product_id': [			
														('type', '=', 		'service'),
														('pl_family', '=', 	self.family),
														('pl_treatment', '=', self.treatment_cosmetology),
														('pl_price_list', '=', '2019'),
													],
									},
						}







# ----------------------------------------------------------- Fields ------------------------------------------------------

	# Name 
	name = fields.Text(
			string='Description', 
			required=True,

			compute='_compute_name', 
		)
	@api.multi
	#@api.depends('partner_id')
	def _compute_name(self):
		for record in self:
			if record.product_id.name != False: 
				record.name = record.product_id.name 

	# Type 
	x_type= fields.Selection(
			selection=[
							('service', 				'Servicio'),
							('product', 				'Producto'),
						], 

			string='Tipo', 
		)


	# Qty 
	product_uom_qty = fields.Float(
			string='Quantity', 
			digits=(16, 0), 
			required=True, 
			default=1.0,
		)



	# Order 
	order_id = fields.Many2one(
			'sale.order', 
			string='Order Reference', 
			required=True, 
			ondelete='cascade', 
			index=True, 
			copy=False, 
		)


# ----------------------------------------------------------- Actions ------------------------------------------------------
	@api.multi
	def create_orderline(self):  
		"""
		Create Order Line 
		"""
		#print()
		#print('Create Orderline')

		# Create 
		ret = self.order_id.order_line.create({
													'name': self.name,
													'product_id': self.product_id.id,
													'product_uom_qty': self.product_uom_qty, 

													#'x_price_manual': self.price_manual, 

													'order_id': self.order_id.id,
												})
