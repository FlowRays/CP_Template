# description
virtue_tree
# tabtrigger
vir
# snippet
```cpp
vi a(n+1);
io.rv(a);
vii pos(n+1);
fore(i,1,n) pos[a[i]].pb(i);
HLD h(n);
forn(i,n-1) {
    int u,v;
    io.r(u,v);
    h.add(u,v);
}
h.work();
vii e(n+1);
vi st(n+1),dp(n+1);
fore(i,1,n) {
    if(pos[i].empty()) continue;
    for(auto x: pos[i]) st[x] = 1;
    auto [vs,es] = h.compress(pos[i]);
    for(auto x: vs) e[x].clear(),dp[x] = 0; // clear info!
    for(auto [u,v]: es) e[u].pb(v);
    auto dfs = [&](auto&& dfs,int u) -> void {
        for(auto v: e[u]) {
            dfs(dfs,v);
            $0
        }
    };
    dfs(dfs,vs[0]);
    for(auto x: pos[i]) st[x] = 0; 
}
```