package br.com.fiap.tds.bean;

// Classe criada por:  Pablo André Nunes
public class Cargo {
	private String cargo, nivel;
	private float salario;

	// Constructors
	public Cargo() {

	}

	public Cargo(String cargo, String nivel) {
		this.cargo = cargo;
		this.nivel = nivel;
	}

	// Methods
	// Retorna Salario de acordo com o Cargo informado
	public String retornaSalario() {
		String valorSalario = "";
		switch (cargo) {
		case "Gerente":
			valorSalario = "8000";
			break;
		case "Coordenador":
			valorSalario = "6000";
			break;
		case "Analista":
			valorSalario = "4000";
			break;
		case "Assistente":
			valorSalario = "2000";
			break;
		}
		return valorSalario;
	}

	// Retorna nivel hierárquico de acordo com o número informado
	public String retornaNivel() {
		String cargoNivel = "";
		switch (nivel) {
		case "1":
			cargoNivel = "Junior";
			break;
		case "2":
			cargoNivel = "Pleno";
			break;
		case "3":
			cargoNivel = "Senior";
			break;
		}
		return cargoNivel;
	}

	// Getters and Setters
	public String getCargo() {
		return cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public String getNivel() {
		return nivel;
	}

	public void setNivel(String nivel) {
		this.nivel = nivel;
	}

	public float getSalario() {
		return salario;
	}

	public void setSalario(float salario) {
		this.salario = salario;
	}
}
