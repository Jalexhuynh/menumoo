from menumoo import app

app.secret_key = 'super_secret_key'
app.debug = False
app.run(host='0.0.0.0', port=5000)