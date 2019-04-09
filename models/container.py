# -*- coding: utf-8 -*-

from __future__ import print_function
import csv
import pandas

from openerp import models, fields, api
#import product
from . import pl_vars


class Container(models.Model):

	_name = 'price_list.container'

	_description = 'container'

	#_inherit = 'sale.order'

	#_order = 'date_begin asc'




# ---------------------------------------------- Fields -----------------------

	name = fields.Char(
			required=True,
		)


	path = fields.Char(
			required=True,
		)

	file_name = fields.Selection(

			selection=pl_vars._file_name_list,
		
			required=True,
		)




# ----------------------------------------------------------- Relational --------------------------
	product_ids = fields.One2many(
			'price_list.product',

			'container_id',		
		)


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
			print(pro.name)

			if pro.pl_price_list in [False]:
				pro.pl_price_list = '2018'

			print(pro.pl_price_list)


		print(count)
		







# ----------------------------------------------------------- Load ------------------------

	# Load
	@api.multi
	def load(self):
		print('Load')

		self.product_ids.unlink()


		#fname = '/Users/gibil/Virtualenvs/loader/loader/services.csv'
		fname = self.path + self.file_name

		df = self.open_with_pandas_read_csv(fname)

		print(df)

		for index, row in df.iterrows():

			#print(row['idx'], row['name'])

			product = self.product_ids.create({
												'name': 			row['name'],

												'prefix': 			row['prefix'],
												'idx': 				row['idx'],

												#'code': 			row['code'],
												'code': 			False,

												'x_type': 			row['x_type'],
												'family': 			row['family'],
												'subfamily': 		row['subfamily'],

												'name_short': 		row['name_short'],
												'treatment': 		row['treatment'],
												'zone': 			row['zone'],
												'pathology': 		row['pathology'],


												'level': 			row['level'],
												'sessions': 		row['sessions'],
												'time': 			row['time'],

												'price': 			row['price'],
												'price_vip': 		row['price_vip'],
												'price_company': 	row['price_company'],
												
												'price_session': 		row['price_session'],
												'price_session_next': 	row['price_session_next'],
												'price_max': 			row['price_max'],


												'container_id': 	self.id,
											})
			print(product)



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
