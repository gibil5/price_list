# -*- coding: utf-8 -*-
"""
	Configurator - EMR

	Created: 			25 Jan 2019
	Last updated: 		25 Jan 2019
"""
from __future__ import print_function

from openerp import models, fields, api

class ConfiguratorEmr(models.Model):
	"""
	high level support for doing this and that.
	"""
	#_inherit = 'openhealth.configurator'
	_inherit = 'openhealth.configurator.emr'



# ----------------------------------------------------------- Account -------------------------------

	warning = fields.Text(
		)

	website = fields.Char(
		)

	email = fields.Char(
		)

	company_name = fields.Char()

	company_address = fields.Char()

	company_phone = fields.Char()

	company_ruc = fields.Char()

	vspace = fields.Char(
			' ',
			readonly=True,
		)


