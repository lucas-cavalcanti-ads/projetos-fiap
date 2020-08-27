package br.com.fiap.tds.bean;

public class Bacharelado extends Formacao {
	
	//VARIAVEIS
	private String projetoConclusao;
	private int cargaHorariaEstagio;
	
	
	//CONSTRUTORES
	public Bacharelado() {}
	
	public Bacharelado(String descricao, int periodo, int duracao, double mensalidade, String projetoConclusao, int cargaHorariaEstagio) {
		super(descricao, periodo, duracao, mensalidade);
		this.projetoConclusao = projetoConclusao;
		this.cargaHorariaEstagio = cargaHorariaEstagio;
	}

	
	//GETTERS E SETTERS
	public String getProjetoConclusao() {
		return projetoConclusao;
	}

	public void setProjetoConclusao(String projetoConclusao) {
		this.projetoConclusao = projetoConclusao;
	}

	public int getCargaHorariaEstagio() {
		return cargaHorariaEstagio;
	}

	public void setCargaHorariaEstagio(int cargaHorariaEstagio) {
		this.cargaHorariaEstagio = cargaHorariaEstagio;
	}
	
	///METODOS
	public void calcularMensalidade(double fator) {
		
	}
	

	
	
	
	
	
	
	
	
	
	
	
	
	
}
