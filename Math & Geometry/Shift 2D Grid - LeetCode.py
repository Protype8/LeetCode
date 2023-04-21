class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<vector<int>> y(grid);
        y[0][0] = 0;
        for(int i = 0;i < grid.size();i++){
            for(int j = 0; j < grid[i].size();j++){
                int total = i*grid[i].size()+j+k;
                int row = (total/grid[i].size())%grid.size();
                int col = total%grid[i].size();
                y[row][col] = grid[i][j];
            }
        }
        return y;
    }
};
