import flask
import json
from metrics_storage import MetricsStorage

app = flask.Flask(__name__)


@app.route('/metrics', methods=['POST'])
def ingest_metrics():
	data = flask.request.get_json()
	print("data", data)
	ip_address = flask.request.remote_addr
	metric_store.store_metrics(ip_address=ip_address, data=data)
	return 'Success!'


@app.route('/report', methods=['GET'])
def generate_report():
	return json.dumps(metric_store.generate_report())


if __name__ == '__main__':
	metric_store = MetricsStorage()
	app.run(debug=True)
