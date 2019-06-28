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




# ----------------------------------------------------------- Dep -------------------------------
	cuentab_products = fields.Char(
			'Cuentab Productos',
		)

	cuentab_services = fields.Char(
			'Cuentab Servicios',
		)

	cuentab_consu = fields.Char(
			'Cuentab Consumibles',
		)



# ----------------------------------------------------------- Natives -------------------------------

	company_name = fields.Char()

	company_address = fields.Char()

	company_phone = fields.Char()

	company_ruc = fields.Char()

	company_ubigeo = fields.Char()

	company_country = fields.Char()

	company_account = fields.Char()




	# Ticket

	website = fields.Char(
		)

	email = fields.Char(
		)

	ticket_company_address = fields.Char()

	ticket_company_ruc = fields.Char()

	ticket_description = fields.Text()

	ticket_warning = fields.Text()

	warning = fields.Text(
		)



# ----------------------------------------------------------- Natives -------------------------------

	x_type = fields.Selection(
			[
				('emr', 'Clinica'),
			],
			string="Tipo",
			required=True,
		)


	vspace = fields.Char(
			' ',
			readonly=True,
		)
