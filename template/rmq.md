# description
rmq
# tabtrigger
rmq
# snippet
```cpp
template<typename T>
struct RMQ {
    using vt = vector<T>;
    using vtt = vector<vt>;
    using func_type = function<T(const T &, const T &)>;

    int n,m;
    vtt f;
    func_type op;
    
    static T default_func(const T &t1, const T &t2) {
        return max(t1,t2);
    }

    RMQ(int n, func_type func) : n(n), m(__lg(n)), f(m+1, vt(n+1)), op(func) {}
    RMQ(const vt &v, func_type func = default_func) : RMQ(int(v.size()), func) {
        fore(i,1,n) f[0][i] = v[i-1];
        fore(j,1,m)
            for(int i=1;i+(1<<j)-1<=n;++i)
                f[j][i] = op(f[j-1][i],f[j-1][i+(1<<(j-1))]);
    }

    T query(int l,int r){
        int s = __lg(r-l+1);
        return op(f[s][l],f[s][r-(1<<s)+1]);
    }
};
```