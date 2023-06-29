from flask import Flask, send_file, request, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = 'root'
app.config['SESSION_COOKIE_MAX_SIZE'] = 4096 * 10  # 40 KB pour stocker le graph


@app.route('/')
def index():
    return render_template('acceuil.html')

@app.route('/initialise/<int:difficulte>')
def initialise(difficulte):
    # player = session.get('player')
    session['difficulte'] = difficulte
    newGrid = [ 0,1,2,3,4,5,6,7,8 ]
    return render_template('jeu.html', grid = newGrid)

@app.route('/symbole/<int:player>')
def symbole(player):
    if player == 1:
        player = 'X'
    elif player == 0:
        player = 'O'
    session['player'] = player
    return render_template('difficultes.html', player = player)

if __name__ == '__main__':
    app.run()