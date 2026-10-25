class Solution {
    public int getSum(int a, int b) {
        // XOR to get the sum without carry
        // AND to get the carry
        // continue to do this until carry is 0

        while (b != 0) {
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }

        return a;
    }
}
