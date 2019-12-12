# -*- coding: utf-8 -*-
"""
	Counter Set - Object Oriented
	
	For Marketing

	Created: 				12 Dec 2019
	Last up: 				12 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class CounterSet(models.Model):
	"""
	Used by Marketing
	"""
	_name = 'openhealth.marketing.counter_set'

	_description = 'Openhealth Marketing Counter Set'

	#_order = 'date_create asc'



# ----------------------------------------------------------- Primitives ---------------------------------------------

	name = fields.Char()
