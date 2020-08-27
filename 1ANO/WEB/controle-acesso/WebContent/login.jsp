<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, shrink-to-fit=no">
		<title>Login</title>
		<link rel="stylesheet" href="./css/bootstrap.css">
	</head>
	
	<body class="container">
	
		<!-- INICIO CABECALHO -->
		<header>
			<div>
				<!-- BOTAO QUE ABRE A MODAL -->
				<button type="button" class="btn btn-info" data-toggle="modal"
					data-target="#modalLogin">Login</button>
			</div>
		</header>
		<!-- TERMINO CABECALHO -->
	
		<!-- INICIO DO CONTEÚDO PRINCIPAL -->
	    <main>
	        <!-- INICIO DA MODAL DE LOGIN -->
	        <div id="modalLogin" class="modal fade" role="dialog">
	            <div class="modal-dialog">
	                <div class="modal-content">
	                
	                    <div class="modal-header">
	
	                        <h3>
	                            Login de usuários
	                        </h3>
	
	                        <button type="button" class="close" data-dismiss="modal">&times;</button>
	
	                    </div>
	                    
	                    <!-- INICIO CORPO DA MODAL DE LOGIN -->
	                    <div class="modal-body">
	                        <div class="form">
	                            <form class="form-horizontal" action="index.aspx" method="GET">
	                                <div class="form-group">
	                                    <label class="control-label col-sm-2" for="usuario">Usuário</label>
	                                    <div class="col-sm-10">
	                                        <input type="text" class="form-control" name="usuario" id="usuario"
	                                            placeholder="Digite seu usuário" required="required">
	                                    </div>
	
	                                    <label class="control-label col-sm-2 mt-2" for="usuario">Senha</label>
	                                    <div class="col-sm-10">
	                                        <input type="password" class="form-control" name="senha" id="senha"
	                                            placeholder="Digite sua senha" required="required">
	                                    </div>
	                                </div>
	                                <div class="form-group">
	                                    <button type="submit" class="btn btn-success form-control col-3">Entrar</button>
	                                </div>
	                            </form>
	                            
	                        </div>
	                    </div>
	                    <!-- TÉRMINO CORPO DA MODAL DE LOGIN -->
	
	                    <div class="modal-footer">
	                        <button class="btn btn-danger" data-dismiss="modal">Fechar</button>
	                    </div>
	
	                </div>
	            </div>
	
	        </div>
	        <!-- TÉRMINO DA MODAL DE LOGIN -->
	    </main>
	    <!-- TÉRMINO DO CONTEÚDO PRINCIPAL -->
	    
	    <div>	    
		    <p>
		    	<a href="validador">
		    		VALIDADOR
		    	</a>
		    </p>	    
	    </div>
	
		<script src="./js/jquery-3.5.1.js"></script>
	    <script src="./js/bootstrap.js"></script>
	</body>
</html>