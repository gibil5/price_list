
	#treatment_gynecology = fields.Selection(
	#		selection=px_vars_ext._treatment_list_gynecology,
	#		required=True,
	#	)

	#@api.onchange('treatment_gynecology')
	#def _onchange_treatment_gynecology(self):
	#	if self.treatment_gynecology != False: 
	#		if self.x_type == 'service': 
	#			return { 'domain': { 
	#									'product_id': [			
	#													('type', '=', 'service'),
	#													('pl_family', '=', self.family),
	#													('pl_treatment', '=', self.treatment_gynecology),
	#													('pl_price_list', '=', '2019'),
	#												],
	#								},
	#					}






	#treatment = fields.Selection(
	#		selection=px_vars._treatment_list,
	#		required=True,
	#	)






	# Family  
	#family = fields.Selection(
	#		selection=[
	#						# Service 
	#						('consultation',	'Consultas'), 
	#						('laser',			'Láser'),
	#						('medical',			'Tratamientos Médicos'), 
	#						('cosmetology',		'Cosmiatría'),
	#			],
	#		string='Familia', 
	#	)

	# Treatment 
	#treatment = fields.Selection(
	#		selection=[
	#						('laser_quick',		'Quick'), 
	#						('laser_co2',		'Co2'), 
	#						('laser_excilite',	'Excilite'), 
	#						('laser_ipl',		'IPL'), 
	#						('laser_ndyag',		'NDYAG'), 
	#			],
	#		string='Tratamiento', 
	#	)







	# Price manual flag 
	price_manual_flag = fields.Boolean(			
			string="Precio manual",
			required=False, 
		)


	# Price manual
	price_manual = fields.Float(			
			string="Valor",
			required=False, 
		)
	

	# Zone 
	zone = fields.Many2one(
			'openhealth.zone', 
			string='Zona', 
			#create_edit=False, 
		)




	# Code 
	default_code = fields.Char(
			string="Código", 
		)



	# Price Unit 
	price_unit = fields.Float(
			'Unit Price', 
			required=True, 
			digits=dp.get_precision('Product Price'), 
			default=0.0,
		)


	# Price Sub
	price_subtotal = fields.Monetary(
			string='Subtotal', 
			readonly=True, 
			store=True,
		)


	# Currency 
	currency_id = fields.Many2one(
			related='order_id.currency_id', 
			store=True, 
			string='Currency', 
			readonly=True
		)








# ----------------------------------------------------------- On Changes ------------------------------------------------------



	# Treatment 
	@api.onchange('treatment')	
	def _onchange_treatment(self):
		#print 'jx'
		#print 'On change treatment'
		if self.treatment != False: 
			#print self.treatment
			if self.x_type == 'service': 
				return {	'domain': {	'product_id': [
														#('x_origin', '=', False),

														('type', '=', self.x_type),
														('x_family', '=', self.family),
														('x_treatment', '=', self.treatment),
														('pl_price_list', '=', '2019'),
												], 
										'zone': 	[
														('treatment', '=', self.treatment),
													], 
								},
				}





	# Zone 
	@api.onchange('zone')	
	def _onchange_zone(self):
		#print 'jx'
		#print 'On change zone'
		if self.zone != False: 
			if self.x_type == 'service': 
				return {	'domain': {	'product_id': [
														#('x_origin', '=', False),

														('type', '=', self.x_type),
														('x_family', '=', self.family),
														('x_treatment', '=', self.treatment),
														('x_zone', '=', self.zone.name_short),

														('pl_price_list', '=', '2019'),
													], 
									},
					}





	# Type 
	@api.onchange('x_type')
	def _onchange_x_type(self):
		#print 'jx'
		#print 'On change x_type'
		if self.x_type != False: 
			if self.x_type == 'product': 
				return {	'domain': {'product_id': [
														#('x_origin', '=', False),
														#('categ_id', '=', 'Cremas'),

														('type', '=', self.x_type),

														('pl_price_list', '=', '2019'),
									]},
				}
			elif self.x_type == 'service': 
				return {	'domain': {'product_id': [
														#('x_origin', '=', False),
														('type', '=', self.x_type),
														('pl_price_list', '=', '2019'),
									]},
				}


	# Default Code 
	@api.onchange('default_code')
	def _onchange_default_code(self):
		#print 'jx'
		#print 'On change default_code'
		if self.default_code != False: 
			default_code = self.default_code
			product = self.env['product.product'].search([
																	('default_code', '=', default_code),
													],
													#order='date desc',
													limit=1,
												)
			#print product
			#print product.name 
			if product.name != False:
				self.product_id = product.id


