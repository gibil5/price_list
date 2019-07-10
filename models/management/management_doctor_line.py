 -*- coding: utf-8 -*-
"""
	Doctor Line

	Created: 			18 May 2018
	Last updated: 		 7 May 2019
"""
from __future__ import print_function
#import collections
from openerp import models, fields, api
#from . import mgt_vars

class DoctorLine(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.management.doctor.line'





# ----------------------------------------------------------- Relational --------------------------

	management_id = fields.Many2one(
			'openhealth.management',
			#ondelete='cascade',
		)


	doctor_id = fields.Many2one(
			'openhealth.management.doctor.line',
			ondelete='cascade',
		)


	# Sales
	order_line = fields.One2many(
			'openhealth.management.order.line',
			'doctor_id',
		)
