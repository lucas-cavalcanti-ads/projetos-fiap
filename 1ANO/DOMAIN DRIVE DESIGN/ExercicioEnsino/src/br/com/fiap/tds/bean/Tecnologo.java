package br.com.fiap.tds.bean;

public class Tecnologo extends Formacao{
	
	//VARIAVEIS
	private boolean planoEstudo;
	
	//CONSTRUTORES
	public Tecnologo() {}
	
	public Tecnologo(String descricao, int periodo, int duracao, double mensalidade, boolean planoEstudo) {
		super(descricao, periodo, duracao, mensalidade);
		this.planoEstudo = planoEstudo;
		
	}

	//GETTERS E SETTERS
	public void setPlanoEstudo(boolean planoEstudo) {
		this.planoEstudo = planoEstudo;
	}
	
	//METODOS
	public void calcularMensalidade(double fator) {
		
	}

	
	
	
	

}
