# -*- coding: utf-8 -*-
"""
	Subfamily

	Created: 			 9 Dec 2019
	Last up: 			 9 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api


class Subfamily(models.Model):	
	"""
	Subfamily 
	"""
	
	_name = 'price_list.product.subfamily'
	
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

