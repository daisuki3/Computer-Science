#include<iostream>
#include<string>
#include<vector>
using namespace std;

int kmp(string s,string w){
    if(w.empty()) return 0;

    vector<int> wContinueTest(w.size(),0);
    for(int i=1,k=0;i<w.size();++i){  
        while(k && w[i]!=w[k]) //wContainingTest contains the index that if test fail
            k=wContinueTest[k-1]; //only after that index ,where to continue 
        if(w[i]==w[k]) ++k;  
        wContinueTest[i]=k;                    // string equal test
    }

    for(int i=0,k=0;i<s.size();++i){
        while(k && s[i]!=w[k])  
            k=wContinueTest[k-1];
        if(s[i]==w[k]) ++k;
        if(k==w.size()) return i-k+1;
    }

    return -1;
}

int main(){
    cout<<kmp("abcdef","bc");
    return 0;
}
