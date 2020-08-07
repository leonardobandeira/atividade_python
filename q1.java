import java.util.*;

//1 - Faça um código em python3 que leia o arquivo data.csv;

public class Teste{
	public static void main(String []args){
		//Endereco do arquivo	
		String end = (new FileReader ("data (1).csv");
		try{
			//Buffer de leitura	abertura		
			BufferedReader arquivo = new BufferedReader(new FileReader(end));
			while(arquivo.ready()){
				String linha = arquivo.readLine();
				System.out.println(linha+"\n");
			}
			
			arquivo.close();
		}catch(IOException ioe){
			ioe.printStackTrace();
		} 
	}
}