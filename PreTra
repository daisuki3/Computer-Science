struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(Null) {}
}

vector<int> preorderTraversal(TreeNode* root){
    vector<int> ans;
    stack<TreeNode*> s;

    TreeNode* tmp = root;

    while(tmp || !s.empty()){
        //not empty
        if(tmp){
            ans.push_back(tmp);
            s.push(tmp);
            tmp = tmp->left;
        }
        else{
            tmp = s.top();
            s.pop();
            tmp = tmp -> right;
        }
    }
}
