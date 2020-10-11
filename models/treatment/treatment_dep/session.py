# -*- coding: utf-8 -*-
"""
Session - Dep - 11 Aug 2020

Created: 			19 Sep 2019
Last updated: 	 	19 Sep 2019
"""
from openerp import models, fields, api

class Session(models.Model):
	"""
	Class Session
	Extends the Business Rules. Should not extend the Data Model.
	"""	
	_inherit = 'openhealth.session.med'

	_description = 'Session'

