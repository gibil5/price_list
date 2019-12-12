# 12 Dec 2019



# ----------------------------------------------------------- Media -------------------------------
def build_media(self):  
	print()
	print('X - Build Media')

	# Clear 
	self.media_line.unlink()


	# Build 
	media_arr = [
					'none', 
					'recommendation', 
					'tv', 
					'internet', 
					'website', 
					'mail', 
					'undefined', 
				]

	idx = 0 

	for media in media_arr: 

		if media == 'none': 
			count = self.how_none
		
		elif media == 'recommendation': 
			count = self.how_reco
		
		elif media == 'tv': 
			count = self.how_tv

		elif media == 'internet': 
			count = self.how_inter

		elif media == 'website': 
			count = self.how_web

		elif media == 'mail': 
			count = self.how_mail

		elif media == 'undefined': 
			count = self.how_u  

		total = self.total_count


		line = self.media_line.create({
										'name' : 	media, 
										'count' :		count, 
										'idx' : 		idx, 
										'total' :		total, 
										'marketing_id' :		self.id, 
									})

		line.update_fields()
		idx = idx + 1

# build_media




# ----------------------------------------------------------- Cities ------------------------------
def build_cities(self):
	print() 
	print('X - Build Cities')


	city_arr = [
				'Lima',
				'Abancay',
				'Huaraz', 
				'Ancash',
				'Arequipa',
				'Ayacucho',
				'Cajamarca',
				'Callao',
				'Cerro de Pasco', 
				'Chachapoyas',
				'Chiclayo',
				'Cuzco',
				'Huacho',
				'Huancavelica',
				'Huancayo',
				'Huanuco',	
				'Ica',
				'Iquitos',
				'Moquegua',
				'Moyobamba',
				'Piura',
				'Pucallpa',
				'Puerto Maldonado', 
				'Puno',
				'Tacna',
				'Trujillo',
				'Tumbes',
				'Otros',
				]


	_h_sector_city =  {
					'Lima':			'Lima',
					'Callao': 		'Lima',
					'Huacho': 		'Lima',
					'Ancash': 		'Centro',
					'Huancavelica': 'Centro',
					'Huancayo': 	'Centro',
					'Huanuco': 		'Centro',
					'Huaraz': 		'Centro', 
					'Pucallpa': 	'Centro',
					'Cerro de Pasco': 	'Centro', 
					'Chiclayo': 	'Costa Norte',
					'Cajamarca': 	'Costa Norte',
					'Piura': 		'Costa Norte',
					'Trujillo': 	'Costa Norte',
					'Tumbes': 		'Costa Norte',
					'Ica': 			'Costa Sur',
					'Arequipa': 	'Costa Sur',
					'Tacna': 		'Costa Sur',
					'Moquegua': 	'Costa Sur',
					'Abancay': 		'Sur Este',
					'Ayacucho': 	'Sur Este',
					'Cuzco': 		'Sur Este',
					'Puerto Maldonado': 	'Sur Este', 		# Madre de Dios 
					'Puno': 		'Sur Este',
					'Iquitos': 		'Nor Este',
					'Chachapoyas': 	'Nor Este',
					'Moyobamba': 	'Nor Este',						# San Martin
					'Otros': 		'Otros',
				}




	# Loop 
	for city in city_arr: 
		
		# Init vars 
		sector = _h_sector_city[city]


		# Count - Search in Collections 
		if city in counter_city: 
			count = counter_city[city]
		else: 
			count = 0 


		# Create 
		line = self.city_line.create({
											'name' : 		city, 
											'sector' : 		sector, 
											'count' :		count,
											'marketing_id' :	self.id, 
									})
		
		# Update 
		line.update_fields()




# ----------------------------------------------------------- Districts ---------------------------
def build_districts(self):  
	"""
	Using Collections to count faster
	"""

	# Build Code Array 
	code_arr = np.arange(44)


	# Loop 
	for code in code_arr: 
		
		if code != 0: 

			# Init
			name = pat_vars.zip_dic_inv[code]



			# Count - Search in Collections 
			if name in counter_district: 

				# Init
				sector = mkt_vars._h_sector[name]
				count = counter_district[name]

				# Create 
				#print(name)
				#print(count)
				#print(code)
				#print(sector)
				#print()

				line = self.district_line.create({
													'name' : 		name, 
													'count' :		count,

													'code' :		code, 
													'sector' : 		sector, 

													'marketing_id' :	self.id, 
											})
				# Update 
				line.update_fields()


			else: 
				count = 0 






