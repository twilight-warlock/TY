import java.util.Scanner;
class Substitution
{
    public static StringBuffer encryptSub(String text){

        StringBuffer result = new StringBuffer();

        for (int i=0; i<text.length(); i++){
            switch((char)((int)text.charAt(i))){
                case 'a':   result.append("z");
                            break;
                case 'b':   result.append("y");
                            break;
                case 'c':   result.append("x");
                            break;                              
                case 'd':   result.append("w");
                            break;                              
                case 'e':   result.append("v");
                            break;                              
                case 'f':   result.append("u");
                            break;                                                         
                case 'g':   result.append("t");
                            break;                              
                case 'h':   result.append("s");
                            break;                              
                case 'i':   result.append("r");
                            break;                              
                case 'j':   result.append("q");
                            break;                                                           
                case 'k':   result.append("p");
                            break;                              
                case 'l':   result.append("o");
                            break;                              
                case 'm':   result.append("n");
                            break;                              
                case 'n':   result.append("m");
                            break;                              
                case 'o':   result.append("l");
                            break;                              
                case 'p':   result.append("k");
                            break;                              
                case 'q':   result.append("j");
                            break;                              
                case 'r':   result.append("i");
                            break;                              
                case 's':   result.append("h");
                            break;                              
                case 't':   result.append("g");
                            break;                              
                case 'u':   result.append("f");
                            break;                              
                case 'v':   result.append("e");
                            break;                              
                case 'w':   result.append("d");
                            break;                              
                case 'x':   result.append("c");
                            break;                              
                case 'y':   result.append("b");
                            break;   
                case 'z':   result.append("a");
                            break;     
                // Capital   
                case 'A':   result.append("Z");
                            break;
                case 'B':   result.append("Y");
                            break;
                case 'C':   result.append("X");
                            break;                              
                case 'D':   result.append("W");
                            break;                              
                case 'E':   result.append("V");
                            break;                              
                case 'F':   result.append("U");
                            break;                                                         
                case 'G':   result.append("T");
                            break;                              
                case 'H':   result.append("S");
                            break;                              
                case 'I':   result.append("R");
                            break;                              
                case 'J':   result.append("Q");
                            break;                                                           
                case 'K':   result.append("P");
                            break;                              
                case 'L':   result.append("O");
                            break;                              
                case 'M':   result.append("N");
                            break;                              
                case 'N':   result.append("M");
                            break;                              
                case 'O':   result.append("L");
                            break;                              
                case 'P':   result.append("K");
                            break;                              
                case 'Q':   result.append("J");
                            break;                              
                case 'R':   result.append("I");
                            break;                              
                case 'S':   result.append("H");
                            break;                              
                case 'T':   result.append("G");
                            break;                              
                case 'U':   result.append("F");
                            break;                              
                case 'V':   result.append("E");
                            break;                              
                case 'W':   result.append("D");
                            break;                              
                case 'X':   result.append("C");
                            break;                              
                case 'Y':   result.append("B");
                            break;   
                case 'Z':   result.append("A");
                            break;                            
                default:  continue;
            }
        }
        return result;
    }

    public static StringBuffer decryptSub(String text){

        StringBuffer result = new StringBuffer();

        for (int i=0; i<text.length(); i++){
            switch((char)((int)text.charAt(i))){
                case 'a':   result.append("z");
                            break;
                case 'b':   result.append("y");
                            break;
                case 'c':   result.append("x");
                            break;                              
                case 'd':   result.append("w");
                            break;                              
                case 'e':   result.append("v");
                            break;                              
                case 'f':   result.append("u");
                            break;                                                         
                case 'g':   result.append("t");
                            break;                              
                case 'h':   result.append("s");
                            break;                              
                case 'i':   result.append("r");
                            break;                              
                case 'j':   result.append("q");
                            break;                                                           
                case 'k':   result.append("p");
                            break;                              
                case 'l':   result.append("o");
                            break;                              
                case 'm':   result.append("n");
                            break;                              
                case 'n':   result.append("m");
                            break;                              
                case 'o':   result.append("l");
                            break;                              
                case 'p':   result.append("k");
                            break;                              
                case 'q':   result.append("j");
                            break;                              
                case 'r':   result.append("i");
                            break;                              
                case 's':   result.append("h");
                            break;                              
                case 't':   result.append("g");
                            break;                              
                case 'u':   result.append("f");
                            break;                              
                case 'v':   result.append("e");
                            break;                              
                case 'w':   result.append("d");
                            break;                              
                case 'x':   result.append("c");
                            break;                              
                case 'y':   result.append("b");
                            break;   
                case 'z':   result.append("a");
                            break;     
                // Capital   
                case 'A':   result.append("Z");
                            break;
                case 'B':   result.append("Y");
                            break;
                case 'C':   result.append("X");
                            break;                              
                case 'D':   result.append("W");
                            break;                              
                case 'E':   result.append("V");
                            break;                              
                case 'F':   result.append("U");
                            break;                                                         
                case 'G':   result.append("T");
                            break;                              
                case 'H':   result.append("S");
                            break;                              
                case 'I':   result.append("R");
                            break;                              
                case 'J':   result.append("Q");
                            break;                                                           
                case 'K':   result.append("P");
                            break;                              
                case 'L':   result.append("O");
                            break;                              
                case 'M':   result.append("N");
                            break;                              
                case 'N':   result.append("M");
                            break;                              
                case 'O':   result.append("L");
                            break;                              
                case 'P':   result.append("K");
                            break;                              
                case 'Q':   result.append("J");
                            break;                              
                case 'R':   result.append("I");
                            break;                              
                case 'S':   result.append("H");
                            break;                              
                case 'T':   result.append("G");
                            break;                              
                case 'U':   result.append("F");
                            break;                              
                case 'V':   result.append("E");
                            break;                              
                case 'W':   result.append("D");
                            break;                              
                case 'X':   result.append("C");
                            break;                              
                case 'Y':   result.append("B");
                            break;   
                case 'Z':   result.append("A");
                            break;                            
                default:  continue;
            }
        }
        return result;
    }


    public static void main(String[] args)
    {
        Scanner ob = new Scanner(System.in);
        System.out.println("Enter text");
        String text = ob.next();
        System.out.println("Text  : " + text);
        StringBuffer cipher = encryptSub(text);
        System.out.println("Cipher: " + cipher);
        System.out.println("Decrypt Cipher: " + decryptSub(cipher.toString()));
    }
}