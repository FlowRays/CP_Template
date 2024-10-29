# description
sa
# tabtrigger
sa
# snippet
```cpp
template<class T, class Cmp = less<T>>
struct RMQ {
    const Cmp cmp = Cmp();
    static constexpr unsigned B = 64;
    using u64 = unsigned long long;
    int n;
    vector<vector<T>> a;
    vector<T> pre, suf, ini;
    vector<u64> stk;

    RMQ() {}
    RMQ(const vector<T> &v) {
        init(v);
    }

    void init(const vector<T> &v) {
        n = v.size();
        pre = suf = ini = v;
        stk.resize(n);
        if (!n) return;
        const int M = (n-1)/B + 1;
        const int lg = __lg(M);
        a.assign(lg+1, vector<T>(M));
        forn(i,M) {
            a[0][i] = v[i*B];
            for(int j=1;j<B && i*B+j<n;j++) {
                a[0][i] = min(a[0][i], v[i*B+j], cmp);
            }
        }
        fore(i,1,n-1) if(i%B) pre[i] = min(pre[i], pre[i - 1], cmp);
        for(int i=n-2;i>=0;i--) if(i%B != B-1) suf[i] = min(suf[i], suf[i + 1], cmp);
        forn(j,lg) {
            for(int i=0;i+(2<<j)<=M;i++) {
                a[j+1][i] = min(a[j][i], a[j][i+(1<<j)], cmp);
            }
        }
        forn(i,M) {
            const int l = i*B;
            const int r = min(1U * n, l + B);
            u64 s = 0;
            fore(j,l,r-1) {
                while(s && cmp(v[j], v[__lg(s) + l])) {
                    s ^= 1ULL << __lg(s);
                }
                s |= 1ULL << (j - l);
                stk[j] = s;
            }
        }
    }

    T operator()(int l, int r) {
        if(l/B != (r-1)/B) {
            T ans = min(suf[l], pre[r-1], cmp);
            l = l/B+1;
            r = r/B;
            if(l<r) {
                int k = __lg(r-l);
                ans = min({ans, a[k][l], a[k][r-(1<<k)]}, cmp);
            }
            return ans;
        } else {
            int x = B*(l/B);
            return ini[__builtin_ctzll(stk[r-1]>>(l-x))+l];
        }
    }    
};

struct SA {
    int n;
    vi sa,rk,lc;
    RMQ<int> rmq;

    SA(string &s) {
        n = s.size();
        sa.resize(n);
        lc.resize(n-1);
        rk.resize(n);
        iota(all(sa),0);
        sort(all(sa),[&](int a,int b){return s[a]<s[b];});
        rk[sa[0]] = 0;
        fore(i,1,n-1) rk[sa[i]] = rk[sa[i-1]]+(s[sa[i]] != s[sa[i-1]]);
        int k = 1;
        vi tmp,cnt(n);
        tmp.reserve(n);
        while(rk[sa[n-1]] < n-1) {
            tmp.clear();
            forn(i,k) tmp.pb(n-k+i);
            for(auto i: sa) if(i>=k) tmp.pb(i-k);
            fill(all(cnt),0);
            forn(i,n) cnt[rk[i]]++;
            fore(i,1,n-1) cnt[i] += cnt[i-1];
            for(int i=n-1;i>=0;--i) sa[--cnt[rk[tmp[i]]]] = tmp[i];
            swap(rk,tmp);
            rk[sa[0]] = 0;
            fore(i,1,n-1) {
                rk[sa[i]] = rk[sa[i-1]]+(tmp[sa[i-1]] < tmp[sa[i]] || sa[i-1]+k == n || tmp[sa[i-1]+k] < tmp[sa[i]+k]);
            }
            k *= 2;
        }
        for(int i=0,j=0;i<n;++i) {
            if(!rk[i]) j = 0;
            else {
                for(j-=j>0;i+j<n && sa[rk[i]-1]+j<n && s[i+j]==s[sa[rk[i]-1]+j];) ++j;
                lc[rk[i]-1] = j;
            }
        }
        rmq.init(lc);
    }

    int lcp(int i,int j) {
        i = rk[i], j = rk[j];
        if(i>j) swap(i,j);
        debug_assert(i != j);
        return rmq(i,j);
    }
};
```