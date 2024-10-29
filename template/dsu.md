# description
dsu
# tabtrigger
dsu
# snippet
```cpp
struct DSU {
    vi f, sz;

    DSU(int n): f(n+1), sz(n+1,1) {
        iota(all(f), 0);
    }

    int find(int x) {
        return x == f[x] ? x : f[x] = find(f[x]);
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    bool merge(int x,int y) {
        x = find(x), y = find(y);
        if(x == y) return false;
        sz[x] += sz[y];
        f[y] = x;
        return true;
    }

    int size(int x) {
        return sz[find(x)];
    }
};
```