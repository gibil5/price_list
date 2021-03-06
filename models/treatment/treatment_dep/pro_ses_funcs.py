# -*- coding: utf-8 -*-
"""
	Procedure Session Funcs - Dep - 10 Aug 2020

	Created: 				 1 Nov 2016
	Last updated: 	 	 	25 Apr 2019
"""
from datetime import datetime
from openerp import models, fields, api
from . import time_funcs
from openerp.addons.openhealth.models.libs import user, lib

#------------------------------------------------ Create Sessions ---------------------------------------------------
@api.multi
def create_sessions(self, nr_sessions, nr_ses_created):
	"""
	Create Sessions. For Procedure.
	"""
	print()
	print('Pl - Create Sessions - Go')

	# Init
	procedure_id = self.id 
	patient_id = self.patient.id		
	chief_complaint = self.chief_complaint
	evaluation_type = 'Session'
	product_id = self.product.id
	treatment_id = self.treatment.id
	laser = self.laser

	# Actual Doctor 
	doctor_id = user.get_actual_doctor_pro(self)

	# Appointment 
	duration = 0.5

	x_type = 'session'
	subtype = self.product.x_treatment 

	doctor_name = self.doctor.name 
	
	# Date 		
	GMT = time_funcs.Zone(0,False,'GMT')
	evaluation_start_date = datetime.now(GMT).strftime("%Y-%m-%d %H:%M:%S")
	app_date = datetime.now(GMT).strftime("%Y-%m-%d ")

	# Loop 
	# Date dictionary - Number of days for controls 
	k_dic = {
				#0 :	0,
				#1 :	7,
				#2 :	15,
				#3 :	21,
				#3 :	30,
				#4 :	60,
				#5 :	120,

				0 : 0,
				
				1 :	1,
				2 :	2,
				3 :	3,
				4 :	4,
				5 :	5,
				6 :	6,
				7 :	7,
				8 :	8,
				9 :	9,
				#10 :	10,
				#11 :	11,
			}


	# Loop
	for k in range(0, nr_sessions):
		# Init 
		nr_days = nr_ses_created

		# Session date 
		session_date = lib.get_next_date(self, evaluation_start_date, nr_days)
		session_date_str = session_date.strftime("%Y-%m-%d")		

		# Create Session 
		appointment_id = False
		session = self.env['openhealth.session.med'].create({
																'patient': patient_id,
																'doctor': doctor_id,													
																'evaluation_start_date':session_date,																

																'evaluation_type':evaluation_type,
																'product': product_id,
																'laser': laser,

																'chief_complaint': chief_complaint,																
																'appointment': appointment_id,																
																'procedure': procedure_id,				

																'treatment': treatment_id,	
											})
		#session_id = session.id 


	return 0

# create_sessions_go

