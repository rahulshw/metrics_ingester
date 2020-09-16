import copy

class MetricsStorage:
	def __init__(self):
		self.data = dict()

	def store_metrics(self, ip_address, data):

		if ip_address in self.data:

			# storing only the max values as only these are required in the report
			if data['percentage_cpu_used'] > self.data[ip_address]['max_cpu']:
				self.data[ip_address]['max_cpu'] = data['percentage_cpu_used']

			if data['percentage_memory_used'] > self.data[ip_address]['max_memory']:
				self.data[ip_address]['max_memory'] = data['percentage_memory_used']
		else:
			self.data[ip_address] = dict(
				max_cpu=data['percentage_cpu_used'],
				max_memory=data['percentage_memory_used']
			)

	def generate_report(self):
		report = []
		for ip_address, stats in self.data.items():

			_stats = copy.deepcopy(stats)
			_stats.update({'ip_address': ip_address})

			report.append(_stats)

		return report