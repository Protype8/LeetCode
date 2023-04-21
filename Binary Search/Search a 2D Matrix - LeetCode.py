class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int left = 0;
        int right = matrix.length - 1;
        while(left<=right){
            int mid = left + (right - left) / 2;
            if(matrix[mid][0] == target){
                left = mid+1;
                break;
            }
            else if(matrix[mid][0]>target){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        System.out.println(left);
        int matrix_no = left > 0 ? left-1:left;
        left = 0;
        right = matrix[matrix_no].length - 1;
        while(left<=right){
            int mid = left + (right - left) / 2;
            if(matrix[matrix_no][mid] == target){
                return true;
            }
            else if(matrix[matrix_no][mid]>target){
                right = mid - 1;
         
            }
            else{
                left = mid + 1;
              
            }
