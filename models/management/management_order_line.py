# -*- coding: utf-8 -*-
"""
	Management Order Line - Clean This !

	Only functions. Not the data model. 

	Created: 			28 May 2018
	Last updated: 		 9 Dec 2019
"""
from openerp import models, fields, api
#from openerp.addons.openhealth.models.order import ord_vars
#from openerp.addons.openhealth.models.emr import prodvars

class management_order_line(models.Model):
	
	_inherit = 'openhealth.management.order.line'
	


# ----------------------------------------------------------- Handles Nex -----------------------------
	
	# Doctor Daily
	doctor_daily_id = fields.Many2one(			
			'doctor.daily',
			ondelete='cascade', 			
		)






