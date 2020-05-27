```cpp
//矩阵遍历传参技巧 
dfs(row,col)
{
    /*
    code
    */
    dfs(row + (col + 1) / col, (col + 1) % col);
    /*
    code
    */
}
```