from flask import Flask, render_template, jsonify  #flask=module, Flask = class

app = Flask(__name__)  #creating object of Flask

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Bengaluru, India',
  'salary': 'RS. 15,00,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Bengaluru, India',
  'salary': 'RS. 12,00,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'San Francisco USA',
  'salary': '$120,000'
}]


@app.route("/")  #adding a route
def hello_world():  #when url / is active, show "hello"
  return render_template('home.html', jobs=JOBS, company_name="Jovian")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
