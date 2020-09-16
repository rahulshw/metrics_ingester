import requests
import json
from random import randint

ENDPOINT='http://127.0.0.1:5000'


def test_metric_ingester(endpoint):

	values = [
		# (percent_cpu_usage, percent_memory_usage)
		(0, 0)
	]
	max_cpu = 0
	max_memory = 0

	for i in range(5):
		percent_cpu_usage = randint(0,100)
		percent_memory_usage = randint(0, 100)
		max_cpu = max(max_cpu, percent_cpu_usage)
		max_memory = max(max_memory, percent_memory_usage)
		print(max_cpu, max_memory)
		values.append((percent_cpu_usage, percent_memory_usage))


	# push metrics
	for cpu_usage, memory_usage in values:
		res = requests.post(url='%s/metrics'%endpoint, headers={'Content-Type': 'application/json'}, 
			data=json.dumps(dict(percentage_cpu_used=cpu_usage, percentage_memory_used=memory_usage)))
		if res.status_code != 200:
			print(res.text)
			exit(1)


	# get_report
	res = requests.get(url='%s/report'%endpoint)
	data = res.json()
	print(data, max_cpu, max_memory)
	assert max_cpu == data[0]['max_cpu']
	assert max_memory == data[0]['max_memory']

test_metric_ingester(ENDPOINT)