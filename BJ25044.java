import java.util.*;

public class BJ25044
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> L = new ArrayList<String>();

        int N = scan.nextInt();
        int K = scan.nextInt();
        int[] array = {3, 3, 18};

        int hour = 15;
        int minute = 0;
        int day = 0;

        if (N == 0)
        {
            System.out.println("15 : 00");
            System.out.println("18 : 00");

            if (K == 60) System.out.println((hour+1) + " : " + "00");
            else System.out.println("21 : " + (minute+K)+ 0);
        }
        else
        {
            for (int i = 0; i < N; i++)
            {
                for (int j = 0; j < array.length; j++)
                {
                    hour += array[j];
                    if (j == 2) minute += K;

                    if (minute >= 60)
                    {
                        hour += (minute / 60);
                        minute %= 60;
                    }

                    if (hour >= 24)
                    {
                        hour %= 24;
                        day += 1;
                    }

                    if (day == N)
                        L.add(hour + " : " + minute);
                }
            }
            System.out.println(L.size());

            Iterator<String> it = L.iterator();
            while (it.hasNext())
            {
                String a = it.next();
                System.out.println(a);
            }
        }
    }
}
