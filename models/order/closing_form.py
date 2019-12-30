# -*- coding: utf-8 -*-
"""
 	Closing Form

	Created: 			30 Dec 2019
	Last up: 	 		30 Dec 2019
"""
from __future__ import print_function
from openerp import models, fields, api

from . import lib

class ClosingForm(models.Model):
	"""
	Closing Form
	Forms of payment - cash, card, bank
	"""
	_name = 'openhealth.closing.form'




# ----------------------------------------------------------- Set Form Total ----------------------------
	def analyse(self):
		"""
		Analyses - Forms of payment
		"""
		print()
		print('CF - Analyse')



		# Get Orders
		orders, count = lib.get_orders_by_state_all(self, self.date)  		# Only used by Closings
		#print(orders)
		#print(count)



		# Init
		cash_tot = 0
		ame_tot = 0
		din_tot = 0
		mac_tot = 0
		mad_tot = 0
		vic_tot = 0
		vid_tot = 0

		bbva_tot = 0
		scotiabank_tot = 0
		interbank_tot = 0
		bcp_tot = 0


		# Loop
		for order in orders:

			print(order.state)


			# Conditional
			#if order.state == 'credit_note':
			if order.state == 'credit_note'		and 	not order.x_block_flow:
				payment_method = order.x_credit_note_owner.x_payment_method
				coeff = -1

			else:
				payment_method = order.x_payment_method
				coeff = 1



			# Loop
			for pm_line in payment_method.pm_line_ids:

				#print('mark')
				#print(pm_line.method)


				subtotal = pm_line.subtotal * coeff


				# Standard - Cash and Cards
				if pm_line.method == 'cash':
					cash_tot = cash_tot + subtotal

				elif pm_line.method == 'american_express':
					ame_tot = ame_tot + subtotal

				elif pm_line.method == 'diners':
					din_tot = din_tot + subtotal

				elif pm_line.method == 'credit_master':
					mac_tot = mac_tot + subtotal

				elif pm_line.method == 'debit_master':
					mad_tot = mad_tot + subtotal

				elif pm_line.method == 'credit_visa':
					vic_tot = vic_tot + subtotal

				elif pm_line.method == 'debit_visa':
					vid_tot = vid_tot + subtotal


				# New - Banks
				elif pm_line.method == 'bbva':
					bbva_tot = bbva_tot + subtotal

				elif pm_line.method == 'interbank':
					interbank_tot = interbank_tot + subtotal

				elif pm_line.method == 'scotiabank':
					scotiabank_tot = scotiabank_tot + subtotal

				elif pm_line.method == 'bcp':
					bcp_tot = bcp_tot + subtotal




		# Form
		self.cash = cash_tot
		self.american = ame_tot
		self.diners = din_tot

		self.master_credit = mac_tot
		self.master_debit = mad_tot
		self.visa_credit = vic_tot

		self.visa_debit = vid_tot
		self.bbva = bbva_tot
		self.interbank = interbank_tot

		self.scotia = scotiabank_tot
		self.bcp = bcp_tot

		#return cash_tot, ame_tot, din_tot, 	mac_tot, mad_tot, vic_tot, 		vid_tot, bbva_tot, interbank_tot, 	scotia, bcp

		#return cash, american, diners, 	master_credit, master_debit, visa_credit, 		visa_debit, bbva, interbank, 	scotia, bcp

	# analyse




# ----------------------------------------------------------- Get Totals -----------------------
	def get_totals(self):
		"""
		Get Totals
		"""
		print()
		print('CF - Get Totals')

		return self.cash, self.american, self.diners, self.master_credit, self.master_debit, self.visa_credit, self.visa_debit, self.bbva, self.interbank, 	self.scotia, self.bcp



# ----------------------------------------------------------- Fields -----------------------
	name = fields.Char()


	date = fields.Date(
			string="Fecha",
			default=fields.Date.today,
			#readonly=True,
			required=True,
		)



	# Totals
	cash = fields.Float()

	american = fields.Float()

	diners = fields.Float()

	master_credit = fields.Float()

	master_debit = fields.Float()
	
	visa_credit = fields.Float()
	
	visa_debit = fields.Float()
	
	bbva = fields.Float()
	
	interbank = fields.Float()
	
	scotia = fields.Float()

	bcp_tot = fields.Float()



