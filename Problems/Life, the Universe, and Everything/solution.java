import java.util.*;
import java.lang.*;

class solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		while(true){
			int i = 0;
			if(sc.hasNext())
			{	i = sc.nextInt();	}
			if( i != 42){
				System.out.println(i);
			}
			else{
				break;
			}
				
		}
	}
}
