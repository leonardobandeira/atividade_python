import java.util.*;

//2 - Salve em um arquivo .csv o first_name e o gender de cada pessoa. E imprima na tela a média das idades;

public class Teste{
	public static void main(String []args){
		//Endereco do arquivo	
		String end = ();
		
		double media = 0;
		int cont = 0;
		String[] dados = new String();
		
		try{
			//Objeto de escrita
			FilerWriter base = new FilerWriter("dados.csv")
			PrintWriter maquina = new PrintWriter(base);
			
			//Buffer de leitura	abertura		
			BufferedReader arquivo = new BufferedReader(new FileReader ("data (1).csv");
			
			//Leitura do arquivo
			while(arquivo.ready()){
				//Linha atual, cursor
				String linha = arquivo.readLine();
				
				//Quebra de dados
				dados = linhas.split(",");
				
				//Contagem de individuos
				++cont;
				
				//Acumulo das idades
				media += dados[3];
				
				//Salvar dados no arquivo de saida
				maquina.print(dados[0]+ "," + dados[2] + "\n");
			}
			
			//Encerrar buffers
			arquivo.close();
			maquina.close();
			
			//Saida da media
			media = media/cont;
			System.out.printl("A media das idades e: ");
		}catch(IOException ioe){
			ioe.printStackTrace();
		} 
	}
}