# description
hld
# tabtrigger
hld
# snippet
```cpp
struct HLD {
    int n,idx;
    vii e;
    vi sz,fa,dep,hs,top,l,r,id;

    HLD() {}

    HLD(int n) {
        init(n);
    }

    void init(int n) {
        this->n = n, idx = 0;
        e.assign(n+1,{});
        sz.resize(n+1);
        fa.resize(n+1);
        dep.resize(n+1);
        hs.assign(n+1,0);
        top.resize(n+1);
        l.resize(n+1);
        r.resize(n+1);
        id.resize(n+1);
    }

    void add(int u,int v) {
        e[u].pb(v);
        e[v].pb(u);
    }

    void work(int root = 1) {
        dfs1(root,0);
        dfs2(root,root);
    }

    void dfs1(int u,int f) {
        sz[u] = 1;
        fa[u] = f;
        dep[u] = dep[f]+1;
        for(auto v: e[u]) {
            if(v == f) continue;
            dfs1(v,u);
            sz[u] += sz[v];
            if(!hs[u] || sz[v] > sz[hs[u]]) hs[u] = v;
        }
    }

    void dfs2(int u,int t) {
        top[u] = t;
        l[u] = ++idx;
        id[idx] = u;
        if(hs[u]) dfs2(hs[u],t);
        for(auto v: e[u]) {
            if(v == hs[u] || v == fa[u]) continue;
            dfs2(v,v);
        }
        r[u] = idx;
    }

    vector<pii> get_path(int u,int v) {
        vector<pii> res;
        while(top[u] != top[v]) {
            if(dep[top[u]] < dep[top[v]]) swap(u,v);
            res.eb(l[top[u]],l[u]);
            u = fa[top[u]];
        }
        if(dep[u] < dep[v]) swap(u,v);
        res.eb(l[v],l[u]);
        return res;
    }

    int lca(int u,int v) {
        while(top[u] != top[v]) {
            if(dep[top[u]] < dep[top[v]]) v = fa[top[v]];
            else u = fa[top[u]];
        }
        return dep[u] < dep[v] ? u : v; 
    }

    int dist(int u, int v) {
        return dep[u] + dep[v] - 2 * dep[lca(u, v)];
    }

    int jump(int u, int k) {
        if(dep[u] < k) return -1;
        int d = dep[u] - k;
        while(dep[top[u]] > d) u = fa[top[u]];
        return id[l[u]-dep[u]+d];
    }
    
    bool isAncester(int u, int v) {
        return l[u] <= l[v] && r[v] <= r[u];
    }

    // example
    void modify(int u,int v,int k) {
        while(top[u] != top[v]) {
            if(dep[top[u]] < dep[top[v]]) swap(u,v);
            // seg.modify(l[top[u]],l[u],{k});
            u = fa[top[u]];
        }
        if(dep[u] < dep[v]) swap(u,v);
        // seg.modify(l[v],l[u],{k});
    }

    // example
    int query(int u,int v) {
        int res = 0;
        while(top[u] != top[v]) {
            if(dep[top[u]] < dep[top[v]]) swap(u,v);
            // res += seg.query(l[top[u]],l[u]).s;
            u = fa[top[u]];
        }
        if(dep[u] < dep[v]) swap(u,v);
        // res += seg.query(l[v],l[u]).s;
        return res;
    }

    pair<vi,ve<pii>> compress(vi v) {
        auto cmp = [&](int a, int b) { return l[a] < l[b]; };
        sort(all(v),cmp);
        v.erase(unique(all(v)),v.end());
        int k = v.size();
        forn(i,k-1) v.pb(lca(v[i],v[i+1]));
        sort(all(v),cmp);
        v.erase(unique(all(v)),v.end());
        ve<pii> edges;
        vi stk;
        for(auto x: v){
            while(!stk.empty() && r[stk.back()] < l[x]) stk.pop_back();
            if(!stk.empty()) edges.eb(stk.back(),x);
            stk.pb(x);
        }
        return {v, edges};
    }
};
```