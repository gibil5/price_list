# 13 Dec 2019

# Create Sales
@api.multi
def create_sale_lines(self):

	# Handle Exceptions
	#exc_mkt.handle_exceptions(self)

	# Go
	# Print Disable
	#test_funcs.disablePrint()


	# Benchmark
	t0 = timer()




	t1 = timer()
	self.delta_create_sale_lines = t1 - t0

	# Print Enable
	#test_funcs.enablePrint()







# 12 Dec 2019



# ----------------------------------------------------------- Update Counters ------------------------
# Set Stats
@api.multi
def update_counters(self):
	# Collections
	#country_arr = []
		# Countries - Dep
		#country_arr.append(line.country)



# Update Macros - Countries - Dep

	# Using collections
	#counter_country = collections.Counter(country_arr)

	# Country
	#print 'Create Country Line '
	#for key in counter_country:
	#	count = counter_country[key]
	#	country = self.country_line.create({
	#											'name': key,
	#											'count': count,
	#											'marketing_id': self.id,
	#										})
		#print country

	#print self.country_line
	#print


