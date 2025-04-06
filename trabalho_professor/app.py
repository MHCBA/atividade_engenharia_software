from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Aluno, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta_aqui'

db.init_app(app)

# Criar banco de dados e tabelas
with app.app_context():
    init_db()

@app.route('/')
def index():
    alunos = Aluno.query.all()
    return render_template('index.html', alunos=alunos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        try:
            aluno = Aluno(
                nome=request.form['nome'],
                cpf=request.form['cpf'],
                matricula=request.form['matricula'],
                endereco=request.form['endereco'],
                telefone=request.form['telefone']
            )
            db.session.add(aluno)
            db.session.commit()
            flash('Aluno cadastrado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao cadastrar aluno: {str(e)}', 'danger')
    return render_template('cadastro.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    aluno = Aluno.query.get_or_404(id)
    if request.method == 'POST':
        try:
            aluno.nome = request.form['nome']
            aluno.cpf = request.form['cpf']
            aluno.matricula = request.form['matricula']
            aluno.endereco = request.form['endereco']
            aluno.telefone = request.form['telefone']
            db.session.commit()
            flash('Aluno atualizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Erro ao atualizar aluno: {str(e)}', 'danger')
    return render_template('editar.html', aluno=aluno)

@app.route('/excluir/<int:id>')
def excluir(id):
    aluno = Aluno.query.get_or_404(id)
    try:
        db.session.delete(aluno)
        db.session.commit()
        flash('Aluno excluído com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao excluir aluno: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    alunos = Aluno.query.filter(
        (Aluno.nome.contains(termo)) | 
        (Aluno.cpf.contains(termo)) | 
        (Aluno.matricula.contains(termo))
    ).all()
    return render_template('buscar.html', alunos=alunos, termo=termo)

@app.route('/exportar/json')
def exportar_json():
    alunos = Aluno.query.all()
    alunos_dict = [{
        'id': aluno.id,
        'nome': aluno.nome,
        'cpf': aluno.cpf,
        'matricula': aluno.matricula,
        'endereco': aluno.endereco,
        'telefone': aluno.telefone
    } for aluno in alunos]
    return jsonify(alunos_dict)

if __name__ == '__main__':
    app.run(debug=True)