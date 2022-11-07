from flask import Flask, jsonify, request, render_template, Response, redirect,url_for
import config as dbase
from models import Produto

app = Flask(__name__)
app.secret_key = 'random'

db = dbase.dbConnection()

#Rotas
@app.route('/')
def home():
    produtos = db['produtos']
    produtosRecebidos = produtos.find()
    return render_template('index.html', produtos = produtosRecebidos)

#Metódo POST - CRIAR NOVO PRODUTO
@app.route('/produtos', methods=['POST'])
def criar_produtos():
    produtos = db['produtos']
    nome = request.form['nome']
    preco = request.form['preco']
    categoria = request.form['categoria']
    desc = request.form['desc']
    quantidade = request.form['quantidade']
    
    if nome and preco and categoria and desc and quantidade:
        produto = Produto(nome,preco,categoria,desc,quantidade)
        produtos.insert_one(produto.toDBCollection())
        response = jsonify({
            'nome': nome,
            'preco': preco,
            'categoria': categoria,
            'desc': desc,
            'quantidade': quantidade
        })
        return redirect(url_for('home'))
    else:
        return notFound()
    
    
    
#Metódo DELETE
@app.route('/delete/<string:produto_nome>')
def delete(produto_nome):
    produtos = db['produtos']
    produtos.delete_one({'nome': produto_nome})
    return redirect(url_for('home'))

#Metódo PUT
@app.route('/edit/<string:produto_nome>', methods=['POST'])
def editar_produto(produto_nome):
    produtos = db['produtos']
    nome = request.form['nome']
    preco = request.form['preco']
    categoria = request.form['categoria']
    desc = request.form['desc']
    quantidade = request.form['quantidade']
    
    if nome and preco and categoria and desc and quantidade:
        produtos.update_one({'nome': produto_nome},{'$set': {'nome':nome,'preco':preco,'categoria':categoria,'desc':desc,'quantidade':quantidade}})
        response = jsonify({'message': 'Produto' + produto_nome + 'atualizado com sucesso.'})
        return redirect(url_for('home')) 
    else:
        return notFound()
    


#PÁGINA DE ERRO, COM POSSÍVEL ERRO EM FORMA DE JSON.
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'status':404,
        'message': 'Not found ' + request.url
    }
    
    response = jsonify(message)
    
    response.status_code = 404
    
    return response
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
