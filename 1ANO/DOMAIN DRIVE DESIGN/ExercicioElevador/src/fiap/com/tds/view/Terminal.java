package fiap.com.tds.view;

import javax.swing.JOptionPane;

import fiap.com.tds.bean.Elevador;

public class Terminal {
	public static void main (String arg[]) {
		//Criar objeto do tipo elevador
		Elevador elevador = new Elevador(20, 20);
		
		
		
		int quantidadePessoa = Integer.parseInt(JOptionPane.showInputDialog("Digite o peso da primeira pessoa (kg): "));
		/*/Recebendo informacoes iniciais
		System.out.print("Digite a quantidade de pessoas que cabem: ");
		short quantidadePessoa = teclado.nextShort();
		System.out.print("Digite a quantidade de andares: ");
		short quantidadeAndares = teclado.nextShort();
		
		//Chamar metodos para inicializar o elevador
		elevador.inicializar(quantidadePessoa, quantidadeAndares);
		
		//Exibindo informacoes iniciais
		System.out.println("A quantidade de pessoas que cabem é: " + elevador.capacidadeMaxima);
		System.out.println("A quantidade de andares é: " + elevador.andar);
		System.out.println("O andar atual é: " + elevador.andarAtual + "ºAndar");
		
		//Quantidade de andares que quer subir
		System.out.print("Digite a quantidade de andares que deseja subir: ");
		short qtdSubir = teclado.nextShort();
		elevador.subir(qtdSubir);
		
		//Quantidade de andares que quer descer
		System.out.print("Digite a quantidade de andares que deseja descer: ");
		short qtdDescer = teclado.nextShort();
		elevador.descer(qtdDescer);
		
		//Quantidade de pessoas que entra
		System.out.println("Digite o numero de pessoas que estao entrando: ");
		short qtdEntrar = teclado.nextShort();
		elevador.entrar(qtdEntrar);
		
		//Quantidade de pessoas que sai
		System.out.println("Digite o numero de pessoas que estao saindo: ");
		short qtdSai = teclado.nextShort();
		elevador.sair(qtdSai);
		
		//Exibindo informacoes finiais
		System.out.println("O andar atual é: " + elevador.andarAtual + "ºAndar");
		System.out.println("A quantidade de pessoas no elevador é: " + elevador.quantidadePessoas);
		
		*/
		
	}

}
