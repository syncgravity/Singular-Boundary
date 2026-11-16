// Exact n=10 cut-load ceiling-class regression for the interval Hall coupling.
// Enumerates all connected perfect matchings on 10 ports and all labeled trees
// that can possibly be neighbors (the two endpoint vertices must be leaves).
// Standard-library-only; compile with: c++ -O3 -std=c++17 file.cpp -o verifier
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>

using namespace std;
constexpr int N = 10;
constexpr int S = N / 2;
using Load = array<int, N - 1>;

long long bareiss_det(vector<vector<long long>> a) {
    const int n = (int)a.size();
    if (n == 0) return 1;
    long long sign = 1, previous = 1;
    for (int k = 0; k < n - 1; ++k) {
        if (a[k][k] == 0) {
            int pivot_row = k + 1;
            while (pivot_row < n && a[pivot_row][k] == 0) ++pivot_row;
            if (pivot_row == n) return 0;
            swap(a[k], a[pivot_row]);
            sign = -sign;
        }
        const long long pivot = a[k][k];
        for (int i = k + 1; i < n; ++i) {
            for (int j = k + 1; j < n; ++j) {
                const long long numerator =
                    a[i][j] * pivot - a[i][k] * a[k][j];
                assert(numerator % previous == 0);
                a[i][j] = numerator / previous;
            }
        }
        for (int i = k + 1; i < n; ++i) a[i][k] = 0;
        previous = pivot;
    }
    return sign * a[n - 1][n - 1];
}

long long spanning_tree_count(int vertices,
                              const vector<pair<int, int>>& edges) {
    if (vertices == 1) return 1;
    vector<vector<long long>> lap(vertices, vector<long long>(vertices, 0));
    for (auto [u, v] : edges) {
        ++lap[u][u]; ++lap[v][v];
        --lap[u][v]; --lap[v][u];
    }
    vector<vector<long long>> cofactor(vertices - 1,
                                       vector<long long>(vertices - 1));
    for (int i = 0; i < vertices - 1; ++i)
        for (int j = 0; j < vertices - 1; ++j)
            cofactor[i][j] = lap[i][j];
    return bareiss_det(cofactor);
}

map<Load, long long> left_mass;
long long connected_matchings = 0;
vector<pair<int, int>> matching_pairs;

void record_matching() {
    vector<pair<int, int>> intervals = matching_pairs;
    const int s = (int)intervals.size();
    vector<pair<int, int>> overlap_edges;
    for (int i = 0; i < s; ++i) {
        for (int j = i + 1; j < s; ++j) {
            if (max(intervals[i].first, intervals[j].first) <
                min(intervals[i].second, intervals[j].second)) {
                overlap_edges.emplace_back(i, j);
            }
        }
    }
    const long long tau = spanning_tree_count(s, overlap_edges);
    if (tau == 0) return;
    ++connected_matchings;
    Load h{};
    for (auto [a, b] : intervals)
        for (int k = a; k < b; ++k) ++h[k];
    left_mass[h] += tau;
}

void enumerate_matchings(vector<int> remaining) {
    if (remaining.empty()) {
        record_matching();
        return;
    }
    const int a = remaining.front();
    for (int j = 1; j < (int)remaining.size(); ++j) {
        const int b = remaining[j];
        vector<int> next;
        next.reserve(remaining.size() - 2);
        for (int k = 1; k < (int)remaining.size(); ++k)
            if (k != j) next.push_back(remaining[k]);
        matching_pairs.emplace_back(a, b);
        enumerate_matchings(next);
        matching_pairs.pop_back();
    }
}

vector<Load> primitive_paths;
Load current_path{};

void generate_primitive_paths(int pos, int height) {
    if (pos == N - 1) {
        if (height == 1) {
            bool positive = true;
            for (int k = 0; k < N - 1; ++k)
                if (current_path[k] <= 0) positive = false;
            if (positive) primitive_paths.push_back(current_path);
        }
        return;
    }
    current_path[pos] = height + 1;
    generate_primitive_paths(pos + 1, height + 1);
    if (height > 0) {
        current_path[pos] = height - 1;
        generate_primitive_paths(pos + 1, height - 1);
    }
}

int find_path(const Load& h) {
    for (int i = 0; i < (int)primitive_paths.size(); ++i)
        if (primitive_paths[i] == h) return i;
    return -1;
}

vector<uint64_t> right_mass;
uint64_t feasible_trees = 0, excluded_trees = 0;

