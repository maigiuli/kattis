#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <queue>

using namespace std;

int main()
{
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> tunnels(n - 1, vector<int>(2));
    for (int i = 0; i < n - 1; i++)
    {
        cin >> tunnels[i][0] >> tunnels[i][1];
    }

    vector<vector<int>> racers(m, vector<int>(2));
    for (int i = 0; i < m; i++)
    {
        cin >> racers[i][0] >> racers[i][1];
    }

    int end_checkpoint;
    cin >> end_checkpoint;

    int c;
    cin >> c;

    vector<int> specials(c);
    for (int i = 0; i < c; i++)
    {
        cin >> specials[i];
    }

    vector<vector<int>> adj(n); 

    for (auto &t : tunnels)
    {
        int u = t[0] - 1;
        int v = t[1] - 1;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> dist(n, -1);
    queue<int> q;
    dist[end_checkpoint - 1] = 0;
    q.push(end_checkpoint - 1);

    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (int v : adj[u])
        { // solo vicini
            if (dist[v] == -1)
            {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    sort(specials.begin(), specials.end(), [&](int x, int y)
         { return dist[x] > dist[y]; });

    vector<int> passed_special(specials.size(), 0);

    vector<double> speeds;
    for (auto &racer : racers)
    {
        speeds.push_back(1.0 / racer[1]);
    }

    vector<vector<int>> passing_per_special;

    for (auto special : specials)
    {
        vector<pair<double, int>> arrivals;

        for (int r_index = 0; r_index < m; r_index++)
        {
            int start = racers[r_index][0];
            double speed = 1.0 / racers[r_index][1];

            if (dist[special - 1] < dist[start - 1])
            {
                arrivals.emplace_back(speed, r_index);
            }
        }

        sort(arrivals.rbegin(), arrivals.rend());

        vector<int> passing;
        for (int i = 0; i < (int)arrivals.size() && i < k; i++)
        {
            passing.push_back(arrivals[i].second);
        }

        passing_per_special.push_back(passing);
    }

    vector<int> times;

    for (int j = 0; j < m; j++)
    {
        bool eliminated = false;
        for (int i = 0; i < (int)specials.size(); i++)
        {
            if (dist[specials[i] - 1] < dist[racers[j][0] - 1])
            {
                if (find(passing_per_special[i].begin(), passing_per_special[i].end(), j) == passing_per_special[i].end())
                {
                    eliminated = true;
                    break;
                }
            }
        }
        if (eliminated)
        {
            times.push_back(-1);
        }
        else
        {
            times.push_back(racers[j][1] * dist[racers[j][0] - 1]);
        }
    }

    cout << "[";
    for (size_t i = 0; i < times.size(); i++)
    {
        cout << times[i];
        if (i != times.size() - 1)
            cout << ", ";
    }
    cout << "]" << endl;

    return 0;
}