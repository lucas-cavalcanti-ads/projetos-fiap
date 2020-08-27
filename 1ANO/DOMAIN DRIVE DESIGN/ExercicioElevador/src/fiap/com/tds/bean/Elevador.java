package fiap.com.tds.bean;

public class Elevador {
	
	//Atributos
	private int andar;
	private int andarAtual;
	private int capacidadeMaxima;
	private int quantidadePessoas;
	
	
	//CONTRUTORES
	public Elevador(){ //VAZIO
		
	}
	
	//METODOS - gets e sets
	
	public Elevador (int capacidadeMaxima,int andar) {
		
		this.andar = andar;
		this.capacidadeMaxima = capacidadeMaxima;
	}
	
	public int subir (int subiu) {
		this.andarAtual += subiu;
		return this.andarAtual;
	}
	
	public int descer (int desceu){
		
		if(validarAndar(desceu)) {
			
			this.andarAtual -= desceu;
			
		}
		
		return this.andarAtual;
	}
	
	public int entrar(int maisPessoas) {
		
		if(validarCapacidade(maisPessoas)) {
			
			this.quantidadePessoas += maisPessoas;
			
		}
		
		return this.quantidadePessoas;
	}
	
	public void sair(int menosPessoas){
		
		if(validarCapacidade(menosPessoas * -1)) {
			
			this.quantidadePessoas -= menosPessoas;
			
		}
		
	}
	
	//GETS E SETS
	
	public int getAndar() {
		
		return this.andar;
		
	}
	
	public int getAndarAtual() {
		
		return this.andarAtual;
		
	}
	
	public int getCapacidadeMaxima() {
		
		return this.capacidadeMaxima;
		
	}

	public int getQuantidadePessoas() {
	
		return this.quantidadePessoas;
	
	}
	
	public void setAndar(int andar) {
		
		this.andar = andar;
		
	}
	
	public void setAndarAtual(int andarAtual) {
		
		this.andarAtual = andarAtual;
		
	}
	
	public void setCapacidadeMaxima(int capacidadeMaxima) {
		
		this.capacidadeMaxima = capacidadeMaxima;
		
	}

	public void setQuantidadePessoas(int quantidadePessoas) {
	
		this.quantidadePessoas = quantidadePessoas;
	
	}
	
	
	//Metodos de validacao
	//VERIFICA SE ADICIONA PESSOAS NO ELEVADOR
	private boolean validarCapacidade(int quantidade) {
		
		if(quantidade >=0){ //ADICIONA
			
			return quantidadePessoas + quantidade <= capacidadeMaxima;
			
		}else {//RETIRA
		
			return quantidadePessoas + quantidade >= 0;
		}
	}
	
	//VERIFICA SE ADICIONA PESSOAS NO ELEVADOR
	private boolean validarAndar(int quantidade) {
		
		if(quantidade >=0){ //SOBE
			
			return quantidadePessoas + quantidade <= capacidadeMaxima;
			
		}else {//DESCE
		
			return quantidadePessoas + quantidade >= 0;
		}
	}
}
