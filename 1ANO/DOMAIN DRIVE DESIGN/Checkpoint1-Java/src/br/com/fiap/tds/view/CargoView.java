package br.com.fiap.tds.view;

import javax.swing.JOptionPane;

import br.com.fiap.tds.bean.Cargo;

public class CargoView {
	public static void main(String[] args) {

		String cargoString = JOptionPane.showInputDialog("Digite o cargo:");
		String nivelString = JOptionPane.showInputDialog("Digite o n�vel do cargo:");

		Cargo cargo = new Cargo(cargoString, nivelString);

		JOptionPane.showMessageDialog(null, "O salario para o cargo: " + cargo.getCargo() + " �: "
				+ cargo.retornaSalario() + "\n O n�vel do cargo �: " + cargo.retornaNivel());

	}

}