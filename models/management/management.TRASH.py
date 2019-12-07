# 7 Dec 2019


	- A Class exposes abstract interfaces that allow its users to manipulate the Essence of the data, 
	  without having to know its Implementation. 

	- Respect the Law of Demeter. Avoid Train Wrecks.

	- Treat the Active Record as a data structure and create separate objects that contain the business rules 
	  and that hide their internal data. These Objects are just instances of the Active Record.	

	- Handle Exceptions.




# ----------------------------------------------------------- Check Statistics - Dep -----------------

	@api.multi
	def check_stats(self):
		"""
		Check Stats
		"""
		print()
		print('Check Stats')

		# Handle Exceptions
		exc_mgt.handle_exceptions(self)

		# Go
		print(self.statistics)
		print(self.statistics.name)
		#self.statistics.print()
		self.statistics.print_short()
	# check_stats



# ----------------------------------------------------------- Validate Internal - Dep -------------------------
	# Validate
	@api.multi
	def validate(self):
		"""
		Validates Data Coherency - internal and external. 
		"""
		print()
		#print('Pl - Validate')
		print('Validate')

		# Handle Exceptions
		exc_mgt.handle_exceptions(self)

		# Go
		self.pl_validate_internal()
		self.pl_validate_external()
	# validate






# 4 Sep

	def create_doctor_data(self, doctor_name, orders):

				# Amount
				#amount = amount + order.amount_total

					#amount = amount - order.amount_total
					#amount = amount - order.amount_total
					#amount = amount - order.x_credit_note_amount
					#print('Gotcha !')
					#print(amount)

						# State
						#if order.state in ['credit_note']:
						#	price_unit = -line.price_unit
						#elif order.state in ['sale']:
						#	price_unit = line.price_unit






# 29 Aug 2019


# ----------------------------------------------------------- PL - Natives ----------------------
	pl_max = fields.Boolean(
			'Max',
		)

	pl_min = fields.Boolean(
			'Min',
		)

# ----------------------------------------------------------- PL - Relational ----------------------
	# Doctor
	doctor_line = fields.One2many(
			'openhealth.management.doctor.line',
			'management_id',
		)



# ----------------------------------------------------------- Natives ----------------------

	# New Procedures

	# Echography
	nr_echo = fields.Integer(
			'Nr Ecografia',
		)
	amo_echo = fields.Float(
			'Monto Ecografia',
		)
	per_amo_echo = fields.Float(
			'% Monto Ecografia',
		)
	avg_echo = fields.Float(
			'Precio Prom. Ecografia',
		)


	# Gynecology
	nr_gyn = fields.Integer(
			'Nr Ginecologia',
		)
	amo_gyn = fields.Float(
			'Monto Ginecologia',
		)
	per_amo_gyn = fields.Float(
			'% Monto Ginecologia',
		)
	avg_gyn = fields.Float(
			'Precio Prom. Ginecologia',
		)


	# Promotions
	nr_prom = fields.Integer(
			'Nr Promocion',
		)
	amo_prom = fields.Float(
			'Monto Promocion',
		)
	per_amo_prom = fields.Float(
			'% Monto Promocion',
		)
	avg_prom = fields.Float(
			'Precio Prom. Promocion',
		)

	# Time Line
	base_dir = fields.Char()






# ----------------------------------------------------------- Natives -------------------------
	per_amo_credit_notes = fields.Float(
		)

	# Medical
	nr_sub_con_med = fields.Integer(
			'Nr Cons Med',
		)

	amo_sub_con_med = fields.Float(
			'Monto Cons Med',
		)
	
	per_amo_sub_con_med = fields.Float(
			'% Monto Cons Med',
		)

	# Gyn
	nr_sub_con_gyn = fields.Integer(
			'Nr Cons Gin',
		)

	amo_sub_con_gyn = fields.Float(
			'Monto Cons Gin',
		)
	
	per_amo_sub_con_gyn = fields.Float(
			'% Monto Cons Gin',
		)

	# Chavarri
	nr_sub_con_cha = fields.Integer(
			'Nr Cons Dr. Chav',
		)

	amo_sub_con_cha = fields.Float(
			'Monto Cons Dr. Chav',
		)
	
	per_amo_sub_con_cha = fields.Float(
			'% Monto Sub Cons Dr. Chav',
		)


	# Families and Sub Families
	per_amo_families = fields.Float(
			'% Monto Familias',
		)

	per_amo_subfamilies = fields.Float(
			'% Monto Sub Familias',
		)

	#per_amo_subfamilies_products = fields.Float(
	#		'% Monto Sub Familias Productos',
	#	)

	#per_amo_subfamilies_procedures = fields.Float(
	#		'% Monto Sub Familias Procedimientos',
	#	)


	report_sale_product = fields.Many2one(
			'openhealth.report.sale.product'
		)

	rsp_count = fields.Integer(
			'RSP Nr',
		)

	rsp_total = fields.Float(
			'RSP Monto',
		)

	rsp_count_delta = fields.Integer(
			'RSP Nr Delta',
		)

	rsp_total_delta = fields.Float(
			'RSP Total Delta',
		)








# 29 Aug 2019

# ----------------------------------------------------------- Admin ---------------------------------------------

	admin_mode = fields.Boolean()

	nr_products_stats = fields.Integer()

	nr_consultations_stats = fields.Integer()

	nr_procedures_stats = fields.Integer()



# ----------------------------------------------------------- Update Year - Fields ----------------------
	# Owner
	owner = fields.Selection(
			[
				('aggregate', 'Aggregate'),
				('month', 'Month'),
				('year', 'Year'),
				('account', 'Account'),
			],
			default='month',
			required=True,
		)

	month = fields.Selection(
			selection=pl_mgt_vars._month_order_list,
			string='Mes',
			required=True,
		)


# ----------------------------------------------------------- Relational -------------------------

	# Configurator
	configurator = fields.Many2one(
			'openhealth.configurator.emr',
			string="Config",
			required=True,
		)





