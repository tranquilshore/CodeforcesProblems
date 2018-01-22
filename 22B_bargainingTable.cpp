#include <iostream>
using namespace std;
char G[50][50];
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++)cin>>G[i];
    int ans=0;
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            for(int k=i;k<n;k++)
                for(int l=j,check=true;l<m;l++,check=true){
                    for(int a=i;a<=k;a++)
                        for(int b=j;b<=l;b++)if(G[a][b]=='1')check=false;
                    if(check)ans=max(ans,2*(k-i+1+l-j+1));
                }
    cout<<ans;
}