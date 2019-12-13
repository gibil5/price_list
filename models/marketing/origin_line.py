# -*- coding: utf-8 -*-
"""
	Origin Line - Object Oriented
	
	For Marketing

	Created: 				13 Dec 2019
	Last up: 				13 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class OriginLine(models.Model):
	"""
	Used by Marketing
	"""
	#_inherit = 'openhealth.marketing.counter_set'

	_name = 'openhealth.marketing.origin.line'

	_description = 'Openhealth Marketing Origin Line'

	#_order = 'date_create asc'


# ----------------------------------------------------------- Relational ------------------------------------------------------

	# Marketing 
	marketing_id = fields.Many2one(
			'openhealth.marketing',
			#ondelete='cascade', 
			required=True,
		)


# ----------------------------------------------------------- Fields ---------------------------------------------

	name = fields.Char(
			#string='Origen',
			required=True,
		)

	name_sp = fields.Char(
			string='Origen',
			required=True,
		)


	count = fields.Integer(
			default=0,
			string='Nr Pacientes',
			required=True,
		)


