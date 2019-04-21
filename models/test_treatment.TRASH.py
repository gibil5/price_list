

# ----------------------------------------------------------- Reset Treatment ---------------------

def reset_treatment(self):



	# Vip Card
	card = self.env['openhealth.card'].search([
													('patient_name', '=', self.patient.name),
												],
													#order='write_date desc',
													limit=1,
											)
	#print card
	#print card.patient_name
	#if card.name != False:
		#card.unlink()



	# Conter Decrease - Deprecated !!!
	#name_ctr = 'advertisement'
	#counter = self.env['openhealth.counter'].search([
	#														('name', '=', name_ctr), 
	#												],
														#order='write_date desc',
	#													limit=1,
	#												)
	#counter.decrease()
	#counter.decrease()