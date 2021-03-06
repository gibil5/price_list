# -*- coding: utf-8 -*-
"""
	patient Line

	Created: 			20 Jun 2019
	Last up: 			20 Jun 2019
"""
from __future__ import print_function
from openerp import models, fields, api
from openerp.addons.openhealth.models.patient import pat_vars
from openerp.addons.price_list.models.management.lib import pl_mgt_funcs

class PatientLine(models.Model):
	"""
	Patient lines
	"""
	_name = 'openhealth.management.patient.line'

	_order = 'amount_total desc'


# ----------------------------------------------------------- Handles -----------------------------

	# Management 
	management_id = fields.Many2one(
			'openhealth.management',
			ondelete='cascade',
		)


	# Patient
	patient = fields.Many2one(
			'oeh.medical.patient',
			#string='Paciente',
		)


	amount_total = fields.Float()

	count_total = fields.Integer()


	# Age
	age = fields.Char(
			#string="Edad",
		)

	# Sex
	sex = fields.Selection(

			selection=pat_vars.get_sex_type_list(),

			#string="Sexo",
			#required=False,
		)



# ----------------------------------------------------------- Update -------------------------
	# Update
	@api.multi
	def update(self):
		"""
		Update 
		"""
		print()
		print('X - Update')


		self.sex = self.patient.sex
		self.age = self.patient.age

		self.amount_total = 0
		self.count_total = 0


		# Get Orders
		orders, count = pl_mgt_funcs.get_orders_filter_by_patient_fast(self, self.patient.id)
		#print(orders)
		#print(count)


		for order in orders:
			self.amount_total = self.amount_total + order.x_amount_flow

			for line in order.order_line:
				self.count_total = self.count_total + line.product_uom_qty


