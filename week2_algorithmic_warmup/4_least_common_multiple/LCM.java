import java.util.*;

public class LCM {
  private static long lcm_naive(int a, int b) {
    long gcd=0;
    if(b==0){
        gcd=a;
    }
    else{
        int c=a%b;
        lcm_naive(b,c);
    }

    return ((long) a * b)/gcd;
  }

  public static void main(String args[]) {
    Scanner scanner = new Scanner(System.in);
    int a = scanner.nextInt();
    int b = scanner.nextInt();

    System.out.println(lcm_naive(a, b));
  }
}
