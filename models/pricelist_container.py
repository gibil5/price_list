# -*- coding: utf-8 -*-
"""
	Container

	Created: 			23 Apr 2019
	Last updated: 		23 Apr 2019
"""
from __future__ import print_function
import pandas
from openerp import models, fields, api
from . import px_vars

class PricelistContainer(models.Model):
	"""
	Container
	"""
	_name = 'price_list.container'

	_description = 'container'




# ----------------------------------------------------------- Relational --------------------------
	product_ids = fields.One2many(
			'price_list.product',
			'container_id',
		)


# ----------------------------------------------------------- Load ----------------------------------------------------
	@api.multi
	def load(self):
		"""
		Load CSV data
		"""
		print('Load')

		self.product_ids.unlink()

		fname = self.path + self.file_name

		df = self.open_with_pandas_read_csv(fname)

		#print(df)

		# Loop
		for index, row in df.iterrows():
			#print(row['idx'], row['name'])
			#print(row['name'])
			#print(row['name_short'])


			# Check Values
			level = self.check(row['level'])
			time = self.check(row['time'])
			price = self.check(row['price'])
			price_vip = self.check(row['price_vip'])
			price_company = self.check(row['price_company'])
			price_session = self.check(row['price_session'])
			price_session_next = self.check(row['price_session_next'])
			price_max = self.check(row['price_max'])

			time_stamp = row['time_stamp']


			if row['x_type'] in ['product']:
				manufacturer = row['manufacturer']
				brand = row['brand']
				name = row['name'].upper()
				name_short = row['name_short'].upper()
			else:
				manufacturer = False
				brand = False
				name = row['name']
				name_short = row['name_short']


			# Here !
			#if self.caps_name:
			#	name = 			row['name'].upper()
			#	name_short = 	row['name_short'].upper()
			#else:
			#	name = 			row['name']
			#	name_short = 	row['name_short']



			# Create
			product = self.product_ids.create({
												'name': 			name,
												'name_short': 		name_short,

												'time_stamp': 		time_stamp,

												'prefix': 			row['prefix'],
												'idx': 				row['idx'],

												#'code': 			row['code'],
												'code': 			False,

												'x_type': 			row['x_type'],
												'family': 			row['family'],
												'subfamily': 		row['subfamily'],
												'treatment': 		row['treatment'],
												'zone': 			row['zone'],
												'pathology': 		row['pathology'],
												'sessions': 		row['sessions'],
												'level': 			level,
												
												'time': 				time,
												'price': 				price,
												'price_vip': 			price_vip,
												'price_company': 		price_company,
												'price_session': 		price_session,
												'price_session_next': 	price_session_next,
												'price_max': 			price_max,

												# Only Prods
												'manufacturer': 	manufacturer,
												'brand': 			brand,

												'container_id': 	self.id,
											})
			#print(product)
	# load





# ----------------------------------------------------------- Remove Procurement ----------------------------------------------------
	@api.multi
	def clean_procurements(self):
		"""
		Remove Procurement
		"""
		print('Container Clean Procurements')

		# Search
		procs = self.env['procurement.order'].search([
															#('x_name_short', 'in', [name]),
															#('product_id', '=', 'PROTECTOR SOLAR - H'),
															#('product_id', '=', 'PROTECTOR SOLAR'),
														],
															#order='date_begin asc',
															#limit=10,
													)
		for procurement in procs:
			#print(procurement)
			#print(procurement.name)
			procurement.state = 'cancel'
			#print(procurement.state)
			#procurement.unlink()
			#print()
		
		print('Finished !')




