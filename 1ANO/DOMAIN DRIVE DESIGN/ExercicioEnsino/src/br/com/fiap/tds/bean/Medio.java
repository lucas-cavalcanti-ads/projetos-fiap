package br.com.fiap.tds.bean;

public class Medio extends Formacao {
	
	//VARIAVEIS
	private String tipo;

	
	//CONSTRUTORES	
	public Medio() {}

	public Medio(String descricao, int periodo, int duracao, double mensalidade, String tipo) {
		super(descricao, periodo, duracao, mensalidade);
		this.tipo = tipo;
	}

	
	//GETTERS E SETTERS
	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	
	///METODOS
	public void calcularMensalidade(double fator) {
		
	}
	
	
	
	
	

}
