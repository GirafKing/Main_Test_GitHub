import java.util.*;

public class BJ10871 
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int X = scan.nextInt();

        ArrayList<Integer> List = new ArrayList<Integer>(N);

        int i = 0;
        while(i < N)
        {
            int num = scan.nextInt();
            List.add(num);
            i++;
        }

        Iterator<Integer> it = List.iterator();
        while(it.hasNext())
        {
            int number = it.next();
            if (number < X)
                System.out.print(number + " ");
        }
    }
}
