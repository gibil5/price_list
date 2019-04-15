# -*- coding: utf-8 -*-
"""
		*** Product Product
 
		Created: 			 9 Apr 2019
		Last up: 	 		 9 Apr 2019
"""
from openerp import models, fields, api

class ProductProduct(models.Model):

	_inherit = 'product.product'

	#_order = 'name'




# ----------------------------------------------------------- Print Ticket -------------------------------

	def get_name_ticket(self):
		"""
		Used by Print Ticket.
		"""
		#return self.x_name_ticket
		return self.pl_name_short


