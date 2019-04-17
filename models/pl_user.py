# -*- coding: utf-8 -*-
"""
		user.py

 		Bussiness oriented.
 		Can not be Unit-tested (depends on a third-party library: Odoo).

 		Created: 			13 Aug 2018
 		Last up: 	 		 7 Feb 2019
"""
#import datetime

#from openerp.addons.openhealth.models.order import ord_vars






#------------------------------------------------ Get Actual Doctor -------------------------------
# Get Actual Doctor
def get_actual_doctor(self):
	"""
	high level support for doing this and that.
	"""
	#print
	#print 'Get Actual Doctor'

	user_name = self.env.user.name

	doctor = self.env['oeh.medical.physician'].search([
															('x_user_name', '=', user_name),
														],
														#order='appointment_date desc',
														limit=1
													)
	return doctor
# get_actual_doctor









