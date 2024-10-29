# description
read_edge_weight
# tabtrigger
rew
# snippet
```cpp
vpi e(n+1);
forn(i,n-1) {
    int u,v,w;
    io.r(u,v,w);
    e[u].eb(v,w);
    e[v].eb(u,w);
}
```