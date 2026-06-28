
import numpy as np
K_TSP, K_SCHEDULING, K_SET_COVER, K_KNAPSACK, K_CVRP, K_COLORING = 2.609, 2.609, 0.8, 1.2, 1.8, 2.2

class HSAG:
    def solve_tsp(self, dist_matrix, starts=5):
        n = len(dist_matrix); best_route, best_length = None, float('inf')
        for start in range(min(starts, n)):
            visited, route, total_dist, current = [False]*n, [start], 0.0, start
            visited[start] = True
            for _ in range(n - 1):
                best_city, best_score = -1, float('inf')
                for nc in range(n):
                    if not visited[nc]:
                        f0, f1 = dist_matrix[current][nc], dist_matrix[nc][start]
                        score = f0 - K_TSP * (f1 / (f0 + 1e-9))
                        if score < best_score: best_score, best_city = score, nc
                total_dist += dist_matrix[current][best_city]; visited[best_city] = True
                route.append(best_city); current = best_city
            total_dist += dist_matrix[current][start]
            if total_dist < best_length: best_length, best_route = total_dist, route[:]
        improved = True
        while improved:
            improved = False
            for i in range(1, len(best_route)-1):
                for j in range(i+1, len(best_route)):
                    nr = best_route[:i] + best_route[i:j+1][::-1] + best_route[j+1:]
                    nl = sum(dist_matrix[nr[k]][nr[k+1]] for k in range(len(nr)-1)) + dist_matrix[nr[-1]][nr[0]]
                    if nl < best_length: best_route, best_length, improved = nr, nl, True
        return best_route, best_length

    def solve_scheduling(self, jobs, machines):
        schedule, machine_load = [[] for _ in range(machines)], [0.0]*machines
        avg_load = sum(jobs) / machines
        for jid, pt in sorted(enumerate(jobs), key=lambda x: -x[1]):
            bm, bs = -1, float('inf')
            for m in range(machines):
                f0 = machine_load[m] + pt; f1 = abs(f0 - avg_load); f2 = max(max(machine_load), f0)
                score = f0 - K_SCHEDULING * (f1 / (f0 + 1e-9)) + 0.1 * f2
                if score < bs: bs, bm = score, m
            schedule[bm].append(jid); machine_load[bm] += pt
        return schedule, max(machine_load)

    def solve_knapsack(self, weights, values, capacity):
        n = len(weights); dp = [[0]*(capacity+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for w in range(capacity+1):
                if weights[i-1] <= w: dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
                else: dp[i][w] = dp[i-1][w]
        sel, w = [], capacity
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]: sel.append(i-1); w -= weights[i-1]
        return sel, dp[n][capacity], sum(weights[i] for i in sel)

    def solve_graph_coloring(self, adjacency, n):
        colors, order = [-1]*n, sorted(range(n), key=lambda x: -len(adjacency[x]))
        cc = 0
        for v in order:
            nc = set(colors[u] for u in adjacency[v] if colors[u] != -1)
            bc = 0
            while bc in nc: bc += 1
            colors[v] = bc
            if bc >= cc: cc = bc + 1
        return colors, cc
