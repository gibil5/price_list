#------------------------------------------------ Create Controls ---------------------------------
# Create Controls
def create_controls(self, nr_controls, nr_ctl_created):
	"""
	Creates Controls for the Procedure Class.
	"""

	# Clean - Deprecated
	#rec_set = self.env['openhealth.control'].search([
	#													('procedure', '=', self.id),
	#												])
	#ret = rec_set.unlink()


	#for k in range(0, nr_controls):


		#if nr_ctl_created < 6:
		#	nr_days = k_dic[nr_ctl_created]
		#else:
		#	nr_days = 7



		# Appointment

		# Create App - Dep !
		if False:
			duration = 0.25
			state = 'pre_scheduled_control'
			states = ['pre_scheduled_control']
			x_type = 'control'

			# Check and Push
			appointment_date_str = user.check_and_push(self, control_date_str, duration, doctor_name, states)

			# Create Appointment
			appointment = self.env['oeh.medical.appointment'].create({
																		'appointment_date': appointment_date_str,

																		'patient': patient_id,
																		'doctor': doctor_id,
																		'duration': duration,
																		'state': state,
																		'x_chief_complaint': chief_complaint,
																		'x_create_procedure_automatic': False,
																		'x_target': 'doctor',
																		'x_type': x_type,
																		'x_subtype': subtype,

																		'treatment': treatment_id,
																	})
			appointment_id = appointment.id



											#'evaluation_start_date':control_date,
											#'first_date':control_date,


		control_id = control.id

		# Update Appointments
		if False:
			rec_set = self.env['oeh.medical.appointment'].browse([appointment_id])
			ret = rec_set.write({
									'control': control_id,
									'procedure': procedure_id,
								})

			