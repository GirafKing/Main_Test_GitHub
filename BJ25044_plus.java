import java.util.*;

public class BJ25044_plus 
{
    public static void main(String[] args) 
    {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int K = scan.nextInt();

        int[] step = {3, 3, 18};   // 시간 단위

        int hour = 15, minute = 0, day = 0;
        ArrayList<String> L = new ArrayList<>();

        // ✅ 시작 시각(0일차 15:00)도 이벤트이므로, N일차면 먼저 수집
        if (day == N) 
        {
            L.add(String.format("%02d:%02d", hour, minute));
        }

        // 날짜 분기 없이 한 로직으로만 처리
        outer:
        while (day <= N && L.size() < 3) 
        {
            for (int j = 0; j < 3; j++) 
            {
                // 1) 시간 증가
                hour += step[j];
                if (j == 2) minute += K; // 18h + K분

                // 2) 캐리 정규화
                if (minute >= 60) { hour += minute / 60; minute %= 60; }

                // 3) 자정 넘김(날짜 증가)
                if (hour >= 24) { hour %= 24; day++; }

                // 4) N일차면 수집
                if (day == N) 
                {
                    L.add(String.format("%02d:%02d", hour, minute));
                    if (L.size() == 3) break outer;
                }

                // N일차를 넘었으면 끝
                if (day > N) break outer;
            }
        }

        // 출력
        System.out.println(L.size());
        for (String t : L) System.out.println(t);
    }
}