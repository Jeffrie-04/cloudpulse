from flask import Flask
from metrics import get_metrics
from alerts import send_alert


app = Flask(__name__)

@app.route("/")
def dashboard():
     metrics_data = get_metrics()
     html_output = "<h1>CloudPulse Metrics</h1>"
    
     for m in metrics_data:
          color = "red" if m['status'] == "WARNING" else "green"
        
          html_output += f"""
          <p>
              <b>Metric:</b> {m['name']} | 
              <b>Instance:</b> {m['instance']} | 
              <b>Value:</b> {f"{m['value']:.2f}%" if m['value'] is not None else "N/A"} | 
              <b>Status:</b> <span style="color: {color};">{m['status']}</span>
          </p>
          <hr>
          """
          if m['status'] == "WARNING":
               send_alert(m['name'], m['value'])
     return html_output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
