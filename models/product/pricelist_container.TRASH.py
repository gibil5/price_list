
# ----------------------------------------------------------- Remove Stock Moves - Button ----------------------------------------------------
	@api.multi
	def clean_stock_moves(self):
		"""
		Cancels stock moves
		Remove manually
		"""
		print('Container Clean stock_moves')

		# Search
		moves = self.env['stock.move'].search([
													#('x_name_short', 'in', [name]),
												],
												#order='date_begin asc',
												#limit=10,
											)
		for stock_move in moves:
			#print()
			#print(stock_move)
			#print(stock_move.name)
			#print(stock_move.state)
			#stock_move.unlink()
			stock_move.state = 'cancel'

		print('Finished !')

	# clean_stock_moves



# ----------------------------------------------------------- Remove Procurement - Button ----------------------------------------------------
	@api.multi
	def clean_procurements(self):
		"""
		Cancels Procurements
		Remove manually
		"""
		print('Container Clean Procurements')

		# Search
		procs = self.env['procurement.order'].search([
															#('x_name_short', 'in', [name]),
														],
															#order='date_begin asc',
															#limit=10,
													)
		for procurement in procs:
			#print()
			#print(procurement)
			#print(procurement.name)
			#print(procurement.state)
			#procurement.unlink()
			procurement.state = 'cancel'
		
		print('Finished !')

	# clean_procurements












# ----------------------------------------------------------- Update Price list - Dep ??? ------------------------

	@api.multi
	def update_price_list(self):
		"""
		Update Price list
		"""
		print('Update Price list')

		# Search
		#products = self.env['product.product'].search([
		products = self.env['product.template'].search([
															#('x_name_short', 'in', [name]),
														],
															#order='date_begin asc',
															#limit=1,
													)
		# Count
		count = self.env['product.template'].search_count([
														],
															#order='x_serial_nr asc',
															#limit=1,
													)
		print(products)

		for pro in products:
			#print(pro.name)

			if pro.pl_price_list in [False]:
				pro.pl_price_list = '2018'

			#print(pro.pl_price_list)

		#print(count)







# ----------------------------------------------------------- Update  Dep ? ----------------------------------------------------
	@api.multi
	def update_old(self):
		"""
		Update
		"""
		print('DEP - Container Update')

		# Search
		products = self.env['price_list.product'].search([
															#('x_name_short', 'in', [name]),
														],
															#order='date_begin asc',
															#limit=1,
													)
		for product_pricelist in products:

			product_pricelist.update()

			# Search
			product_template = self.env['product.template'].search([
																		#('name', 'in', [prod.name]),
																		('name', '=', product_pricelist.name),
																		('pl_price_list', '=', '2019'),
															],
																#order='date_begin asc',
																#limit=1,
														)
			product_template.update()




			# Here !
			#if self.caps_name:
			#	name = 			row['name'].upper()
			#	name_short = 	row['name_short'].upper()
			#else:
			#	name = 			row['name']
			#	name_short = 	row['name_short']






			#self.create_product(prefix, idx, code, x_type, family, subfamily, name_short, name, treatment, zone, pathology, level, sessions, time,
			#price, price_vip, price_company, price_session, price_session_next, price_max)

		#f = open(fname, 'r')

		#my_list = []

		#with open('services.csv', 'r') as f:

		#with open(fname, 'r') as f:

		#	reader = csv.reader(f)

		#	for row in reader:
		#		print(row)
				#print(row.name)
		#		print()

				#my_list.append(myClass(row[0], row[1], row[2:]))

				# Create
				#product = self.product_ids.create({
				#										'name': name,
				#										'container_id': self.id,
				#		})
				#print(product)

				#my_list.append(product)

		#print(my_list)





	#def create_product(self, name):
		# Create
	#	product = self.product_ids.create({
	#											'name': name,
	#											'container_id': self.id,
	#			})
	#	print(product)
