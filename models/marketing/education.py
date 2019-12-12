# -*- coding: utf-8 -*-
"""
	Education
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class Education(models.Model):
	"""
	Used by Marketing
	"""
	_name = 'openhealth.marketing.education'

	_description = 'Openhealth Marketing Education'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Fields ---------------------------------------------

	name = fields.Char()


	first = fields.Integer()

	second = fields.Integer()

	technical = fields.Integer()

	university = fields.Integer()

	master_phd = fields.Integer()

	undefined = fields.Integer()





