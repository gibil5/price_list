# -*- coding: utf-8 -*-

from __future__ import print_function
import csv
import pandas

from openerp import models, fields, api
#import product
from . import px_vars


class Container(models.Model):

	_name = 'price_list.container'

	_description = 'container'

	#_inherit = 'sale.order'

	#_order = 'date_begin asc'




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





# ----------------------------------------------------------- Relational --------------------------
	product_ids = fields.One2many(
			'price_list.product',

			'container_id',		
		)



# ----------------------------------------------------------- Create Products 2019 ------------------------

	@api.multi
	def create_products_2019(self):
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


# ----------------------------------------------------------- Load ------------------------

	# Load
	@api.multi
	def load(self):
		print('Load')

		self.product_ids.unlink()


		#fname = '/Users/gibil/Virtualenvs/loader/loader/services.csv'
		fname = self.path + self.file_name

		df = self.open_with_pandas_read_csv(fname)

		#print(df)

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



			if row['x_type'] in ['product']:
				manufacturer = row['manufacturer']
				brand = row['brand']
			else:
				manufacturer = False
				brand = False



			# Here !
			if self.caps_name:
				name = 			row['name'].upper()
				name_short = 	row['name_short'].upper()

			else:
				name = 			row['name']
				name_short = 	row['name_short']




			time_stamp = row['time_stamp']



			product = self.product_ids.create({
												'time_stamp': 			time_stamp,


												#'name': 			row['name'],
												#'name_short': 		row['name_short'],
												'name': 			name,
												'name_short': 		name_short,


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



												#'level': 			row['level'],
												#'time': 			row['time'],
												'level': 			level,
												'time': 			time,



												#'price': 				row['price'],
												#'price_vip': 			row['price_vip'],
												#'price_company': 		row['price_company'],
												#'price_session': 		row['price_session'],
												#'price_session_next': 	row['price_session_next'],
												#'price_max': 			row['price_max'],

												'price': 				price,
												'price_vip': 			price_vip,
												'price_company': 		price_company,												
												'price_session': 		price_session,
												'price_session_next': 	price_session_next,
												'price_max': 			price_max,



												# Only Prods
												#'manufacturer': 	row['manufacturer'],
												#'brand': 			row['brand'],
												'manufacturer': 	manufacturer,
												'brand': 			brand,


												'container_id': 	self.id,
											})
			#print(product)



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





	def open_with_pandas_read_csv(self, filename):
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
