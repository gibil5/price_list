# 29 Aug 2019



# ----------------------------------------------------------- Fields -----------

	x_firm_address = fields.Char(
			'Direccion de la Empresa',
		)

# ----------------------------------------------------------- Configurator ------------------------
	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Configuracion",
		)










# Before
# ----------------------------------------------------------- Natives - Dep ? -----------
	#x_blacklist = fields.Boolean(
	#		'Black List',
	#	)


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






# Before

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

