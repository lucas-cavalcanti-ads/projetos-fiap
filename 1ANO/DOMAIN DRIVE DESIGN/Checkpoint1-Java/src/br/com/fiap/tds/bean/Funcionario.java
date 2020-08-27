package br.com.fiap.tds.bean;

//Classe criada por:  Pablo André Nunes
public class Funcionario {

	private String Nome, cpf;
	private int matricula, dataNascimento;

	// Constructors

	public Funcionario() {

	}

	public Funcionario(String nome) {
		this.Nome = nome;
	}

	public Funcionario(String nome, String cpf) {
		this.Nome = nome;
		this.cpf = cpf;
	}

	public Funcionario(String nome, String cpf, int matricula) {
		this.Nome = nome;
		this.cpf = cpf;
		this.matricula = matricula;
	}

	// Methods
	// Converter nome para maiúsculo
	public String nomeMaiusculo(String nome) {
		return nome.toUpperCase();
	}

	// Valida CPF
	/*
	 * String soma; int resto; int multiplicador;
	 * 
	 * public String validaCPF() { if (cpf.length() != 11) { return "CPF Invalido";
	 * }else { for(int i =1; i<=9;i++) { soma = soma + (cpf.charAt(i) * 10); return
	 * soma; } } return soma; }
	 */

	/*
	 * int soma; int resto; int multiplicador;
	 * 
	 * public boolean validaCPF() { if (cpf.length() != 11) {
	 * 
	 * for ( int i = 1; i <=9; i++) { soma = soma + cpf.charAt(i) * 11-i; } return
	 * false; } return false; }
	 */

	// Getters and setters
	public String getCpf() {
		return cpf;
	}

	public void setCpf(String cpf) {
		this.cpf = cpf;
	}

	public String getNome() {
		return Nome;
	}

	public void setNome(String nome) {
		Nome = nome;
	}

	public int getMatricula() {
		return matricula;
	}

	public void setMatricula(int matricula) {
		this.matricula = matricula;
	}

	public int getDataNascimento() {
		return dataNascimento;
	}

	public void setDataNascimento(int dataNascimento) {
		this.dataNascimento = dataNascimento;
	}

}
