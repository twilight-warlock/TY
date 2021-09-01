#include <bits/stdc++.h>
using namespace std;

//creates a graph
void addEdge(vector<int> adj[],int u , int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

//display the graph (adjacency list representation)
void displayGraph(vector<int> adj[],int V){
    cout<<endl<<"Adjacency list representation of the graph: "<<endl;
    for(int i=0;i<V;i++){
        cout<<i;
        for(auto x : adj[i]){
            cout<< "->"<<x;   
        }
        cout<<endl;
    }
    cout<<endl;
}

//bfs function
void bfs(vector<int> adj[], int destination,int source, int V){
    cout<<"**BFS**"<<endl;
    vector<int> path;
    bool found = false;
    // queue using deque...done to iterate through queue which //is not possible using inbuilt queue in STL
    deque<int> q;
    q.push_back(source);

    vector<int> vis(V,0); //visited vector for keeping track o//f visited nodes
    vis[source] = 1;
    cout<<"Queue: "<<q[0]<<endl;
    while(!q.empty()){
        int td = q.front();
        if(td == destination){
            found = true;
            break;
        }
        else{
            path.push_back(td);
        }
        q.pop_front();
        for(auto v : adj[td]){
            if(!vis[v]){
                vis[v] = 1;
                q.push_back(v);
            }
        }
        cout<<"Visited nodes till now: ";
        for(int i=0;i<vis.size();i++){
            if(vis[i] == 1){
                cout<<i<<" ";
            }   
        }
       cout<<endl<<"Queue: ";
       for(int i=0;i<q.size();i++){
           cout<<q[i]<<" ";
       }
        cout<<endl;
    }
    if(found){
        cout<<endl<<"Element found"<<endl;
    }
    else{
        cout<<endl<<"Element not found"<<endl;
    }
    cout<<"BFS Path: ";
    for(auto p : path){
        cout<< p <<" ";
    }
    
    if(found)
        cout<<destination<<endl<<endl;

}

//dfs fucntion
void dfs(vector<int> adj[], int destination,int source, int V){
    cout<<"**DFS**"<<endl;

    vector<int> path;
    bool found = false;
    //stack implemented using deque... done to iterate through //stack which is not possible using inbuilt stack in STL
    deque<int> st;
    st.push_front(source);
    cout<<"Stack: "<<source;
    vector<int> vis(V,0); //visited vector for keeping track o//f visited nodes
    vis[source] = 1;
    while(!st.empty()){
        int td = st.front();
        if(td == destination){
            found = true;
            break;
        }
        else{
            path.push_back(td);
        }
        st.pop_front();
        for(auto x: adj[td]){
            if(!vis[x]){
                vis[x] = 1;
                st.push_front(x);
            }  
        }
        cout<<endl;
        cout<<"Visited nodes till now: ";
        if(found == false){
            for(int i=0;i<vis.size();i++){
                if(vis[i] == 1){
                    cout<<i<<" ";
                }      
            }
        } 
        cout<<endl<<"Stack: ";
        for(int i=0;i<st.size();i++){
           cout<<st[i]<<" ";
        }    
    }
    cout<<endl;
    if(found){
        cout<<endl<<"Element found"<<endl;
    }
    else{
        cout<<endl<<"Element not found"<<endl;
    }
    cout<<"DFS Path: ";
    for(auto p : path){
        cout<< p <<" ";
    }

    if(found)
        cout<<destination<<endl;

}

int main(){
    
    int V,E;
    cout<<"Enter the number of vertices: ";
    cin>>V;
    vector<int> adj[V];

    cout<<"Enter the number of edges: ";
    cin>>E;
    for(int i=0;i<E;i++){
        int a,b;
        cout<<"Enter the vertices of edge "<<i+1<<": ";
        cin>>a>>b;
        addEdge(adj,a,b);
    }
    displayGraph(adj,V);
    int destination,source ;
    cout<<"Enter the source: ";
    cin>>source;
    cout<<"Enter the element to be searched: ";
    cin>>destination;

    bfs(adj, destination, source, V);
    dfs(adj, destination, source, V);
    return 0;
}
 
