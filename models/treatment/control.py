# -*- coding: utf-8 -*-
"""
Control

Created: 			19 Sep 2019
Last updated: 	 	19 Sep 2019
"""
from openerp import models, fields, api

class Control(models.Model):
	"""
	Class Control
	Extends the Business Rules. Should not extend the Data Model.
	"""	
	_inherit = 'openhealth.control'

	_description = 'Control'