void enumerate_relevant_prufer_codes() {
    // c_1(T)<=1 and c_{N-1}(T)<=1 force vertices 0 and N-1 to be leaves.
    // Their labels therefore cannot occur in a Prüfer code. This enumerates
    // every potentially neighboring tree exactly once: (N-2)^(N-2)=8^8.
    constexpr int CODE_LEN = N - 2;
    constexpr int ALPHABET = N - 2;
    uint64_t total_codes = 1;
    for (int i = 0; i < CODE_LEN; ++i) total_codes *= ALPHABET;

    int code[CODE_LEN];
    for (uint64_t encoded = 0; encoded < total_codes; ++encoded) {
        uint64_t q = encoded;
        int degree[N];
        for (int i = 0; i < N; ++i) degree[i] = 1;
        for (int i = 0; i < CODE_LEN; ++i) {
            code[i] = 1 + (int)(q % ALPHABET);
            q /= ALPHABET;
            ++degree[code[i]];
        }

        pair<int, int> edges[N - 1];
        for (int i = 0; i < CODE_LEN; ++i) {
            int leaf = 0;
            while (leaf < N && degree[leaf] != 1) ++leaf;
            assert(leaf < N);
            const int v = code[i];
            edges[i] = {leaf, v};
            --degree[leaf];
            --degree[v];
        }
        int last_a = -1, last_b = -1;
        for (int i = 0; i < N; ++i) {
            if (degree[i] == 1) {
                if (last_a < 0) last_a = i;
                else last_b = i;
            }
        }
        assert(last_a >= 0 && last_b >= 0);
        edges[N - 2] = {last_a, last_b};

        Load c{};
        for (auto [u0, v0] : edges) {
            const int u = min(u0, v0), v = max(u0, v0);
            for (int k = u; k < v; ++k) ++c[k];
        }

        // The maximal primitive Dyck path is (1,2,...,5,...,2,1).
        // Every tree outside these cut caps has no left neighbor.
        const int max_height[N - 1] = {1, 2, 3, 4, 5, 4, 3, 2, 1};
        bool potentially_relevant = true;
        for (int k = 0; k < N - 1; ++k)
            if (c[k] > max_height[k]) potentially_relevant = false;
        if (!potentially_relevant) {
            ++excluded_trees;
            continue;
        }
        ++feasible_trees;

        // Meet all primitive majorants of c. Closure under coordinatewise
        // minimum guarantees that this meet is itself a primitive path.
        bool found = false;
        Load ceiling{};
        for (const Load& h : primitive_paths) {
            bool dominates = true;
            for (int k = 0; k < N - 1; ++k)
                if (c[k] > h[k]) dominates = false;
            if (!dominates) continue;
            if (!found) {
                ceiling = h;
                found = true;
            } else {
                for (int k = 0; k < N - 1; ++k)
                    ceiling[k] = min(ceiling[k], h[k]);
            }
        }
        assert(found);
        const int index = find_path(ceiling);
        assert(index >= 0);
        ++right_mass[index];
    }
    assert(feasible_trees + excluded_trees == total_codes);
}

int main() {
    vector<int> ports(N);
    for (int i = 0; i < N; ++i) ports[i] = i;
    enumerate_matchings(ports);
    generate_primitive_paths(0, 0);
    sort(primitive_paths.begin(), primitive_paths.end());
    assert(primitive_paths.size() == 14);
    right_mass.assign(primitive_paths.size(), 0);
    enumerate_relevant_prufer_codes();

    long long left_total = 0;
    uint64_t right_total = 0;
    for (const auto& [h, count] : left_mass) left_total += count;
    for (uint64_t count : right_mass) right_total += count;
    assert(left_mass.size() == primitive_paths.size());
    assert(connected_matchings == 706);
    assert(left_total == 31744);
    assert(feasible_trees == 442979);
    assert(excluded_trees == 16334237);

    cout << "PASS n=10 primitive-Dyck ceiling-class regression\n";
    cout << "connected_matchings=" << connected_matchings
         << " primitive_paths=" << primitive_paths.size()
         << " left_copies=" << left_total
         << " relevant_trees=" << right_total
         << " excluded_trees=" << excluded_trees << "\n";
    for (int i = 0; i < (int)primitive_paths.size(); ++i) {
        const long long demand = left_mass.at(primitive_paths[i]);
        const uint64_t supply = right_mass[i];
        assert(supply >= (uint64_t)demand);
        for (int k = 0; k < N - 1; ++k)
            cout << primitive_paths[i][k] << (k + 1 == N - 1 ? ':' : ',');
        cout << "L=" << demand << " Q=" << supply << "\n";
    }
    cout << "PASS pointwise Q(h)>=L(h) for all 14 primitive Dyck paths at n=10\n";
}
