# -*- coding: utf-8 -*-
"""
	First Contact - Object Oriented
	
	For Marketing

	Created: 				11 Dec 2019
	Last up: 				11 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class FirstContact(models.Model):
	"""
	Used by Marketing
	"""
	_name = 'openhealth.marketing.first_contact'

	_description = 'Openhealth Marketing First Contact'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Fields ---------------------------------------------

	name = fields.Char()
