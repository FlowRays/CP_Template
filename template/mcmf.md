# description
mcmf
# tabtrigger
mcmf
# snippet
```cpp
const int V = 2e4+10;
const int E = 2e5+10;

template<typename T>
struct MCMF {
    struct edge {
        int v,nxt;
        T f,c;
    } e[E*2];

    int s,t,vtot;
    int head[V],etot;
    T dis[V],flow,cost;
    int pre[V];
    bool vis[V];

    void addedge(int u,int v,T f,T c,T vf = 0) {
        e[etot] = {v,head[u],f,c}; head[u] = etot++;
        e[etot] = {u,head[v],vf,-c}; head[v] = etot++;
    }

    bool spfa() {
        T inf = numeric_limits<T>::max() / 2;
        fore(i,1,vtot) {
            dis[i] = inf;
            vis[i] = false;
            pre[i] = -1;
        }
        dis[s] = 0;
        vis[s] = true;
        queue<int> q;
        q.push(s);
        while(q.size()) {
            int u = q.front();
            q.pop();
            vis[u] = false;
            for(int i=head[u];~i;i=e[i].nxt) {
                int v = e[i].v;
                if(e[i].f && dis[v] > dis[u] + e[i].c) {
                    dis[v] = dis[u] + e[i].c;
                    pre[v] = i;
                    if(!vis[v]) {
                        vis[v] = true;
                        q.push(v);
                    }
                }
            }
        }
        return dis[t] != inf;
    }

    void augment() {
        int u = t;
        T f = numeric_limits<T>::max();
        while(~pre[u]) {
            f = min(f,e[pre[u]].f);
            u = e[pre[u]^1].v;
        }
        flow += f;
        cost += f*dis[t];
        u = t;
        while(~pre[u]) {
            e[pre[u]].f -= f;
            e[pre[u]^1].f += f;
            u = e[pre[u]^1].v;
        }
    }

    pair<T,T> solve() {
        flow = 0;
        cost = 0;
        while(spfa()) augment();
        return {flow,cost};
    }

    void init(int s_,int t_,int vtot_) {
        s = s_, t = t_, vtot = vtot_;
        etot = 0;
        fore(i,1,vtot) head[i] = -1;
    }
};
```