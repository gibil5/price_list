# -*- coding: utf-8 -*-
"""
	payment method line

 	Created: 				2016
 	Last mod: 				28 Aug 2018
"""
from openerp import models, fields, api

#from . import pm_vars
from . import pl_pm_vars

#from openerp.addons.openhealth.models.libs import acc_lib

class payment_method_line(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.payment_method_line'




# ----------------------------------------------------------- Method --------------------------------
	# Method
	method = fields.Selection(

			#selection=pm_vars._payment_method_list,
			selection=pl_pm_vars._payment_method_list,
		
			string="Forma de Pago",
			default="cash",
			required=True,
		)

