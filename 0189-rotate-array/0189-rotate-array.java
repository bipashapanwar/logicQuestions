class Solution {
    public void rotate(int[] nums, int k) {
        int length=nums.length;
        k=k%length;
        int[] tempArray=new int[k];
            for(int i=0;i<k;i++){
                tempArray[i]=nums[length-k+i];
            }
            for(int j=length-1;j>=k;j--){
                nums[j]=nums[j-k];
            }
            for(int l=0;l<k;l++){
                nums[l]=tempArray[l];
            }
    }
}