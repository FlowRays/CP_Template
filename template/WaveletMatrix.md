# description
WaveletMatrix
# tabtrigger
WaveletMatrix
# snippet
```cpp
struct WaveletMatrix {
    struct BitRank {
        vector<long long> block;
        vector<int> count;
        BitRank() {}
        void resize(int num) {
            block.resize(((num + 1) >> 6) + 1, 0);
            count.resize(block.size(), 0);
        }
        void set(int i, long long val) {
            block[i >> 6] |= (val << (i & 63));
        }
        void build() {
            for (int i = 1; i < block.size(); i++) {
            count[i] = count[i - 1] + __builtin_popcountll(block[i - 1]);
            }
        }
        int rank1(int i) {
            return count[i >> 6] +
                __builtin_popcountll(block[i >> 6] & ((1ULL << (i & 63)) - 1ULL));
        }
        int rank1(int i, int j) {
            return rank1(j) - rank1(i);
        }
        int rank0(int i) { return i - rank1(i); }
        int rank0(int i, int j) {
            return rank0(j) - rank0(i);
        }
    };
    
    int height;
    vector<BitRank> B;
    vector<int> pos;

    WaveletMatrix() {}
    WaveletMatrix(vector<int> vec): WaveletMatrix(vec, *max_element(vec.begin(), vec.end()) + 1) {}
    // sigma: 字母表大小(字符串的话)，数字序列的话是数的种类
    WaveletMatrix(vector<int> vec, int sigma) {
        init(vec, sigma);
    }
    void init(vector<int>& vec, int sigma) {
        height = (sigma == 1) ? 1 : (64 - __builtin_clzll(sigma - 1));
        B.resize(height), pos.resize(height);
        for (int i = 0; i < height; ++i) {
            B[i].resize(vec.size());
            for (int j = 0; j < vec.size(); ++j) {
                B[i].set(j, get(vec[j], height - i - 1));
            }
            B[i].build();
            auto it = stable_partition(vec.begin(), vec.end(), [&](int c) {
                return !get(c, height - i - 1);
            });
            pos[i] = it - vec.begin();
        }
    }
    int get(int val, int i) { return val >> i & 1; }

    // [l, r] 中val出现的频率 (1-base)
    int query(int l, int r, int val) {
        return l == 1 ? query(val, r) : query(val, r) - query(val, l-1);
    }
    // [1, i] 中val出现的频率
    int query(int val, int i) {
        int p = 0;
        for (int j = 0; j < height; ++j) {
            if (get(val, height - j - 1)) {
                p = pos[j] + B[j].rank1(p);
                i = pos[j] + B[j].rank1(i);
            } else {
                p = B[j].rank0(p);
                i = B[j].rank0(i);
            }
        }
        return i - p;
    }
    // [l, r] 中k小
    int kth(int l, int r, int k) {
        l--;
        int res = 0;
        for (int i = 0; i < height; ++i) {
            int j = B[i].rank0(l, r);
            if (j >= k) {
                l = B[i].rank0(l);
                r = B[i].rank0(r);
            } else {
                l = pos[i] + B[i].rank1(l);
                r = pos[i] + B[i].rank1(r);
                k -= j;
                res |= (1 << (height - i - 1));
            }
        }
        return res;
    }
    int query(int i, int j, int a, int b, int l, int r, int x) {
        if (i == j || r <= a || b <= l) return 0;
        if (a <= l && r <= b) return j - i;
        int mid = (l + r) >> 1;
        int left = query(B[x].rank0(i), B[x].rank0(j), a, b, l, mid, x + 1);
        int right = query(pos[x] + B[x].rank1(i), pos[x] + B[x].rank1(j), a, b, mid, r, x + 1);
        return left + right;
    }
    // [l, r] 在 [a, b] 值域的数字个数
    int query(int l, int r, int a, int b) {
        return query(l-1, r, a, b+1, 0, 1 << height, 0);
    }
    int rangemin(int i, int j, int a, int b, int l, int r, int x, int val) {
        if (i == j || r <= a || b <= l) return -1;
        if (r - l == 1) return val;
        int mid = (l + r) >> 1;
        int res = rangemin(B[x].rank0(i), B[x].rank0(j), a, b, l, mid, x + 1, val);
        if (res < 0) return rangemin(pos[x] + B[x].rank1(i), pos[x] + B[x].rank1(j), a, b, mid, r, x + 1, val + (1 << (height - x - 1)));
        else return res;
    }
    // [l, r] 在 [a, b] 值域内存在的最小值是什么，不存在返回-1
    int rangemin(int l, int r, int a, int b) {
        return rangemin(l-1, r, a, b+1, 0, 1 << height, 0, 0);
    }
};
```