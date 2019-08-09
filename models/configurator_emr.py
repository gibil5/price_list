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
	_inherit = 'openhealth.configurator.emr'



# ----------------------------------------------------------- Dep ! -------------------------------
	#cuentab_products = fields.Char(
	#		'Cuentab Productos',
	#	)

	#cuentab_services = fields.Char(
	#		'Cuentab Servicios',
	#	)

	#cuentab_consu = fields.Char(
	#		'Cuentab Consumibles',
	#	)




# ----------------------------------------------------------- Get Inactive Days -------------------------------

	def get_inactive_days(self):
		"""
		Gets Inactive Days. From Configurator.
		"""
		print()
		print('Configurator - Get Inactive Days')

		days_inactive = []

		if self.name not in [False]:		
			for day in self.day_line:								# Respects the LOD
				if day.holiday:
					days_inactive.append(day.date)

		return days_inactive







# ----------------------------------------------------------- Natives -------------------------------

	def validate_errors_electronic(self):
		"""
		Validate Electronic Errors ?
		"""
		print()
		print('Configurator - Validate Errors Electronic')

		if self.error_electronic_validation:
			return True
		else:
			return False




	#validate_errors_electronic = fields.Boolean(
	error_electronic_validation = fields.Boolean(
			'Validacion de Errores Electronicos',
			default=False,
		)



	company_name = fields.Char(
			required=True,
		)

	company_address = fields.Char(
			required=True,
		)

	company_phone = fields.Char(
			required=True,
		)

	company_ruc = fields.Char(
			required=True,
		)

	company_ubigeo = fields.Char(
			required=True,
		)

	company_country = fields.Char(
			required=True,
		)

	company_account = fields.Char(
			required=True,
		)




	# Ticket

	website = fields.Char(
			required=True,
		)

	email = fields.Char(
			required=True,
		)

	ticket_company_address = fields.Char(
			required=True,
		)

	ticket_company_ruc = fields.Char(
			required=True,
		)

	ticket_description = fields.Text(
			required=True,
		)

	ticket_warning = fields.Text(
			required=True,
		)

	warning = fields.Text(
			#required=True,
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
