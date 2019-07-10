# -*- coding: utf-8 -*-
"""
	Pricelist Marketing Order Line 

	Created: 			26 Jun 2019
	Last updated: 		26 Jun 2019
"""
from openerp import models, fields, api
from . import mkt_vars

class MarketingOrderLine(models.Model):

	_name = 'price_list.marketing.order_line'

	_description = "PriceList Marketing Order Line"

	_order = 'date desc'



# ----------------------------------------------------------- Relational ------------------------------------------------------

	#family = fields.Char()
	#subfamily = fields.Char(
	#subsubfamily = fields.Char(


	family = fields.Selection(

			selection=mkt_vars._family_list,
		)


	subfamily = fields.Selection(

			selection=mkt_vars._subfamily_list,
		)


	subsubfamily = fields.Selection(

			selection=mkt_vars._subsubfamily_list,
		)





# ----------------------------------------------------------- Relational ------------------------------------------------------
	# Marketing Id
	marketing_id = fields.Many2one(			
			'openhealth.marketing',
			ondelete='cascade', 			
		)

	# Marketing Id
	patient_line_id = fields.Many2one(			
			'openhealth.patient.line',
			ondelete='cascade', 			
		)




# ----------------------------------------------------------- Setters ------------------------------------------------------

	def set_patient_line_id(self, patient_line_id):

		self.patient_line_id = patient_line_id





# ----------------------------------------------------------- Natives ------------------------------------------------------
	order = fields.Many2one(
			'sale.order',
			ondelete='cascade',
		)


	patient = fields.Many2one(
			'oeh.medical.patient',
			string='Paciente',
			ondelete='cascade',
		)


	doctor = fields.Many2one(
			'oeh.medical.physician',
			#string = "Médico", 	
		)


	product_id = fields.Many2one(
			'product.product',
			ondelete='cascade',			
		)


	date = fields.Datetime(
		)


	product_uom_qty = fields.Float(
		)

	price_unit = fields.Float(
		)

	price_net = fields.Float(
		)






	price_list = fields.Char(
		)

	state = fields.Char(
		)

