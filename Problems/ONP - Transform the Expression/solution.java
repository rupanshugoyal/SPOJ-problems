import java.util.*;
import java.lang.*;

public class Main
{
	public static void main(String[] args) {
        
        Scanner S = new Scanner(System.in);
        
        int testcases = S.nextInt();
        
        for(int i = 0; i <= testcases; i++){
            
            String expression = S.nextLine();
            String[] chars = expression.split("");
            
            //for(int j = 0; j<chars.length; j++)System.out.println(chars[j]);
            
            ArrayList<String> evalstack = new ArrayList<String>();
            for(String character : chars){
                
                if(character.equals(")")){
                    int index = 0;
                    for(int j = evalstack.size()-1; j>=0 ; j--){
                        if(evalstack.get(j).equals("(")){
                            index = j;
                            break;
                        }
                    }
                    
                    ArrayList<String> part = new ArrayList<String>();
                    int limit = evalstack.size();
                    for(int j = index+1 ; j < limit; j++){
                        part.add(evalstack.get(index+1));
                        evalstack.remove(index+1);
                    }
                    evalstack.remove(index);
                    
                    String addpart = part.get(0) + part.get(2) + part.get(1);
                    
                    evalstack.add(addpart);
                }
                else{
                    evalstack.add(character);
                }
                
            }
            for(String q : evalstack)System.out.print(q);
        }
	}
}
