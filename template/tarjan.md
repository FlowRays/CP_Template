# description
tarjan
# tabtrigger
tarjan
# snippet
```cpp
vi dfn(n+1),low(n+1),be(n+1),ins(n+1);
int idx = 0, cnt = 0;
stack<int> stk;
function<void(int)> dfs = [&](int u) {
    dfn[u] = low[u] = ++idx;
    ins[u] = 1;
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
            ins[v] = 0;
            be[v] = cnt;
            if(v == u) break;
        }
    }
};
fore(i,1,n) if(!dfn[i]) dfs(i);
```