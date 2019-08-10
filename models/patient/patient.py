# -*- coding: utf-8 -*-
"""
		Patient

 		Created: 		26 Aug 2016
		Last up: 		 6 Aug 2019

	- A Class exposes abstract interfaces that allow its users to manipulate the Essence of the data, 
	  without having to know its Implementation.

	- Respect the Law of Demeter. Avoid Train Wrecks.

	- Treat the Active Record as a data structure and create separate objects that contain the business rules 
	  and that hide their internal data. These Objects are just instances of the Active Record.	

	- Handle Exceptions.
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.libs import count_funcs

from . import exc_pat

class Patient(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'oeh.medical.patient'



# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)


	def init_configurator(self):
		"""
		Init Configurator
		"""
		#print()
		#print('Init Configurator')

		# Configurator
		if self.configurator.name in [False]:
			self.configurator = self.env['openhealth.configurator.emr'].search([
																					('x_type', 'in', ['emr']),
															],
															#order='date_begin,name asc',
															limit=1,
														)
			#print(self.configurator)
			#print(self.configurator.name)





# ----------------------------------------------------------- Validate -----------
	@api.multi
	def validate(self):
		"""
		Validate Patient, for Id Doc.
		Triggered by all Buttons
		"""
		print()
		print('Pl - Patient Validate')

		# Handle Exceptions
		exc_pat.handle_exceptions(self)



# ----------------------------------------------------------- Validate -----------
	@api.multi
	def validate_for_invoice(self):
		"""
		Validate Patient, for Invoice
		Used by Electronic Container (Txt Generation). 
		"""
		print()
		print('Pl - Patient Validate')

		# Handle Exceptions
		exc_pat.handle_exceptions_invoice(self)






# ----------------------------------------------------------- Fields -----------

	x_firm_address = fields.Char(
			'Direccion de la Empresa',
		)

# ----------------------------------------------------------- Natives -----------
	x_blacklist = fields.Boolean(
			'Black List',
		)
