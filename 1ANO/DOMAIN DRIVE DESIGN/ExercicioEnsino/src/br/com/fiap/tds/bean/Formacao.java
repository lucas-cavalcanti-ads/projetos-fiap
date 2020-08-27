package br.com.fiap.tds.bean;

public class Formacao {
	
	//VARIAVEIS
	private String descricao;
	private int periodo, duracao;
	private double mensalidade;
	
	
	//CONSTRUTORES
	public Formacao() {}
	
	public Formacao(String descricao, int periodo, int duracao, double mensalidade) {
		super();
		this.descricao = descricao;
		this.periodo = periodo;
		this.duracao = duracao;
		this.mensalidade = mensalidade;
	}
	
	
	//GETTERS E SETTERS
	public String getDescricao() {
		return descricao;
	}

	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}

	public int getPeriodo() {
		return periodo;
	}

	public void setPeriodo(int periodo) {
		this.periodo = periodo;
	}

	public int getDuracao() {
		return duracao;
	}

	public void setDuracao(int duracao) {
		this.duracao = duracao;
	}

	public double getMensalidade() {
		return mensalidade;
	}

	public void setMensalidade(double mensalidade) {
		this.mensalidade = mensalidade;
	}


	//METODOS
	public void definirDuracao() {
			
	}
	
	public double ExibirMedia(double ps1, double ps2) {
		return 0;
	}
	
	public double ExibirMedia(double ps1, double ps2, double nac1, double nac2) {
		return 0;
	}
	
	public double ExibirMedia(double ps1, double ps2, double nac1, double nac2, double am1, double am2) {
		return 0;
	}
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
}
