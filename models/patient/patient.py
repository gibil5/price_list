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
	Patient Class. 
	Inherits from Openhealth and OeHealth.
	Encapsulates Business Rules. Should not extend the Data Model.
	"""
	_inherit = 'oeh.medical.patient'




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
		#print()
		#print('Pl - Patient Validate')

		# Handle Exceptions
		exc_pat.handle_exceptions_invoice(self)

