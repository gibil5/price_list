# -*- coding: utf-8 -*-
"""
 		clos_funcs.py

 		Created: 			       2016
		Last up: 	 		 4 Sep 2018
"""
from __future__ import print_function
import datetime
from openerp.addons.openhealth.models.order import clos_funcs



# ----------------------------------------------------------- Set Form ----------------------------

#def set_form_totals(self):
def pl_set_form_totals(self):
	"""
	Object oriented. 
	User of services.
	"""
	print()
	print('Pl - Set By Form')

	# Get Orders
	x_type = 'all'
	#orders, count = get_orders(self, self.date, x_type)
	orders, count = clos_funcs.get_orders(self, self.date, x_type)

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


		for pm_line in order.x_payment_method.pm_line_ids:

			# Standard - Cash and Cards
			if pm_line.method == 'cash':
				cash_tot = cash_tot + pm_line.subtotal

			elif pm_line.method == 'american_express':
				ame_tot = ame_tot + pm_line.subtotal

			elif pm_line.method == 'diners':
				din_tot = din_tot + pm_line.subtotal

			elif pm_line.method == 'credit_master':
				mac_tot = mac_tot + pm_line.subtotal

			elif pm_line.method == 'debit_master':
				mad_tot = mad_tot + pm_line.subtotal

			elif pm_line.method == 'credit_visa':
				vic_tot = vic_tot + pm_line.subtotal

			elif pm_line.method == 'debit_visa':
				vid_tot = vid_tot + pm_line.subtotal


			# New - Banks
			elif pm_line.method == 'bbva':
				bbva_tot = bbva_tot + pm_line.subtotal

			elif pm_line.method == 'interbank':
				interbank_tot = interbank_tot + pm_line.subtotal

			elif pm_line.method == 'scotiabank':
				scotiabank_tot = scotiabank_tot + pm_line.subtotal

			elif pm_line.method == 'bcp':
				bcp_tot = bcp_tot + pm_line.subtotal




	# Form
	#self.cash_tot = cash_tot
	self.cash_tot = cash_tot - self.crn_tot
	self.ame_tot = ame_tot
	self.din_tot = din_tot
	self.mac_tot = mac_tot
	self.mad_tot = mad_tot
	self.vic_tot = vic_tot
	self.vid_tot = vid_tot

	self.bbva_tot = bbva_tot
	self.interbank_tot = interbank_tot
	self.scotiabank_tot = scotiabank_tot
	self.bcp_tot = bcp_tot

# set_form_totals

