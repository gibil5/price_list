# -*- coding: utf-8 -*-
"""
 		clos_funcs.py - 2nd Level

 		Created: 			30 Dec 2019
		Last up: 	 		30 Dec 2019

		Abstract, General purpose. Provider of services.
"""
from __future__ import print_function
import datetime

from . import lib


# ----------------------------------------------------------- Set Proof ---------------------------
def set_proof_totals(self):
	"""
	Set Proof Totals - Documentos de Pago
	"""
	print()
	print('2019 - Set Proof Totals')


	# Receipt
	self.x_type = 'receipt'
	self.rec_tot, self.serial_nr_first_rec, self.serial_nr_last_rec = lib.get_gen_totals(self)

	# Invoice
	self.x_type = 'invoice'
	self.inv_tot, self.serial_nr_first_inv, self.serial_nr_last_inv = lib.get_gen_totals(self)

	# Ticket Receipt
	self.x_type = 'ticket_receipt'
	self.tkr_tot, self.serial_nr_first_tkr, self.serial_nr_last_tkr = lib.get_gen_totals(self)

	# Ticket Invoices
	self.x_type = 'ticket_invoice'
	self.tki_tot, self.serial_nr_first_tki, self.serial_nr_last_tki = lib.get_gen_totals(self)

	# Advertisement
	self.x_type = 'advertisement'
	self.adv_tot, self.serial_nr_first_adv, self.serial_nr_last_adv = lib.get_gen_totals(self)

	# Sale Notes
	self.x_type = 'sale_note'
	self.san_tot, self.serial_nr_first_san, self.serial_nr_last_san = lib.get_gen_totals(self)




	# Credit Notes

	# Get
	state = 'credit_note'
	orders, count = lib.get_orders_by_state(self, self.date, state)

	# Init
	total = 0


	# Loop
	for order in orders:
		#total = total + order.x_amount_flow
		total = total + order.x_credit_note_amount



	# Assign
	self.crn_tot = total

	if count != 0:
		self.serial_nr_first_crn = orders[0].x_serial_nr
		self.serial_nr_last_crn = orders[-1].x_serial_nr

	# Totals Proof
	self.total_proof = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot + self.adv_tot + self.san_tot - self.crn_tot

	self.total_proof_wblack = self.rec_tot + self.inv_tot + self.tkr_tot + self.tki_tot 	#+ self.adv_tot + self.san_tot

# set_proof_totals




# ----------------------------------------------------------- Set Totals ---------------------------

def set_totals(self):
	"""
	Set All Totals
	"""
	print()
	print('2019 - Set All')


	# Get Orders
	x_type = 'all'
	orders, count = lib.get_orders(self, self.date, x_type)

	# Init
	amount_untaxed = 0
	count = 0

	# Loop
	for order in orders:
		amount_untaxed = amount_untaxed + order.amount_untaxed
		count = count + 1


	# Total
	#self.total = amount_untaxed
	self.total = amount_untaxed - self.crn_tot

# set_totals

