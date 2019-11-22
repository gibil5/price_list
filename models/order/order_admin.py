# -*- coding: utf-8 -*-
#
# 		*** Order Admin 
# 
# 		Created: 			21 Nov 2019
# 		Last updated: 	 	21 Nov 2019
#
from openerp import models, fields, api

from openerp.addons.openhealth.models.libs import user

class OrderAdmin(models.Model):
	
	_inherit = 'openhealth.order.admin'




# ----------------------------------------------------- Admin --------------------------
	@api.multi
	def update(self):
		"""
		Update
		"""
		print()
		print('Update')


		if self.fix_counter:

			print('Fix Counter')

			self.order.x_counter_value = self.counter
			print(self.order.x_counter_value)

			self.serial_number = user.get_serial_nr(self.order.x_type, self.counter, self.order.state)

			self.order.x_serial_nr = self.serial_number
			print(self.order.x_serial_nr)



