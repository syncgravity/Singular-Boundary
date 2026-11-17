#include <bits/stdc++.h>
using namespace std;

struct Tarjan {
    int n, timer=0, cc=0;
    const vector<vector<int>>& adj;
    const vector<char>& banned;
    vector<int> idx, low, st, comp;
    vector<char> on;
    vector<vector<int>> members;
    Tarjan(const vector<vector<int>>& a, const vector<char>& b)
      : n((int)a.size()), adj(a), banned(b), idx(n,-1), low(n), comp(n,-1), on(n,0) {}
    void dfs(int v) {
        idx[v]=low[v]=timer++;
        st.push_back(v); on[v]=1;
        for(int w:adj[v]) {
            if(banned[w]) continue;
            if(idx[w]<0) { dfs(w); low[v]=min(low[v],low[w]); }
            else if(on[w]) low[v]=min(low[v],idx[w]);
        }
        if(low[v]==idx[v]) {
            members.emplace_back();
            while(true) {
                int w=st.back(); st.pop_back(); on[w]=0;
                comp[w]=cc; members.back().push_back(w);
                if(w==v) break;
            }
            ++cc;
        }
    }
    void run() {
        for(int v=0;v<n;v++) if(!banned[v] && idx[v]<0) dfs(v);
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n,m,f;
    if(!(cin>>n>>m>>f)) return 2;
    vector<vector<int>> adj(n), freeAdj(n);
    for(int i=0;i<m;i++){ int u,v; cin>>u>>v; adj[u].push_back(v); }
    for(int u=0;u<n;u++) {
        int q; cin>>q;
        while(q--){ int t; cin>>t; freeAdj[u].push_back(t); }
    }
    vector<char> banned(n,0);
    vector<int> mark(f,0);
    int stamp=0;
    long long tested=0, sinkComponents=0;
    long long minimumSinkSlack=LLONG_MAX, minimumCount=0;
    int bestB1=-1, bestB2=-1, bestFree=0, bestBoundary=0;
    vector<int> bestSources;
    map<int,long long> slackHistogram;
    auto inspect = [&](int b1, int b2)->bool {
        fill(banned.begin(),banned.end(),0);
        if(b1>=0) banned[b1]=1;
        if(b2>=0) banned[b2]=1;
        ++tested;
        Tarjan tr(adj,banned); tr.run();
        vector<char> sink(tr.cc,1);
        vector<int> boundary(tr.cc,0);
        for(int u=0;u<n;u++) if(!banned[u]) {
            int c=tr.comp[u];
            for(int v:adj[u]) {
                if(banned[v]) {
                    if(v==b1) boundary[c] |= 1;
                    if(v==b2) boundary[c] |= 2;
                } else if(tr.comp[v]!=c) {
                    sink[c]=0;
                }
            }
        }
        for(int c=0;c<tr.cc;c++) if(sink[c]) {
            ++stamp;
            int freeCount=0;
            for(int u:tr.members[c]) for(int t:freeAdj[u]) {
                if(mark[t]!=stamp) { mark[t]=stamp; ++freeCount; }
            }
            int bcount=__builtin_popcount((unsigned)boundary[c]);
            int slack=freeCount+bcount;
            ++sinkComponents;
            ++slackHistogram[slack];
            if(slack<minimumSinkSlack) {
                minimumSinkSlack=slack; minimumCount=1;
                bestB1=b1; bestB2=b2; bestFree=freeCount;
                bestBoundary=bcount; bestSources=tr.members[c];
            } else if(slack==minimumSinkSlack) {
                ++minimumCount;
            }
            if(slack<=2) {
                cout << "LOW_SLACK_WITNESS slack=" << slack
                     << " banned=(" << b1 << "," << b2 << ")"
                     << " boundary_count=" << bcount
                     << " free_target_count=" << freeCount
                     << " source_count=" << tr.members[c].size() << "\n";
                cout << "sources";
                for(int u:tr.members[c]) cout << " " << u;
                cout << "\nboundary";
                if(boundary[c]&1) cout << " " << b1;
                if(boundary[c]&2) cout << " " << b2;
                cout << "\n";
                return true;
            }
        }
        return false;
    };

    if(inspect(-1,-1)) return 0;
    for(int a=0;a<n;a++) if(inspect(a,-1)) return 0;
    for(int a=0;a<n;a++) for(int b=a+1;b<n;b++)
        if(inspect(a,b)) return 0;
    cout << "NO_BOUNDARY_AT_MOST_2"
         << " n=" << n << " arcs=" << m << " free_targets=" << f
         << " banned_sets_tested=" << tested << "\n";
    cout << "sink_components_examined=" << sinkComponents
         << " minimum_sink_slack=" << minimumSinkSlack
         << " minimizers=" << minimumCount << "\n";
    cout << "minimum_witness_banned=(" << bestB1 << "," << bestB2 << ")"
         << " boundary_count=" << bestBoundary
         << " free_target_count=" << bestFree
         << " source_count=" << bestSources.size() << "\nsources";
    for(int u:bestSources) cout << " " << u;
    cout << "\nslack_histogram";
    for(auto [s,c]:slackHistogram) cout << " " << s << ":" << c;
    cout << "\nTherefore every nonempty source subset A has Hall slack >= 3.\n";
    return 0;
}
