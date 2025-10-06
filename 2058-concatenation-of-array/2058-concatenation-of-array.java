class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] ans=new int[(nums.length)*2];
        int ansIndex=0;
        for(int j=0;j<2;j++){
        int numsIndex=0;
        for(int i=0;i<nums.length;i++){
            ans[ansIndex++]=nums[numsIndex++];
        }
        }
        return ans;
    }
}