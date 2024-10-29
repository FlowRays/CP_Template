# description
seg
# tabtrigger
seg
# snippet
```cpp
struct Info {
    $0
};

struct Tag {
    
};

Info operator+(const Info &a, const Info &b){
    return {};
}

void apply(Info &x, Tag &a, Tag f) {
    
}

template<class Info, class Tag>
struct LazySegmentTree {
    int n;
    vector<Info> info;
    vector<Tag> tag;

    LazySegmentTree() {}

    LazySegmentTree(int n, Info _init = Info()) {
        init(vector<Info>(n+1, _init));
    }

    LazySegmentTree(const vector<Info> &_init) {
        init(_init);
    }

    void init(const vector<Info> &_init) {
        n = (int)_init.size()-1;
        info.assign((n<<2)+1, Info());
        tag.assign((n<<2)+1, Tag());
        function<void(int,int,int)> build = [&](int u,int l,int r) {
            if(l == r) {
                info[u] = _init[l];
            } else {
                int m = l+r >> 1;
                build(u<<1,l,m), build(u<<1|1,m+1,r);
                pull(u);
            }
        };
        build(1,1,n);
    }

    void pull(int u) {
        info[u] = info[u<<1] + info[u<<1|1];
    }

    void apply(int u, const Tag &v) {
        ::apply(info[u], tag[u], v);
    }

    void push(int u) {
        apply(u<<1,tag[u]);
        apply(u<<1|1,tag[u]);
        tag[u] = Tag();
    }

    void modify(int u,int l,int r,int x, const Info &v) {
        if(l == r) {
            info[u] = v;
        } else {
            int m = l+r >> 1;
            push(u);
            if(x<=m) modify(u<<1,l,m,x,v);
            else modify(u<<1|1,m+1,r,x,v);
            pull(u);
        }
    }

    void modify(int x, const Info &v) {
        modify(1,1,n,x,v);
    }

    Info query(int u,int l,int r,int x,int y) {
        if(x<=l && r<=y) return info[u];
        int m = l+r >> 1;
        push(u);
        if(y<=m) return query(u<<1,l,m,x,y);
        if(x>m) return query(u<<1|1,m+1,r,x,y);
        return query(u<<1,l,m,x,y) + query(u<<1|1,m+1,r,x,y);
    }

    Info query(int l,int r) {
        return query(1,1,n,l,r);
    }

    void modify(int u,int l,int r,int x,int y, const Tag &v) {
        if(l>y || r<x) return;
        if(x<=l && r<=y) return apply(u,v);
        int m = l+r >> 1;
        push(u);
        modify(u<<1,l,m,x,y,v);
        modify(u<<1|1,m+1,r,x,y,v);
        pull(u);
    }

    void modify(int l,int r, const Tag &v) {
        modify(1,1,n,l,r,v);
    }
};
```