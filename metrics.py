import requests


PROMETHEUS_URL = 'http://localhost:9090/api/v1/query'

def get_metrics():
     queries = {
         "CPU Usage (%)": '100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)',
         "Memory Usage (%)": '(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / node_memory_MemTotal_bytes * 100',
         "Disk Usage (%)": '(node_filesystem_size_bytes{mountpoint="/"} - node_filesystem_avail_bytes{mountpoint="/"}) / node_filesystem_size_bytes{mountpoint="/"} * 100'
     }
     metric_results = []
     for name, query in queries.items():
         try:
             response = requests.get(PROMETHEUS_URL, params={'query': query})
             response.raise_for_status() # Check for HTTP errors
        
             data = response.json()
        
             # 3. Parsing the JSON result
             for result in data['data']['result']:
                 instance = result['metric'].get('instance', 'unknown')
                 value = result['value'][1] # result['value'] is [timestamp, value]
                 if name  == 'CPU Usage (%)' and float(value) > 80.0:
                      metric_results.append({"name" : name,"value": float(value), "instance" : instance,
						 "status" : "WARNING" })
                 elif name == 'Memory Usage (%)' and float(value) > 90.0:
                      metric_results.append({"name" : name,"value": float(value),"instance" : instance,
						 "status" : "WARNING" })
                 else:
                      metric_results.append({"name" : name,"value": float(value), "instance" : instance, 
						"status" : "Normal"})
            
         except requests.exceptions.RequestException as e:
             metric_results.append({"name": name, "value": None, "instance": "unknown", 
					"status": "ERROR"})

     return metric_results
