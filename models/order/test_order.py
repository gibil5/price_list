# -*- coding: utf-8 -*-
"""
		TestOrder - Pricelist

		Created: 			23 Jul 2020
		Last mod: 			23 Jul 2020

	    This can be a test class.

        Todo
            - Replace self with order
"""

#from openerp import models, fields, api

#class TestOrder(models.Model):
class TestOrder():
	"""
	This encapsultes all Order tests.
	"""

# ----------------------------------------------------------- Test - Ticket Raw Lines ----------------

	# Test Raw Receipt
	@api.multi
	def test_raw_receipt(self):
		"""
		Test Ticket Printing - Receipt
		"""
		print()
		print('Test Raw Receipt')

		x_type = 'ticket_receipt'
		state = 'sale'

		action = self.test_raw_lines(x_type, state)

		return action



	# Test Raw Invoice
	@api.multi
	def test_raw_invoice(self):
		"""
		Test Ticket Printing - Invoice
		"""
		print()
		print('Test Raw Invoice')

		x_type = 'ticket_invoice'
		state = 'sale'

		action = self.test_raw_lines(x_type, state)

		return action



	# Test Raw Receipt - Credit Note
	@api.multi
	def test_raw_credit_note(self):
		"""
		Test Ticket Printing - Credit Note
		"""
		print()
		print('Test Raw Credit Note')

		x_type = 'ticket_receipt'
		state = 'credit_note'

		action = self.test_raw_lines(x_type, state)

		return action


	# Test Raw Line
	@api.multi
	def test_raw_lines(self, x_type, state):
		"""
		Test Ticket Printing
		Used by All
		"""
		#print()
		#print('Test Raw Lines')

		# Orders
		orders = self.env['sale.order'].search([
													('x_type', 'in', [x_type]),

													('patient', '=', self.patient.id),
													('state', 'in', [state]),
											],
												order='date_order desc',
												limit=1,
											)
		#print(orders)

		# Orders
		for order in orders:
			action = order.print_ticket_electronic()
			return action



# ----------------------------------------------------------- Test - Serial Number ----------------
#jx
	# Test Raw Receipt
	@api.multi
	def test_serial_number(self):
		"""
		Unit Testing
		Cover all possible Test Cases !
		"""
		print()
		print('Test Serial Number')

		tc_arr = [
				('ticket_receipt', 'sale'),
				('ticket_receipt', 'cancel'),
				('ticket_receipt', 'credit_note'),
				('ticket_invoice', 'sale'),
				('ticket_invoice', 'cancel'),
				('ticket_invoice', 'credit_note'),
				# Not electronic
				#('receipt', 'sale'),
				#('invoice', 'sale'),
				#('advertisement', 'sale'),
				#('sale_note', 'sale'),
		]


		for tc in tc_arr:
			print()
			print(tc)

			x_type = tc[0]
			state = tc[1]
			#print(x_type, state)

			# Get Next Counter
			counter = ord_funcs.get_next_counter_value(self, x_type, state)

			# Make Serial Number
			serial_number = ord_funcs.get_serial_nr(x_type, counter, state)

			print(counter)
			print(serial_number)
			print()
