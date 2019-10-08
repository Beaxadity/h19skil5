from flask import Flask, render_template, session, request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Leyno'

vorur=[
	[0,"Emergency Underpants",2500,"EmerPants.jpg"],
	[1,"iStick",1599,"Gumbo.jpg"],
	[2,"Scotch Pin",999,"Pin.jpg"],
	[3,"Twat Waffle",1979,"Twaffle.jpg"],
	[4,"Unicorn Meat",15000,"UniBeef.jqg"],
	[5,"Willy Warmer",2999,"Wonka.jqg"],
	[6,"1 Zillion Dollar Bill",1000000000000000,"Zillion.jpg"]
]


@app.route('/')
def index():
	karfa = 0
	if 'karfa' in session:
		karfa = len(session['karfa'])
		real = True
	else:
		real = False
	return render_template("index.html", vorur=vorur, b=karfa, real=real)

@app.route('/karfa')
def karfa():
	karfa = []
	i=0
	heild=0
	if 'karfa' in session:
		karfa = session['karfa']
		i = len(session['karfa'])
		for x in karfa:
			for l in vorur:
				if l[0] == x:
					heild += l[2]
	return render_template("karfa.html", vorur=vorur, karfa=karfa, i=i, heild=heild)

@app.route('/karfan/<int:id>')
def karfan(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.append(id)
		session['karfa'] = karfa
	else:
		karfa.append(id)
		session['karfa'] = karfa
	print(len(karfa))
	return render_template("karfan.html", vorur=vorur)

@app.route('/eyda/<int:id>')
def eyda(id):
	karfa = []
	if 'karfa' in session:
		karfa = session['karfa']
		karfa.remove(id)
		session['karfa'] = karfa
	return render_template("eyda.html", vorur=vorur)

@app.route('/taema')
def taema():
	session.pop('karfa',None)
	return render_template("taema.html", vorur=vorur)

@app.route('/karfa/kaupa')
def kaupa():
	karfa = []
	heild = 0
	if 'karfa' in session:
		karfa = session['karfa']
		for x in karfa:
			for y in vorur:
				if y[0] == x:
					heild += y[2]
	return render_template("kaupa.html", vorur=vorur, karfa=karfa, heild=heild)

@app.route('/karfa/kaupa/yfirlit', methods=['GET','POST'])
def yfirlit():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
	karfa = []
	session['karfa'] = karfa
	return render_template("yfirlit.html", vorur=vorur, name=name, email=email)

@app.errorhandler(404)
def error404(error):
	return "Site not found", 404

if __name__ == "__main__":
	app.run(debug=True)
