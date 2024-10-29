# description
sat
# tabtrigger
sat
# snippet
```cpp
struct SAT {
    int n;
    vii e;
    vi ans;

    SAT(int n): n(n),e(2*n+1),ans(n+1) {}

    void add(int u,int a,int v,int b) {
        e[u+(a^1)*n].pb(v+b*n);
        e[v+(b^1)*n].pb(u+a*n);
    }

    bool solve() {
        vi dfn(2*n+1),low(2*n+1),be(2*n+1),ins(2*n+1);
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
        fore(i,1,2*n) if(!dfn[i]) dfs(i);
        fore(i,1,n) {
            if(be[i] == be[i+n]) return false;
            ans[i] = be[i] > be[i+n];
        }
        return true;
    }
};
```