# -*- coding: utf-8 -*-
"""
Configurator - EMR

Created: 			25 Jan 2019
Last updated: 		14 Aug 2019
"""
from __future__ import print_function
from openerp import models, fields, api

class ConfiguratorEmr(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'openhealth.configurator.emr'



# ----------------------------------------------------------- 2019 Price list -------------------------------

	#path = fields.Char(
	path_csv_pricelist = fields.Char(
			required=False,
			default='/Users/gibil/cellar/github/price_list/csv/',
		)




# ----------------------------------------------------------- Important - Used by Account Contasis Line -------------------------------
	cuentab_services = fields.Char(
			'Cuentab Servicios',
		)

	cuentab_products = fields.Char(
			'Cuentab Productos',
		)

	cuentab_consu = fields.Char(
			'Cuentab Consumibles',
		)




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







# ----------------------------------------------------------- Error Validation -------------------------------

	#def validate_errors_electronic(self):
	#	"""
	#	Validate Electronic Errors ?
	#	"""
	#	print()
	#	print('Configurator - Validate Errors Electronic')
	#	if self.error_validation_electronic:
	#		return True
	#	else:
	#		return False


	error_validation_electronic = fields.Boolean(
			'Validacion de Errores Electronico',
			default=True,
		)

	error_validation_patient = fields.Boolean(
			'Validacion de Errores Paciente',
			default=True,
		)

	error_validation_order = fields.Boolean(
			'Validacion de Errores Venta',
			default=True,
		)

	error_validation_product = fields.Boolean(
			'Validacion de Errores Producto',
			default=True,
		)

	error_validation_management = fields.Boolean(
			'Validacion de Errores Reporte MGT',
			default=True,
		)

	error_validation_marketing = fields.Boolean(
			'Validacion de Errores Reporte MKT',
			default=True,
		)




# ----------------------------------------------------------- Natives -------------------------------

	name = fields.Selection(			
			[
				('Lima', 'Sede Lima'),
				('Tacna', 'Sede Tacna'),
			],
			string="Nombre",
			required=True,

			default="Lima",
		)




	company_name = fields.Char(
			required=True,

			default="SERVICIOS MÉDICOS ESTÉTICOS S.A.C",
		)

	company_address = fields.Char(
			required=True,

			default="Av. La Merced 161",
		)

	company_phone = fields.Char(
			required=True,

			default="Teléfono: (051) 321 2394",
		)

	company_ruc = fields.Char(
			required=True,

			default="20523424221",
		)

	company_ubigeo = fields.Char(
			required=True,

			default="150101",
		)

	company_country = fields.Char(
			required=True,

			default="PE",
		)

	company_account = fields.Char(
			required=True,

			default="6",
		)




	# Ticket

	website = fields.Char(
			required=True,

			default="http://www.clinicachavarri.com/",
		)

	email = fields.Char(
			required=True,

			default="info@clinicachavarri.com",
		)

	ticket_company_address = fields.Char(
			required=True,

			default="Av. La Merced 161 Miraflores - Lima",
		)

	ticket_company_ruc = fields.Char(
			required=True,

			default="R.U.C.: 20523424221",
		)

	ticket_description = fields.Text(
			required=True,

			default="Representación impresa generada por SERVICIOS MÉDICOS ESTÉTICOS S.A.C.",
		)

	ticket_warning = fields.Text(
			required=True,

			default="Por medio del presente, se informa que en caso de cancelación de tratamiento o de la consulta por parte del paciente, ya sea de manera expresa o tácita, este autoriza a la empresa la retención del 15%% del costo del tratamiento o el 25%% de la consulta, sea el caso, por concepto de gastos administrativos y gastos operativos. (Art. 67 Ley 29571, Art 40 Ley General de Salud",
		)


	#warning = fields.Text(			# dep
			#required=True,
	#	)



# ----------------------------------------------------------- Natives -------------------------------

	x_type = fields.Selection(
			[
				('emr', 'Clinica'),
			],
			string="Tipo",
			required=True,

			default="emr",
		)


	vspace = fields.Char(
			' ',
			readonly=True,
		)
