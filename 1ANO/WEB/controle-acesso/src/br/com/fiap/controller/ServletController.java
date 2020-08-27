package br.com.fiap.controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ServletController
 */
@WebServlet(urlPatterns= {"/index.aspx", "/validador"})//MAPEAMENTO > VAI COLOCAR NO ACTION DO FORMULARIO > VIRTUALMENTE ESSE INDEX E VALIDADOR FICAM NA RAIZ WEB CONTENT
public class ServletController extends HttpServlet { //A HttpServlet, prove todos os verbos Http (GET, PUT, POST, etc)
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ServletController() {
        super();
    }

	/**
	 * @see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//TESTE DE REQUEST
		System.out.println("Olá mundo");
		System.out.println("Request: " + request);
		
		String nomeUsuario = "";
		String senhaUsuario = "";
		
		nomeUsuario = request.getParameter("usuario");
		senhaUsuario = request.getParameter("senha");
		
		System.out.println("Usuário: " + nomeUsuario);
		System.out.println("Senha: " + senhaUsuario);
		
		//REDIRECIONANDO ATRAVÉS DO PATH (CAMINHO OU URI)
		response.sendRedirect("resultado.jsp");
		
		
		//metodo getRequestDispatcher(path)
		
		//Enchaminha o request e o response com o forward
		

	}
	
	


}
