# description
dijkstra
# tabtrigger
dijkstra
# snippet
```cpp
priority_queue<pii> q;
q.emplace(0,s);
vi d(n+1,-1);
while(q.size()) {
    auto [dis,u] = q.top();
    q.pop();
    if(d[u] != -1) continue;
    d[u] = -dis;
    for(auto [v,w]: e[u]) {
        q.emplace(dis-w,v);
    }
}
```