class Solution {
    public boolean isPalindrome(int number) {
        int original=number;
        int reversed=0;
        while(number>0){
            int remainder=number%10;
            reversed=(reversed*10)+remainder;
            number=number/10;
        }
        if(reversed==original){
            return true;
        }return false;
}
public static void main(String args[]){
    Solution s=new Solution();
    System.out.println(s.isPalindrome(121));
    System.out.println(s.isPalindrome(-121));
    System.out.println(s.isPalindrome(10));
}
}