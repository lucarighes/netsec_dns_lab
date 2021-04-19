from flask import Flask

app = Flask("trusted")

@app.route('/', methods=['GET'])
def start_attack():
	return 'Here is the trusted webserver with IP: 192.168.0.101'


if __name__ == "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 80)
