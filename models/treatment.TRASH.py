# ----------------------------------------------------------- Computes --------------------------
	@api.multi
	def _compute_nr_invoices_pro(self):
		for record in self:
			record.nr_invoices_pro = self.env['sale.order'].search_count([
																			('treatment', '=', record.id),
																			('x_family', '=', 'procedure'),
																			('state', '=', 'sale'),
																	])


	
	@api.multi
	#@api.depends('consultation_ids')
	def _compute_state(self):
		for record in self:

			# Init
			state = 'empty'


			if record.treatment_closed:
				state = 'done'

			elif record.nr_controls > 0:
				state = 'controls'

			elif record.nr_sessions > 0:
				state = 'sessions'

			elif record.nr_procedures > 0:
				state = 'procedure'

			elif record.nr_invoices_pro > 0:
				state = 'invoice_procedure'

			elif record.nr_budgets_pro > 0:
				state = 'budget_procedure'

			elif record.nr_services > 0:
				state = 'service'

			elif record.consultation_progress == 100:
				state = 'consultation'

			elif record.nr_invoices_cons > 0:
				state = 'invoice_consultation'

			elif record.nr_budgets_cons > 0:
				state = 'budget_consultation'

			elif record.nr_appointments > 0:
				state = 'appointment'


			# Assign
			record.state = state

	# _compute_state



