import java.util.*;
import java.lang.*;

public class Main
{
    static boolean checkPrime(int num){
        int limit = (int) Math.sqrt(num);
        for(int i = 2 ; i <= limit; i++){
            if(num%i == 0){
                return false;
            }
        }
        return true;
    }
    
	public static void main(String[] args) {
        Scanner S = new Scanner(System.in);
        int testcases = S.nextInt();
        int L, R;
        for(int i = 0; i<testcases; i++){
            L = S.nextInt();
            R = S.nextInt();
            
            if(L == 1)
                L = 2;
            
            for(int num = L; num <= R; num++){
                if( num%6 == 1 || num%6 == 5 || num == 2 || num == 3){
                    if(checkPrime(num)){
                        System.out.println(num);
                    }
                }
            }
            //System.out.println();
        }
	}
}
