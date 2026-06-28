
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#define K_TSP 2.609
typedef struct { int* route; double distance; } TSPResult;
static void two_opt(const double* dist, int* route, int n, double* length) {
    int improved = 1;
    while (improved) {
        improved = 0;
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                double new_length = *length - dist[route[i-1] * n + route[i]] - dist[route[j] * n + route[(j+1) % n]] + dist[route[i-1] * n + route[j]] + dist[route[i] * n + route[(j+1) % n]];
                if (new_length < *length - 1e-9) {
                    int left = i, right = j;
                    while (left < right) { int tmp = route[left]; route[left] = route[right]; route[right] = tmp; left++; right--; }
                    *length = new_length; improved = 1;
                }
            }
        }
    }
}
TSPResult hsag_solve_tsp(const double* dist, int n, int starts) {
    TSPResult result; result.route = (int*)malloc(n * sizeof(int)); result.distance = 1e18;
    int* current_route = (int*)malloc(n * sizeof(int)); int* visited = (int*)calloc(n, sizeof(int));
    for (int start = 0; start < starts && start < n; start++) {
        memset(visited, 0, n * sizeof(int)); current_route[0] = start; visited[start] = 1;
        double current_dist = 0.0; int current = start;
        for (int step = 1; step < n; step++) {
            int best_city = -1; double best_score = 1e18;
            for (int next_city = 0; next_city < n; next_city++) {
                if (!visited[next_city]) {
                    double f0 = dist[current * n + next_city]; double f1 = dist[next_city * n + start];
                    double score = f0 - K_TSP * (f1 / (f0 + 1e-9));
                    if (score < best_score) { best_score = score; best_city = next_city; }
                }
            }
            current_dist += dist[current * n + best_city]; visited[best_city] = 1; current_route[step] = best_city; current = best_city;
        }
        current_dist += dist[current * n + start];
        if (current_dist < result.distance) { result.distance = current_dist; memcpy(result.route, current_route, n * sizeof(int)); }
    }
    two_opt(dist, result.route, n, &result.distance); free(current_route); free(visited); return result;
}
static inline void cmp_swap_int(int32_t* d, int i, int j) { int32_t a = d[i], b = d[j]; d[i] = a < b ? a : b; d[j] = a < b ? b : a; }
void hsag_sort8_int(int32_t* d) {
    cmp_swap_int(d,0,1); cmp_swap_int(d,2,3); cmp_swap_int(d,4,5); cmp_swap_int(d,6,7);
    cmp_swap_int(d,0,2); cmp_swap_int(d,1,3); cmp_swap_int(d,4,6); cmp_swap_int(d,5,7);
    cmp_swap_int(d,1,2); cmp_swap_int(d,5,6); cmp_swap_int(d,0,4); cmp_swap_int(d,1,5);
    cmp_swap_int(d,2,6); cmp_swap_int(d,3,7); cmp_swap_int(d,2,4); cmp_swap_int(d,3,5);
    cmp_swap_int(d,1,2); cmp_swap_int(d,3,4); cmp_swap_int(d,5,6);
}
