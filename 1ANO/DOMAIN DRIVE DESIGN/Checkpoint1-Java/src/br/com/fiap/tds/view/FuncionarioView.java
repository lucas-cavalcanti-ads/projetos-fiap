package br.com.fiap.tds.view;

import javax.swing.JOptionPane;
import br.com.fiap.tds.bean.Funcionario;

//Classe criada por:  Pablo André Nunes
public class FuncionarioView {

	public static void main(String[] args) {

		String stringNome = JOptionPane.showInputDialog("Digite o nome:");
		Funcionario funcionario = new Funcionario(stringNome);

		JOptionPane.showInternalMessageDialog(null, "Nome: " + funcionario.nomeMaiusculo(stringNome));

	}

}
