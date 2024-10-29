# description
dfs_f
# tabtrigger
dfs_f
# snippet
```cpp
function<void(int)> dfs = [&](int u) {
    for(auto v: e[u]) {
        dfs(v);
        $0
    }
};
```