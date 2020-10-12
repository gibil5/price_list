# -*- coding: utf-8 -*-
"""
	Family

	Created: 			 9 Dec 2019
	Last up: 			 9 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api


class Family(models.Model):	
	"""
	Family 
	"""
	
	_name = 'price_list.product.family'
	
	#_order = 'name asc'
	_order = 'idx asc'


# ----------------------------------------------------------- Fields ------------------------
	
	name = fields.Char(
			#'Name',
			required=True,
		)

	name_sp = fields.Char(
			'Nombre Esp',
			required=True,
		)

	idx = fields.Integer(
			'Idx',
			required=True,
		)


	#meta = fields.Char(
	#		'Meta',
	#	)

	#meta_sp = fields.Char(
	#		'Meta',
	#	)

