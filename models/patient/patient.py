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

from . import pat_exc

class Patient(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'oeh.medical.patient'




# ----------------------------------------------------------- Validate -----------
	@api.multi
	def validate(self):
		"""
		Validate Patient, for Id Doc.
		Used by Electronic Container (Txt Generation). 
		"""
		print()
		print('Pl - Patient Validate')
		#print(self.name)
		#print(self.x_id_doc)
		#print(self.x_id_doc_type)
		#print(self.x_id_doc_type_code)

		# Handle Exceptions
		pat_exc.handle_exceptions(self)




# ----------------------------------------------------------- Ensure -----------

	#@api.multi
	#def ensure_id_doc(self):
	#def ensure_id_doc_dni(self):
	#	print()
	#	print('Ensure - Id Doc')

		# Init
	#	error = 0
	#	msg = ''

	#	if self.x_id_doc in [False]	or self.x_id_doc_type in [False] or self.x_id_doc_type_code in [False]:
	#		msg = 'ERROR 1 - Paciente: La ficha personal esta incompleta. Documentos de Identidad - ' + self.name
	#		error = 1
			#raise UserError(_(msg))
			#return UserError(_(msg))
	#		return False

		#else:
			#print('Validated !')
		#	print()
		#return error, msg
	# validate



# ----------------------------------------------------------- Fields -----------

	x_firm_address = fields.Char(
			'Direccion de la Empresa',
		)



# ----------------------------------------------------------- Natives -----------
	x_blacklist = fields.Boolean(
			'Black List',
		)
