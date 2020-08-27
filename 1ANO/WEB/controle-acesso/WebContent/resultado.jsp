<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/bootstrap.css">
    <title>Resultado</title>
</head>

<body class="container">
	<div>
		<label>Teste:${param}</label>
	</div>

    <div>
        <label>Usuário: ${nomeUsuario}</label>
    </div>
    <div>
        <label>Senha: ${param.senha}</label>
    </div>


    <script src="./js/jquery-3.5.1.js"></script>
    <script src="./js/bootstrap.js"></script>
</body>

</html>