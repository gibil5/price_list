
		# Age Max and Min 
		if line.age_years >= 0:
			self.age_sum = self.age_sum + line.age_years 

			if line.age_years > self.age_max: 
				self.age_max = line.age_years

			if self.age_min in [0]:
				self.age_min = line.age_years

			else:			
				if line.age_years < self.age_min: 
					self.age_min = line.age_years

		else: 										# Error 
			self.age_undefined = self.age_undefined + 1
