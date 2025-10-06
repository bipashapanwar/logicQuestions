class Solution {
    public int maxFreqSum(String s) {
        int maxVowelCount=0;
        int maxConsonantCount=0;
        for(char c='a';c<='z';c++){
            int count=0;
            for(int i=0;i<s.length();i++){
              char ch=Character.toLowerCase(s.charAt(i));
              if(ch==c){count++;}}
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                if(count>maxVowelCount){maxVowelCount=count;}}
            else{
                if(count>maxConsonantCount){maxConsonantCount=count;}}
        }
        return maxVowelCount+maxConsonantCount;
}
}