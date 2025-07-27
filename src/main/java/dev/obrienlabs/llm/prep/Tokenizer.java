package dev.obrienlabs.llm.prep;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Tokenizer {
	
	public void parse() {
		Scanner scanner = null;
		try {
			File file = new File(getClass().getClassLoader().getResource("data/train.txt").getFile());
			scanner = new Scanner(file);
			while(scanner.hasNext()) {
				String token = scanner.next();
				System.out.println(token);
			}
		} catch (IOException ioe) {
			ioe.printStackTrace();
		} finally {
			scanner.close();
		}
		
	}

	public static void main(String[] args) {
		Tokenizer tokenizer = new Tokenizer();
		tokenizer.parse();

	}

}
