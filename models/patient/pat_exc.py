# -*- coding: utf-8 -*-

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError


# ----------------------------------------------------------- Exceptions -------------------------
class RequiredParameterException(Exception):
    pass




# ----------------------------------------------------------- Handle Exceptions -------------------------

#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	print()
	print('PAT - Handle Exceptions')

	# Patient using RUC
	try:
		if self.x_ruc not in [False, '']: 

			# Firm Name
			if self.x_firm in [False, '']:
				msg = "ERROR 2: Paciente con RUC, falta Nombre Empresa"
				raise RequiredParameterException

			# Firm Address
			if self.x_firm_address in [False, '']:
				msg = "ERROR 3: Paciente con RUC, falta Direccion Empresa"
				raise RequiredParameterException

	except RequiredParameterException:
		raise UserError(_(msg))



	# Patient using DNI or other
	try:
		if self.x_id_doc in [False] or self.x_id_doc_type in [False] or self.x_id_doc_type_code in [False]:
			raise RequiredParameterException

	except RequiredParameterException:
		msg = "ERROR 1: Paciente Documento de Identidad Incompleto"
		raise UserError(_(msg))

# handle_exceptions
