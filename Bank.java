public class Bank {
    public static void main(String[] args) {
        int[][][] opers = {
                { {100, -50, 25}, {150,-300}, {300,-90,100} },
                { {90, -60, 250}, {300,20,-100} },
                { {20, 50}, {300}, {20,-20,40}, {100,-200} }
        };
        int[] sum = new int[opers.length]; int i = 0;
        for (int[][] customer: opers) {
            for (int[] account: customer) {
                for (int n: account)
                    sum[i] += n;
            }
            i++;
        }
        for (int el: sum)
            System.out.print(el + " ");
    }
}
