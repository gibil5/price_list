

#------------------------------------------------ Create Sessions ---------------------------------------------------
@api.multi
def create_sessions(self, nr_sessions, nr_ses_created):
	"""
	Create Sessions. For Procedure.
	"""
	#cosmetology_id = self.cosmetology.id  		# Dep !!!

	#doctor_id = procedure_funcs.get_actual_doctor(self)


		#session_date = procedure_funcs.get_next_date(self, evaluation_start_date, nr_days)



		# Create App - Dep !
		if False:
			# First - Today - The app already exists !
			if k == 0:
				
				appointment_date = session_date_str + ' '

				#print app_date
				#print appointment_date

				# Search Appointment 
				appointment = self.env['oeh.medical.appointment'].search([ 	
																			#('appointment_date', '=', app_date),
																			('appointment_date', 'like', app_date),
																			('patient', '=', self.patient.name),	
																			('doctor', '=', self.doctor.name),
																			#('x_type', '=', 'session'), 
																			('x_type', '=', 'procedure'), 
																			('x_subtype', '=', subtype), 
																		], 
																			order='appointment_date desc', limit=1)
				#print appointment



			else: 	# Create Appointment 

				#appointment_date_str = session_date_str + ' 14:0:0'
				appointment_date_str = session_date_str + ' 15:0:0'


				states = False

				# Check and push 
				#appointment_date_str = procedure_funcs.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)
				appointment_date_str = user.check_and_push(self, appointment_date_str, duration, x_type, doctor_name, states)



				# Create Appointment 
				#state = 'pre_scheduled_control'
				state = 'pre_scheduled_session'

				appointment = self.env['oeh.medical.appointment'].create({
																			'appointment_date': appointment_date_str,
																			'patient': patient_id,
																			'doctor': doctor_id,
																			'duration': duration,
																			'state': state,
																			'x_type': x_type,
																			'x_subtype': subtype,

																			'procedure': self.id,
																			'treatment': treatment_id, 
																	})
			appointment_id = appointment.id
			#print appointment
			#print appointment_id


