class Solution {
    public int addDigits(int num) {
        String numString=String.valueOf(Math.abs(num));
        int numLength=numString.length();
        while(numLength>1){
            int sum=0;
            for(int i=0;i<numLength;i++){
            int remainder=num%10;
            sum+=remainder;
            num=num/10;
            }
            num=sum;
            numString=String.valueOf(Math.abs(num));
            numLength=numString.length();
        }
        return num;
    }
}