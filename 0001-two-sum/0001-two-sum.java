class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result=new int[2];
        int arrayIndex=0;
       for(int i=0;i<nums.length;i++){
        for(int j=i+1;j<nums.length;j++){
            if(nums[i]+nums[j]==target){
                result[arrayIndex++]=i;
                result[arrayIndex]=j;
            }
        }
       }
     return result;
    }
    public static void main(String args[]){
        Solution s=new Solution();
        int[] arr={2,7,11,15};
        int target=9;
        s.twoSum(arr, target);
    }
}