import java.util.Scanner;

class ColumnarTranspositionCiper {

    public static void main(String[] args){
        Scanner src = new Scanner(System.in);
        String ogmessage;
        String ogkeyword;
        System.out.println("Enter your message: ");
        ogmessage = src.nextLine();
        ogmessage = ogmessage.toUpperCase();
        System.out.println("Enter your keyword: ");
        ogkeyword = src.nextLine();
        ogkeyword = ogkeyword.toUpperCase();
        String e = getEncrypted(ogmessage,ogkeyword);
        System.out.println("Encrypted message is: " + e);
        System.out.println("Decrypted message is: " + getDecrypted(e,ogkeyword));

    }
    private static String getEncrypted(String mssg,String kwrd) {
        String coded_mssg = "";
        int[] keywordSeqNo = assignNumbers(kwrd);

//        to make sure our message is a multiple of keyword
        int extraLetters = mssg.length() % kwrd.length();
        int dummyCharacters = kwrd.length() - extraLetters;
        if (extraLetters != 0){
            for (int i = 0; i < dummyCharacters; i++) {
                mssg+="-";
            }
        }

        int rows = mssg.length() / kwrd.length();
        int cols = kwrd.length();

        // Converting message into a grid
        char[][] arr = new char[rows][cols];

        int z = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                arr[i][j] = mssg.charAt(z);
                z++;
            }

        }

        // getting array position of numbers
        int curr = 1;
        int numLoc;
        while(cols>0){
            cols--;
            numLoc = getPosition(keywordSeqNo,curr++);
            for(int i=0;i<rows;i++)
                coded_mssg+= arr[i][numLoc];
        }

        return  coded_mssg;

    }

    private static String getDecrypted(String mssg,String kwrd){
        String coded_mssg="";
        int[] keywordSeqNo = assignNumbers(kwrd);

        int rows = mssg.length() / kwrd.length();
        int cols = kwrd.length();
        char[][] arr = new char[rows][cols];

        
        int curr = 1;
        int numLoc;
        int temp=0;
        while (temp<mssg.length()){
//            cols--;
            numLoc = getPosition(keywordSeqNo,curr++);
            for(int j=0;j<rows;j++) {
                arr[j][numLoc] = mssg.charAt(temp);
                temp++;
            }
        }



        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if(arr[i][j] =='-')
                    break;
                coded_mssg+=arr[i][j];
            }
        }

        return coded_mssg;

    }


    private static int[] assignNumbers(String keyword) {
        String temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int[] arr = new int[keyword.length()];

        int init = 0;
        for (int i = 0; i < temp.length(); i++){
            for (int j = 0; j < keyword.length(); j++) {
                if (temp.charAt(i) == keyword.charAt(j)){
                    init++;
                    arr[j] = init;
                }
            }
        }
        return arr;
    }


    private static int getPosition(int[] kwrdList,int curr) {
            for (int j = 0; j < kwrdList.length; j++) {
                if (kwrdList[j] == curr) {
                    return j;
                }
        }
        return 0;
    }

}
