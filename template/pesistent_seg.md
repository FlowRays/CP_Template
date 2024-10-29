# description
persistent_seg
# tabtrigger
persistent_seg
# snippet
```cpp
int rt[N], cnt;
int ls[N*60], rs[N*60], s[N*60];
int L = -1e9, R = 1e9;

void modify(int p,int q,int l,int r,int x,int v) {
    if(l == r) s[q] = s[p] + v;
    else {
        int mid = l+r >> 1;
        ls[q] = ls[p], rs[q] = rs[p];
        if(x <= mid) {
            ls[q] = ++cnt;
            modify(ls[p],ls[q],l,mid,x,v);
        } else {
            rs[q] = ++cnt;
            modify(rs[p],rs[q],mid+1,r,x,v);
        }
        s[q] = s[ls[q]] + s[rs[q]];
    }
}
```