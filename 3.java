import java.util.Scanner;
public class segitiga_Floyd {
    public static void main(String args[])
    {
       int rows, number = 2, counter, j;
       //To get the user's input
       Scanner input = new Scanner(System.in);
       System.out.println("Masukan tinggi segitiga:");
      
       rows = input.nextInt();
  
   
       for ( counter = 1; counter <= rows ; counter++ )
       {
           for ( j =  (2) ; j <= counter ; j++ )
        
           {
                System.out.print(number+" ");
                //Incrementing the number value
                number++;
           }
           //For new line
           System.out.println();
       }
 }
}