struct TreeNode{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

vector<int> PostTra(TreeNode* root){

        stack<TreeNode*> s;
        stack<TreeNode*> out;
        vector<int> ans;
        
        TreeNode* tmp=root;
        
        s.push(tmp);
        
        while(!s.empty()){
            //not empty
            tmp=s.top();
            s.pop();
            out.push(tmp);
            
            if(tmp->left) s.push(tmp->left);
            if(tmp->right) s.push(tmp->right);
        }
        
        while(!out.empty()){
            tmp=out.top();
            out.pop();
            
            ans.push_back(tmp->val);        
        }
        
        return ans;
}
