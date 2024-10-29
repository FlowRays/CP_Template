# description
sieve
# tabtrigger
sieve
# snippet
```cpp
vi minp, primes;

void sieve(int n) {
    minp.assign(n+1, 0);
    fore(i,2,n) {
        if(minp[i] == 0) {
            minp[i] = i;
            primes.pb(i);
        }
        for(auto p: primes) {
            if(i*p > n) break;
            minp[i*p] = p;
            if(p == minp[i]) break;
        }
    }
}
```