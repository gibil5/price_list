# -*- coding: utf-8 -*-

from __future__ import print_function
from openerp import _
from openerp.exceptions import Warning as UserError


# ----------------------------------------------------------- Exceptions -------------------------
class RequiredParameterException(Exception):
    pass


# ----------------------------------------------------------- Handle Exceptions Invoice -------------------------
#@api.multi
def handle_exceptions_invoice(self):
	"""
	Handle Exceptions Invoice
	"""
	print()
	print('PAT - Handle Exceptions Invoice')

	# Patient using RUC
	try:
		#if self.x_ruc not in [False, '']: 
		if self.x_ruc in [False, '']: 
			msg = "ERROR: Paciente con Factura, falta RUC"
			raise RequiredParameterException

		# Firm Name
		elif self.x_firm in [False, '']:
			msg = "ERROR: Paciente con Factura, falta Nombre Empresa"
			raise RequiredParameterException

		# Firm Address
		elif self.x_firm_address in [False, '']:
			msg = "ERROR: Paciente con Factura, falta Direccion Empresa"
			raise RequiredParameterException


	except RequiredParameterException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name

		raise UserError(_(msg))




# ----------------------------------------------------------- Handle Exceptions -------------------------
#@api.multi
def handle_exceptions(self):
	"""
	Handle Exceptions
	"""
	print()
	print('PAT - Handle Exceptions')

	self.init_configurator()

	if self.configurator.error_validation_patient:
		print('Error validation ACTIVE')
		handle_exceptions_id_doc(self)
	else:
		print('Error validation INACTIVE')




# ----------------------------------------------------------- Handle Exceptions Id Doc -------------------------
#@api.multi
def handle_exceptions_id_doc(self):
	"""
	Handle Exceptions
	"""
	print()
	print('PAT - Handle Exceptions - Id Doc')
	# Patient using DNI or other
	try:
		if self.x_id_doc in [False] or self.x_id_doc_type in [False] or self.x_id_doc_type_code in [False]:
			msg = "ERROR: Paciente Documento de Identidad Incompleto"
			raise RequiredParameterException

	except RequiredParameterException:
		class_name = type(self).__name__
		obj_name = self.name
		msg =  msg + '\n' + class_name + '\n' + obj_name
		raise UserError(_(msg))







# handle_exceptions
