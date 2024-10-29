# description
dsu_w
# tabtrigger
dsu_w
# snippet
```cpp
template<typename T>
struct DSU{
    vi f;
    vector<T> d;
    DSU(int n): f(n+1), d(n+1) {
        iota(all(f), 0);
    }

    int find(int x) {
        if(f[x] != x){
            int rt = find(f[x]);
            d[x] += d[f[x]];
            f[x] = rt;
        }
        return f[x];
    }

    T get(int x, int y) {
        return d[x] - d[y];
    }

    bool same(int x, int y) {
        return find(x) == find(y);
    }

    bool merge(int x, int y, T v) {
        int fx = find(x), fy = find(y);
        if (fx == fy) return false;
        d[fx] = v - d[x] + d[y];
        f[fx] = fy;
        return true;
    }
};
```