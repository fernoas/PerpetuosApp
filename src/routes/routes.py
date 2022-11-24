from src.controllers.errors import NotFoundController
from src.controllers.controller import *



routes = {

    "insert_route":"/","insertcontroller":InsertController.as_view("index"),
    "produtos_route":"/produtos","produtoscontroller":ProdutosController.as_view("produtos"),
    "listaprodutos_route":"/listaprodutos","listaprodutoscontroller":ListaProdutosController.as_view("listaprodutos"),
    "clientes_route":"/clientes","clientescontroller":ClientesController.as_view("clientes"),
    "editoras_route":"/editoras","editorascontroller":EditorasController.as_view("editoras"),
    "login_route":"/login","logincontroller":LoginController.as_view("login"),
    "logout_route":"/logout","logoutcontroller":LogoutController.as_view("logout"),
    "perfil_route":"/perfil","perfilcontroller":PerfilController.as_view("perfil"),
    "excluirperfil_route":"/excluirperfil","excluirperfilcontroller":ExcluirPerfilController.as_view("excluirperfil"),
    "carrinho_route":"/carrinho","carrinhocontroller":CarrinhoController.as_view("carrinho"),
    
    "deleteproduto_route":"/deleteproduto","deleteprodutocontroller": DeleteProdutoController
.as_view("deleteproduto"),


    "update_route":"/update/product/<int:code>", "update_controller": UpdateProdutoController
.as_view("update"),

    "not_found_route":404,"not_found_controller": NotFoundController.as_view("not_found"),


}


