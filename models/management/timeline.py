# -*- coding: utf-8 -*-
"""
	Timeline Class

	Created: 			11 oct 2020
	Last up: 	 		11 oct 2020
"""
import data_stats

class TreatmentState(object):
	"""
	Used by Management
	"""
	def __init__(self):
		print()
		print('TreatmentState  -  init')

# ----------------------------------------------------------- Timeline -----------------
	# Create Timeline
	def create_timeline(self):
		"""
        Create Timeline
		"""
		print()
		print('Create Timeline')

		_dic_mo = {
					'01': 'ENE',
					'02': 'FEB',
					'03': 'MAR',
					'04': 'ABR',
					'05': 'MAY',
					'06': 'JUN',

					'07': 'JUL',
					'08': 'AGO',
					'09': 'SET',
					'10': 'OCT',
					'11': 'NOV',
					'12': 'DIC',
		}

		family_data = []
		subfamily_data = []
		months = []
		idxs = []
		amounts = []
		amounts_con = []
		amounts_prod = []
		amounts_proc = []
		amounts_co2 = []
		amounts_ipl = []
		amounts_exc = []
		amounts_ipl = []
		amounts_ndy = []
		amounts_qui = []
		amounts_med = []
		amounts_cos = []

		# mgts
		mgts = self.env['openhealth.management'].search([
															('owner', 'in', ['month']),
														],
														order='date_begin,name asc',
														#limit=1,
													)
		print(mgts)

		idx = 0
		for mgt in mgts:
			print(mgt.name)
			print(mgt.year)
			print(mgt.month)
			print()

			#months.append(mgt.month)
			months.append(_dic_mo[mgt.month])

			idxs.append(idx)
			idx = idx + 1

			amounts.append(mgt.total_amount)

			amounts_con.append(mgt.amo_consultations)
			amounts_proc.append(mgt.amo_procedures)
			amounts_prod.append(mgt.amo_products)

			amounts_co2.append(mgt.amo_co2)
			amounts_exc.append(mgt.amo_exc)
			amounts_ipl.append(mgt.amo_ipl)
			amounts_ndy.append(mgt.amo_ndyag)
			amounts_qui.append(mgt.amo_quick)
			amounts_med.append(mgt.amo_medical)
			amounts_cos.append(mgt.amo_cosmetology)

		print(amounts)
		print(len(amounts))
		print(months)
		print(len(months))
		print(idxs)
		print(len(idxs))

		# Common
		path = self.base_dir + 'img/chavarri/'

		# Totals
		name = 'All'
		fig_pie = 'mgt_amo_pie.png'
		fig_line = 'mgt_amo_line.png'
		mgt_amo_data = data_stats.Data(amounts, idxs, name, path, fig_pie, fig_line)
		#mgt_amo_data.get_graph()

		family_data.append(mgt_amo_data)
		subfamily_data.append(mgt_amo_data)

# Fams
		# Consultations
		name = 'Consultations'
		fig_pie = 'amo_con_pie.png'
		fig_line = 'amo_con_line.png'
		amo_con_data = data_stats.Data(amounts_con, idxs, name, path, fig_pie, fig_line)
		#amo_con_data.get_graph()

		family_data.append(amo_con_data)

		# Procedures
		name = 'Procedures'
		fig_pie = 'amo_proc_pie.png'
		fig_line = 'amo_proc_line.png'
		amo_proc_data = data_stats.Data(amounts_proc, idxs, name, path, fig_pie, fig_line)
		#amo_proc_data.get_graph()

		family_data.append(amo_proc_data)

		# Products
		name = 'Products'
		fig_pie = 'amo_prod_pie.png'
		fig_line = 'amo_prod_line.png'
		amo_prod_data = data_stats.Data(amounts_prod, idxs, name, path, fig_pie, fig_line)
		#amo_prod_data.get_graph()

		family_data.append(amo_prod_data)

# Subs
		# Co2
		name = 'Co2'
		fig_pie = 'amo_co2_pie.png'
		fig_line = 'amo_co2_line.png'
		amo_co2_data = data_stats.Data(amounts_co2, idxs, name, path, fig_pie, fig_line)
		#amo_co2_data.get_graph()

		subfamily_data.append(amo_co2_data)


		# qui
		name = 'Qui'
		fig_pie = 'amo_qui_pie.png'
		fig_line = 'amo_qui_line.png'
		amo_qui_data = data_stats.Data(amounts_qui, idxs, name, path, fig_pie, fig_line)
		#amo_qui_data.get_graph()

		subfamily_data.append(amo_qui_data)

		# exc
		name = 'Exc'
		fig_pie = 'amo_exc_pie.png'
		fig_line = 'amo_exc_line.png'
		amo_exc_data = data_stats.Data(amounts_exc, idxs, name, path, fig_pie, fig_line)
		#amo_exc_data.get_graph()

		subfamily_data.append(amo_exc_data)

		# ipl
		name = 'Ipl'
		fig_pie = 'amo_ipl_pie.png'
		fig_line = 'amo_ipl_line.png'
		amo_ipl_data = data_stats.Data(amounts_ipl, idxs, name, path, fig_pie, fig_line)
		#amo_ipl_data.get_graph()

		subfamily_data.append(amo_ipl_data)

		# ndy
		name = 'Ndy'
		fig_pie = 'amo_ndy_pie.png'
		fig_line = 'amo_ndy_line.png'
		amo_ndy_data = data_stats.Data(amounts_ndy, idxs, name, path, fig_pie, fig_line)
		#amo_ndy_data.get_graph()

		subfamily_data.append(amo_ndy_data)


		# med
		name = 'Med'
		fig_pie = 'amo_med_pie.png'
		fig_line = 'amo_med_line.png'
		amo_med_data = data_stats.Data(amounts_med, idxs, name, path, fig_pie, fig_line)
		#amo_med_data.get_graph()

		subfamily_data.append(amo_med_data)

		# cos
		name = 'Cos'
		fig_pie = 'amo_cos_pie.png'
		fig_line = 'amo_cos_line.png'
		amo_cos_data = data_stats.Data(amounts_cos, idxs, name, path, fig_pie, fig_line)
		#amo_cos_data.get_graph()

		subfamily_data.append(amo_cos_data)


		# All
		name = 'All'
		fig_pie = 'amo_fam_pie.png'
		fig_line = 'amo_fam_line.png'
		#all_amo_data = data_stats.DataSet(name, months, path, fig_pie, fig_line, family_data)
		all_fam_data = data_stats.DataSet(name, idxs, path, fig_pie, fig_line, family_data)			
		all_fam_data.get_graph()


		# All
		name = 'Sub Families'
		fig_pie = 'amo_sub_pie.png'
		fig_line = 'amo_sub_line.png'
		#all_amo_data = data_stats.DataSet(name, months, path, fig_pie, fig_line, family_data)
		all_sub_data = data_stats.DataSet(name, idxs, path, fig_pie, fig_line, subfamily_data)
		all_sub_data.get_graph()

