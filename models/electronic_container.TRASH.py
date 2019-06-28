
# ----------------------------------------------------------- Correct ------------------------------
	correct_patient = fields.Many2one(
			'oeh.medical.patient',
		)

	@api.multi
	def correct(self):
		"""
		high level support for doing this and that.
		"""
		print()
		print('Pl - Correct')

		patient = self.correct_patient

		#print()
		#print(patient.name)
		#print(patient.x_id_doc_type)
		#print(patient.x_id_doc_type_code)
		#print(patient.x_id_doc)
		#print(patient.x_dni)

		if patient.x_id_doc in [False]:
			if patient.x_dni not in [False]:
				patient.x_id_doc = patient.x_dni
				patient.x_id_doc_type = 'dni'


