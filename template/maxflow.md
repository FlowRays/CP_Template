# description
maxflow
# tabtrigger
maxflow
# snippet
```cpp
const int V = 2e4+10;
const int E = 2e5+10;

template<typename T>
struct MaxFlow {
    struct edge {
        int v,nxt;
        T f;
    } e[E*2];

    int s,t,vtot;
    int head[V],etot;
    int dis[V],cur[V];

    void addedge(int u, int v, T f, T vf = 0) {
        e[etot] = {v,head[u],f}; head[u] = etot++;
        e[etot] = {u,head[v],vf}; head[v] = etot++;
    }

    bool bfs() {
        fore(i,1,vtot) {
            dis[i] = 0;
            cur[i] = head[i];
        }
        queue<int> q;
        q.push(s);
        dis[s] = 1;
        while(q.size()) {
            int u = q.front();
            q.pop();
            for(int i=head[u];~i;i=e[i].nxt) {
                if(e[i].f && !dis[e[i].v]) {
                    int v = e[i].v;
                    dis[v] = dis[u] + 1;
                    if(v == t) return true;
                    q.push(v);
                }
            }
        }
        return false;
    }

    T dfs(int u, T m) {
        if(u == t) return m;
        T flow = 0;
        for(int i=cur[u];~i;cur[u]=i=e[i].nxt) {
            if(e[i].f && dis[e[i].v] == dis[u] + 1) {
                T f = dfs(e[i].v,min(m,e[i].f));
                e[i].f -= f;
                e[i^1].f += f;
                m -= f;
                flow += f;
                if(!m) break;
            }
        }
        if(!flow) dis[u] = -1;
        return flow;
    }

    T dinic() {
        T flow = 0;
        while(bfs()) flow += dfs(s,numeric_limits<T>::max());
        return flow;
    }

    void init(int s_,int t_,int vtot_) {
        s = s_, t = t_, vtot = vtot_;
        etot = 0;
        fore(i,1,vtot) head[i] = -1;
    }
};
```