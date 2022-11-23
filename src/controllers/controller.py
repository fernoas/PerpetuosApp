
from flask.views import MethodView
from flask import request, render_template, redirect, session, flash, url_for
from src.db import mysql
from src import db
import sys




class InsertController(MethodView):
    
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cadastro_cliente")
            data = cur.fetchall
        return render_template('public/index.html', data = data)

    
    def post(self):
        id_cliente = request.form['id_cliente']
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        bairro = request.form['bairro']
        cidade = request.form['cidade']
        cep = request.form['cep']
        senha = request.form['senha']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO cadastro_cliente(id_cliente,nome,email,telefone,endereco,bairro,cidade,cep,senha) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id_cliente,nome,email,telefone,endereco,bairro,cidade,cep,senha))
            cur.connection.commit()
        return redirect('/clientes')




class DeleteProdutoController(MethodView):
    def get( code):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM produtos WHERE code = %s",(code))
            cur.connection.commit()
        return redirect('/')
        


class UpdateProdutoController(MethodView):
    def get():
        with mysql.cursor() as cur:
            pass
        return "deletado com sucesso"




class ProdutosController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cadastro_produto")
            data = cur.fetchall
            return render_template('public/produtos.html', data=data)

    def post(self):
        tipo_produto = request.form['tipo_produto']
        nome_produto = request.form['nome_produto']
        editora = request.form['editora']
        preco = request.form['preco']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO cadastro_produto(tipo_produto,nome_produto,editora,preco) VALUES(%s,%s,%s,%s)",(tipo_produto,nome_produto,editora,preco))
            cur.connection.commit()
        return redirect('/listaprodutos')

class ListaProdutosController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cadastro_produto")
            data = cur.fetchall
            for n in data:
                print(n)
            return render_template('public/listaprodutos.html', data=data)



class ClientesController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM cadastro_cliente")
            data = cur.fetchall
        return render_template('public/clientes.html', data = data)

    
    def post(self):
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO cadastro_cliente(nome,email,senha) VALUES(%s,%s,%s)",(nome,email,senha))
            cur.connection.commit()
        return redirect('/login')


class EditorasController(MethodView):
    def get(self):
        pass
        return render_template('public/editoras.html')


class LoginController(MethodView):
    def post(self): 
        if request.method == 'POST' and 'email' in request.form and 'senha' in request.form: 
            email = request.form['email'] 
            senha = request.form['senha']
            print(email)
            print(senha) 
            with mysql.cursor() as cur: 
                cur.execute('SELECT * FROM cadastro_cliente WHERE email = %s AND senha = %s', (email, senha)) 
                account = cur.fetchone()
                print(account)
            if account: 
                session['loggedin'] = True
                return redirect(url_for('index'))                    
            else: 
                flash("Usuário ou senha incorretos!")
        return render_template('public/login.html')

    def get(self):
        return render_template('public/login.html')
        
          
class LogoutController(MethodView):
    def get(self):
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('username', None)
        return redirect(url_for('login'))      


class CarrinhoController(MethodView):
    def get(self):
        pass
        return render_template('public/carrinho.html')


class PerfilController(MethodView):
    def get(self):
        pass
        return render_template('public/perfil.html')

    def post(self):
        if request.method == 'POST' and 'email' in request.form and 'senha_antiga' in request.form and 'senha' in request.form: 
            email = request.form['email'] 
            senha_antiga = request.form['senha_antiga']
            senha = request.form['senha']
            print(email)
            print(senha_antiga) 
            print(senha)
            with mysql.cursor() as cur: 
                cur.execute('SELECT senha FROM cadastro_cliente WHERE email = %s', (email)) 
                account = cur.fetchone()
                print(account)
                for i in account:
                    x = str(i)
                print(x)
            if x == senha_antiga:
                with mysql.cursor() as cur: 
                    cur.execute('UPDATE cadastro_cliente SET senha = %s WHERE email = %s ', (senha, email))
                    print(senha)
                    cur.connection.commit()
                    flash('Senha alterada com sucesso!')
                    cur.close()
                return render_template('public/perfil.html')
            else:
                flash('Senha antiga está incorreta!')
            return render_template('public/perfil.html')


class ExcluirPerfilController(MethodView):
    def get(self):
        pass
        return render_template('public/excluirperfil.html')

    def post(self):
        if request.method == 'POST' and 'email' in request.form:
            email = request.form['email']
            with mysql.cursor() as cur: 
                    cur.execute('DELETE FROM cadastro_cliente WHERE email = %s', (email))
                    cur.connection.commit()
            session['loggedin'] = False
            return redirect('/')
            
                




