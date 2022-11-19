from flask import Flask
from src.routes.routes import *


app = Flask(__name__)

app.secret_key = '56740367'

app.add_url_rule(routes["insert_route"], view_func=routes["insertcontroller"])

app.add_url_rule(routes["produtos_route"], view_func=routes["produtoscontroller"])

app.add_url_rule(routes["clientes_route"], view_func=routes["clientescontroller"])

app.add_url_rule(routes["editoras_route"], view_func=routes["editorascontroller"])

app.add_url_rule(routes["login_route"], view_func=routes["logincontroller"])

app.add_url_rule(routes["logout_route"], view_func=routes["logoutcontroller"])

app.add_url_rule(routes["perfil_route"], view_func=routes["perfilcontroller"])

app.add_url_rule(routes["carrinho_route"], view_func=routes["carrinhocontroller"])

app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])

app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])

app.register_error_handler(routes["not_found_route"], routes["not_found_controller"])
