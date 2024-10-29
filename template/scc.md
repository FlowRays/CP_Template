# description
scc
# tabtrigger
scc
# snippet
```cpp
struct SCC {
    vii &e, scc;
    vi dfn, low, be;
    vector<bool> ins;
    stack<int> stk;
    int n, idx, cnt;

    SCC(vii &e): e(e) {
        n = (int)e.size()-1;
        dfn.assign(n+1,0);
        low.assign(n+1,0);
        be.assign(n+1,0);
        ins.assign(n+1,false);
        scc.resize(n+1);
        idx = cnt = 0;
        fore(i,1,n) if(!dfn[i]) dfs(i);
    }

    void dfs(int u) {
        dfn[u] = low[u] = ++idx;
        ins[u] = true;
        stk.push(u);
        for(auto v: e[u]) {
            if(!dfn[v]) dfs(v);
            if(ins[v]) low[u] = min(low[u],low[v]);
        }
        if(dfn[u] == low[u]) {
            cnt++;
            while(true) {
                int v = stk.top();
                stk.pop();
                ins[v] = false;
                scc[cnt].pb(v);
                be[v] = cnt;
                if(v == u) break;
            }
        }
    }
};
```