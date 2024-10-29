# description
hash
# tabtrigger
hash
# snippet
```cpp
uniform_int_distribution<ll> dist(0.25*mod, 0.75*mod);
const ll mod1 = 1e9+7;
const ll mod2 = 1e9+9;
const ll k1 = dist(rng);
const ll k2 = dist(rng);

struct Hash {
    vi h1, h2, b1, b2;
    vi s;
    ll n;

    Hash(vi ss) {
        n = ss.size()-1;
        s = ss;
        h1.resize(n+1), h2.resize(n+1);
        b1.resize(n+1), b2.resize(n+1);
        b1[0] = b2[0] = 1;
        fore(i,1,n) {
            b1[i] = b1[i-1]*k1%mod1;
            h1[i] = (h1[i-1]*k1+s[i])%mod1;
            b2[i] = b2[i-1]*k2%mod2;
            h2[i] = (h2[i-1]*k2+s[i])%mod2;
        }
    }

    pii get(ll l,ll r) {
        ll t1 = ((h1[r]-h1[l-1]*b1[r-l+1])%mod1+mod1)%mod1;
        ll t2 = ((h2[r]-h2[l-1]*b2[r-l+1])%mod2+mod2)%mod2;
        return make_pair(t1,t2);
    }
};
```