# ----------------------------------------------------------- Remove Stock Moves ----------------------------------------------------
	@api.multi
	def clean_stock_moves(self):
		"""
		Remove stock_move
		"""
		print('Container Clean stock_moves')

		# Search
		moves = self.env['stock.move'].search([
															#('x_name_short', 'in', [name]),
															#('product_id', '=', 'PROTECTOR SOLAR - H'),
															#('product_id', '=', 'PROTECTOR SOLAR'),
														],
															#order='date_begin asc',
															#limit=10,
													)
		for stock_move in moves:
			#print(stock_move)
			#print(stock_move.name)
			stock_move.state = 'cancel'
			#print(stock_move.state)
			#stock_move.unlink()
			#print()

		print('Finished !')




# ----------------------------------------------------------- Update ----------------------------------------------------
	@api.multi
	def update(self):
		"""
		Update
		"""
		print('Container Update')


		# Search
		products = self.env['product.template'].search([
															#('x_name_short', 'in', [name]),
															('pl_price_list', '=', '2019'),
														],
															#order='date_begin asc',
															#limit=1,
													)
		for product in products:
			#print(product.name)
			product.update()






# ----------------------------------------------------------- Update ----------------------------------------------------
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



# ---------------------------------------------- Fields -----------------------

	file_name = fields.Selection(
			selection=px_vars._file_name_list,
			required=True,
		)

	name = fields.Char(
			required=True,
		)

	path = fields.Char(
			required=True,
		)








# ----------------------------------------------------------- Create Products 2019 ------------------------

	@api.multi
	def create_products_2019(self):
		"""
		Create Products 2019
		"""
		print()
		print('Create Products 2019')



		# Search
		products = self.env['price_list.product'].search([
															#('x_name_short', 'in', [name]),
														],
															#order='date_begin asc',
															#limit=1,
													)
		# Count
		count = self.env['price_list.product'].search_count([
														],
															#order='x_serial_nr asc',
															#limit=1,
													)


		for pro in products:

			#print(pro.name)


			count = self.env['product.template'].search_count([
																('name', '=', pro.name),
																('pl_price_list', '=', '2019'),
														])
			#print(count)


			if count == 0:

				product_template = self.env['product.template'].create({
																			'pl_price_list': 	'2019',

																			'pl_time_stamp': 	pro.time_stamp,



																			'type': 			pro.x_type,

																			'name': 			pro.name,
																			'pl_name_short': 	pro.name_short,

																			'pl_prefix': 		pro.prefix,
																			'pl_idx': 			pro.idx,
																			'pl_idx_int': 		pro.idx_int,

																			'pl_family': 		pro.family,
																			'pl_subfamily':		pro.subfamily,

																			'pl_treatment': 	pro.treatment,
																			'pl_zone': 			pro.zone,
																			'pl_pathology': 	pro.pathology,
																			'pl_level': 		pro.level,
																			'pl_sessions': 		pro.sessions,
																			'pl_time': 			pro.time,

																			'list_price': 				pro.price,
																			'pl_price_vip': 			pro.price_vip,
																			'pl_price_company': 		pro.price_company,
																			'pl_price_session': 		pro.price_session,
																			'pl_price_session_next': 	pro.price_session_next,
																			'pl_price_max': 			pro.price_max,


																			# Only Prods
																			'pl_manufacturer': 			pro.manufacturer,
																			'pl_brand': 				pro.brand,
																})

				#print(product_template)


		#print(products)
		#print(count)




# ----------------------------------------------------------- Update Price list ------------------------

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






	def check(self, value):
		"""
		Check var
		"""
		#print('Check')
		#print(value)

		if value in ['-1', -1]:
			#print('Gotcha !')
			return False
		else:
			return value



	caps_name = fields.Boolean(
			default=False,
		)






	def open_with_pandas_read_csv(self, filename):
		"""
		Open with Pandas
		"""
		csv_delimiter = ","
		df = pandas.read_csv(filename, sep=csv_delimiter)
		#data = df.values
		#data = df
		#return data
		return df



	#def create_product(self, name):
		# Create
	#	product = self.product_ids.create({
	#											'name': name,
	#											'container_id': self.id,
	#			})
	#	print(product)
