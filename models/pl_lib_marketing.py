# -*- coding: utf-8 -*-
from __future__ import print_function


# ----------------------------------------------------------- Media -------------------------------
#def build_media(self):  
def pl_build_media(self):  
	print()
	print('Pl - Build Media')

	# Clear 
	self.media_line.unlink()


	# Build 
	media_arr = [
					'facebook',
					'instagram',
					'callcenter',
					'old_patient',

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



