from flask import Flask, render_template, request, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = "c6e803cd18a8c528c161eb9fcf013245248506ffb540ff70"

oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id='846264335970-vs7uk6k9oqbq4eufskvgkfgdcglvj11b.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'email profile'},
    server_metadata_url= 'https://accounts.google.com/.well-known/openid-configuration'
)


@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect(url_for('index'))

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = dict(google.get('userinfo').json())
    session['user'] = resp
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'user' in session:
        cities = ['Hyderabad','Delhi','Vishakapatnam','Amaravati','Amritsar','Kolkata','Chandigarh','Patna','Gurugram']
        return render_template('home.html', user=False, cities=cities)
    return render_template('index.html')

@app.route('/<selcity>')
def home(selcity):
    if 'user' in session:
        if selcity == 'Hyderabad':
            state = 'Telangana'
        elif selcity == 'Delhi':
            state = 'Delhi'
        elif selcity == 'Vishakapatnam':
            state = 'Andhra Pradesh'
        elif selcity == 'Amaravati':
            state = 'Andhra Pradesh'
        elif selcity == 'Amritsar':
            state = 'Punjab'
        elif selcity == 'Kolkata':
            state = 'West Bengal'
        elif selcity == 'Chandigarh':
            state = 'Chandigarh'
        elif selcity == 'Patna':
            state = 'Bihar'
        elif selcity == 'Gurugram':
            state = 'Haryana'
        else:
            return redirect(url_for('index'))
        return render_template('form.html', user=session['user'], selcity=selcity,state=state)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)