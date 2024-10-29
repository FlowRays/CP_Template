# description
dfs
# tabtrigger
dfs
# snippet
```cpp
function<void(int,int)> dfs = [&](int u,int fa) {
    for(auto v: e[u]) {
        if(v == fa) continue;
        dfs(v,u);
        $0
    }
};
```