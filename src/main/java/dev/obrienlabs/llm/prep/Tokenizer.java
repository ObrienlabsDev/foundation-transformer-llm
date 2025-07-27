package dev.obrienlabs.llm.prep;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Tokenizer {
	
	public void parse() {
		try {
			File file = new File(getClass().getClassLoader().getResource("data/train.txt").getFile());
			Scanner scanner = new Scanner(file);
		} catch (IOException ioe) {
			ioe.printStackTrace();
		}
		
	}

	public static void main(String[] args) {
		Tokenizer tokenizer = new Tokenizer();
		tokenizer.parse();

	}

}
