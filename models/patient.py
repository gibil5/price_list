# -*- coding: utf-8 -*-
"""
		Patient

 		Created: 		26 Aug 2016
		Last up: 		 2 May 2019
"""
from __future__ import print_function
from openerp import models, fields, api
#from . import pat_vars
#from . import pat_funcs
#from . import chk_patient
from openerp.addons.openhealth.models.libs import count_funcs



class Patient(models.Model):
	"""
	high level support for doing this and that.
	"""
	_inherit = 'oeh.medical.patient'

	#_order = 'x_id_code desc'

	#_description = 'Patient'



# ----------------------------------------------------------- Validate -----------

	@api.multi
	def validate(self):
		"""
		Validate Patient, for Id Doc.
		Used by Electronic Container (Txt Generation). 
		"""
		print()
		print('Pl - Patient Validate')

		print(self.name)
		print(self.x_id_doc)
		print(self.x_id_doc_type)
		print(self.x_id_doc_type_code)

		error = 0
		msg = ''

		if self.x_id_doc in [False]		or 	self.x_id_doc_type in [False]		or self.x_id_doc_type_code in [False]:
			print('Gotcha !')

			msg = 'ERROR - Paciente: La ficha personal esta incompleta. Documentos de Identidad - ' + self.name
			error = 1

			#raise UserError(_(msg))
		else:
			print('Validated !')

		return error, msg



