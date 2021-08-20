import java.util.Scanner;
class Additive
{
    public static StringBuffer encryptAdditive(String text, int s)
    {
        StringBuffer result= new StringBuffer();
 
        for (int i=0; i<text.length(); i++)
        {
            if (Character.isUpperCase(text.charAt(i)))
            {
                char ch = (char)(((int)text.charAt(i) +
                                  s - 65) % 26 + 65);
                result.append(ch);
            }
            else
            {
                char ch = (char)(((int)text.charAt(i) +
                                  s - 97) % 26 + 97);
                result.append(ch);
            }
        }
        return result;
    }

    public static StringBuffer decryptAdditive(String text, int s)
    {
        StringBuffer result= new StringBuffer();
 
        for (int i=0; i<text.length(); i++)
        {
            if (Character.isUpperCase(text.charAt(i)))
            {
                char ch = (char)((((int)text.charAt(i)+ (26 -
                                  s) -65) % 26) + 65);
                result.append(ch);
            }
            else
            {
                char ch = (char)((((int)text.charAt(i)+ (26 -
                                  s) - 97) % 26) + 97);
                result.append(ch);
            }
        }
        return result;
    }
 

    public static void main(String[] args)
    {
        Scanner ob = new Scanner(System.in);
        System.out.println("Enter text");
        String text = ob.next();
        System.out.println("Enter shift");
        int s = ob.nextInt();

        System.out.println("Text  : " + text);
        System.out.println("Shift : " + s);
        StringBuffer cipher = encryptAdditive(text, s);
        System.out.println("Cipher: " + cipher);
        System.out.println("Decrypt Cipher: " + decryptAdditive(cipher.toString(), s));
    }
}
