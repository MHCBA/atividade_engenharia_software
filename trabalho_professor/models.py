from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Aluno {self.nome}>'

def init_db():
    db.create_all()
    # Adicionar dados de exemplo se necessário
    if not Aluno.query.first():
        alunos_exemplo = [
            Aluno(nome="João Silva", cpf="123.456.789-00", 
                  matricula="20230001", endereco="Rua A, 123", telefone="(11) 9999-8888"),
            Aluno(nome="Maria Souza", cpf="987.654.321-00", 
                  matricula="20230002", endereco="Av. B, 456", telefone="(11) 9777-6666")
        ]
        db.session.bulk_save_objects(alunos_exemplo)
        db.session.commit()