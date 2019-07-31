import java.util.*;

public class LargestNumber {
    private static String largestNumber(int[] numbers)  {
        String result = "";
        int max = 0;
        int temp_index;
        int temp_n = numbers.length;
        while(temp_n != 0)
        {
            max = numbers[0];
            temp_index = 0;
            for(int i = 0; i < n; i++)
            {
                max = get_max(max, numbers[i]);
                if(max == numbers[i])
                    temp_index = i;
            }
            numbers[temp_index] = 0;
            result += String.valueOf(max);
            temp_n--;
        }
        System.out.println(result);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        System.out.println(largestNumber(a));
    }
}

