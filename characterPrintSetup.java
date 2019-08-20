
public class charcterPrintSetup {

	public static void main(String[] args) {
		String characters1 = "!";
		String characters2 = ".,:;";
		String characters3 = "ilI()[]1";
		String characters4 = "fjkrt";
		String characters5 = "abcdeghmnopqsuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ@#$%&*-_=+?234567890";
		String characters = "";
		/*System.out.print("chars = [ ");
		for(int i = 0; i < characters.length()-1; i++){
			System.out.print("'"+ characters.charAt(i) + "', ");
		}
		System.out.println(characters.charAt(characters.length()-1) + "]");
		/**/
		
		
		
		for(int i = 0; i < characters5.length(); i++){
			characters+= characters5.charAt(i);
			System.out.print("def get"+ characters5.charAt(i) + "(font, background):\n");
			System.out.print("\tif (checkColor(background)):\n");
			System.out.print("\t\ti = background\n");
			System.out.print("\telse:\n");
			System.out.print("\t\ti = [0, 0, 0]\n");
			System.out.print("\tif (checkColor(color)):\n");
			System.out.print("\t\tx = color\n");
			System.out.print("\telse:\n");
			System.out.print("\t\tx = [255, 255, 255]\n");
			System.out.print("\tchar = [\n");
			for(int j = 0; j < 7; j++){
				System.out.println("\t\ti, i, i, i, i, i,");
			}
			System.out.println("\t\ti, i, i, i, i, i");
			System.out.println("\t]\n\treturn char\n\n\n");
		}
		
		for(int i = 0; i < characters4.length(); i++){
			characters+= characters4.charAt(i);
			System.out.print("def get"+ characters4.charAt(i) + "(font, background):\n");
			System.out.print("\tif (checkColor(background)):\n");
			System.out.print("\t\ti = background\n");
			System.out.print("\telse:\n");
			System.out.print("\t\ti = [0, 0, 0]\n");
			System.out.print("\tif (checkColor(color)):\n");
			System.out.print("\t\tx = color\n");
			System.out.print("\telse:\n");
			System.out.print("\t\tx = [255, 255, 255]\n");
			System.out.print("\tchar = [\n");
			for(int j = 0; j < 7; j++){
				System.out.println("\t\ti, i, i, i, i,");
			}
			System.out.println("\t\ti, i, i, i, i");
			System.out.println("\t]\n\treturn char\n\n\n");
		}
		
		for(int i = 0; i < characters3.length(); i++){
			characters+= characters3.charAt(i);
			System.out.print("def get"+ characters3.charAt(i) + "(font, background):\n");
			System.out.print("\tif (checkColor(background)):\n");
			System.out.print("\t\ti = background\n");
			System.out.print("\telse:\n");
			System.out.print("\t\ti = [0, 0, 0]\n");
			System.out.print("\tif (checkColor(color)):\n");
			System.out.print("\t\tx = color\n");
			System.out.print("\telse:\n");
			System.out.print("\t\tx = [255, 255, 255]\n");
			System.out.print("\tchar = [\n");
			for(int j = 0; j < 7; j++){
				System.out.println("\t\ti, i, i, i,");
			}
			System.out.println("\t\ti, i, i, i");
			System.out.println("\t]\n\treturn char\n\n\n");
		}
		
		for(int i = 0; i < characters2.length(); i++){
			characters+= characters2.charAt(i);
			System.out.print("def get"+ characters2.charAt(i) + "(font, background):\n");
			System.out.print("\tif (checkColor(background)):\n");
			System.out.print("\t\ti = background\n");
			System.out.print("\telse:\n");
			System.out.print("\t\ti = [0, 0, 0]\n");
			System.out.print("\tif (checkColor(color)):\n");
			System.out.print("\t\tx = color\n");
			System.out.print("\telse:\n");
			System.out.print("\t\tx = [255, 255, 255]\n");
			System.out.print("\tchar = [\n");
			for(int j = 0; j < 7; j++){
				System.out.println("\t\ti, i, i,");
			}
			System.out.println("\t\ti, i, i");
			System.out.println("\t]\n\treturn char\n\n\n");
		}
		
		for(int i = 0; i < characters1.length(); i++){
			characters+= characters1.charAt(i);
			System.out.print("def get"+ characters1.charAt(i) + "(font, background):\n");
			System.out.print("\tif (checkColor(background)):\n");
			System.out.print("\t\ti = background\n");
			System.out.print("\telse:\n");
			System.out.print("\t\ti = [0, 0, 0]\n");
			System.out.print("\tif (checkColor(color)):\n");
			System.out.print("\t\tx = color\n");
			System.out.print("\telse:\n");
			System.out.print("\t\tx = [255, 255, 255]\n");
			System.out.print("\tchar = [\n");
			for(int j = 0; j < 7; j++){
				System.out.println("\t\ti, i,");
			}
			System.out.println("\t\ti, i");
			System.out.println("\t]\n\treturn char\n\n\n");
		}/**/
		
		System.out.println("'''");
		System.out.print("chars = [ ");
		for(int i = 0; i < characters.length()-1; i++){
			System.out.print("'"+ characters.charAt(i) + "', ");
		}
		System.out.println("'"+characters.charAt(characters.length()-1) + "']");
		System.out.println("'''");
		
	}
	
	

}
