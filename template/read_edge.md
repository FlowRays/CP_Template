# description
read_edge
# tabtrigger
red
# snippet
```cpp
vii e(n+1);
forn(i,n-1) {
    int u,v;
    io.r(u,v);
    e[u].pb(v);
    e[v].pb(u);
}
```