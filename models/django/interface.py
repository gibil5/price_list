# -*- coding: utf-8 -*-
"""
	Django - Interface

	Only Data model. No functions.

 	Created: 				10 Dec 2019
 	Last up: 				10 Dec 2019
"""
from openerp import models, fields, api

class DjangoInterface(models.Model):
	
	_inherit = 'openhealth.django.interface'
	
	#_order = 'name'


