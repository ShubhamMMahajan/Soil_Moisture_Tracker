def get_attributes(data, attributes, attribute_types):
	values = []
	for i in range(len(attributes)):
		start_index = data.find(attributes[i]) + len(attributes[i]) + 2
		end_index = data.find(",", start_index)
		attribute_value = attribute_types[i](data[start_index:end_index].strip())
		values.append(attribute_value)
	return values

def export_to_big_query(event, context):
	import base64
	
	attributes = ["id", "humidity", "timestamp"]
	attribute_types = [str, float, str]
	
	data = base64.b64decode(event['data']).decode('utf-8')
	
	values = [tuple(get_attributes(data, attributes, attribute_types))]
	
	from google.cloud import bigquery


	client = bigquery.Client()


	table_id = "soil-moisture-monitor-269202.soil_data.humidity_data"

	table = client.get_table(table_id)  # Make an API request.

	errors = client.insert_rows(table, values)  # Make an API request.
	if errors == []:
		print("New rows have been added.")
	#print('Hello {}!'.format(name))
