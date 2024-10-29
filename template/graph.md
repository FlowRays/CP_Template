# description
graph
# tabtrigger
graph
# snippet
```cpp
struct Graph {
    int n,tot;
    vi in,out;
    vii e;

    Graph() {}

    Graph(int n): n(n),tot(n),in(n*4+1),out(n*4+1),e(n*7+1) {
        build(1,1,n);
    }

    inline void add(int u,int v) {
        e[u].pb(v);
    }

    void build(int u,int l,int r) {
        if(l == r) {
            in[u] = l;
            out[u] = l;
        } else {
            in[u] = ++tot, out[u] = ++tot;
            int mid = l+r >> 1;
            build(u<<1,l,mid), build(u<<1|1,mid+1,r);
            add(in[u],in[u<<1]);
            add(in[u],in[u<<1|1]);
            add(out[u<<1],out[u]);
            add(out[u<<1|1],out[u]);
        }
    }

    void upd(int u,int l,int r,int x,int y,int k) {
        if(x<=l && r<=y) {
            // add: id[u]
        } else {
            int mid = l+r >> 1;
            if(x<=mid) upd(u<<1,l,mid,x,y,k);
            if(y>mid) upd(u<<1|1,mid+1,r,x,y,k);
        }
    }
};
```