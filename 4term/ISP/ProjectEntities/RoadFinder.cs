using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BLL
{
    public class RoadFinder
    {
        private List<List<int>> graph;
        private List<List<int>> roads;
        private bool[] visited;

        public RoadFinder()
        {
            graph = new List<List<int>>();
            roads = new List<List<int>>();
        }

        public List<List<Flight>> GetRoad(List<Flight> flights, int departingstat, int arrivalstat)
        {
            int i;
            List<List<Flight>> suitflight = new List<List<Flight>>();
            foreach (var flight in flights)
            {
                if (flight.DepartingPoint == arrivalstat)
                    continue;
                for (i = 0; i < graph.Count; i++)
                    if (graph[i][0] == flight.DepartingPoint)
                    {
                        int j;
                        for (j = 0; j < graph[i].Count; j++)
                            if (graph[i][j] == flight.ArrivalPoint)
                                break;
                        if (j == graph[i].Count)
                            graph[i].Add(flight.ArrivalPoint);
                        break;
                    }
                if (i == graph.Count)
                {
                    graph.Add(new List<int>());
                    graph[i].Add(flight.DepartingPoint);
                    graph[i].Add(flight.ArrivalPoint);
                }
            }
            visited = new bool[graph.Count];
            RoadTraveler(0, 0);
            for (int j = 0; j < roads.Count; j++)
            {
                suitflight.Add(new List<Flight>());
                for (int k = 0; k < roads[j].Count - 1; k++)
                    suitflight[j].Add(flights.First(x => x.DepartingPoint == roads[j][k] && x.ArrivalPoint == roads[j][k + 1]));
            }
            return suitflight;
        }

        private void RoadTraveler(int ind, int j)
        {
            if (visited[ind] == false)
            {
                visited[ind] = true;
                for (int i = 1; i < graph[ind].Count; i++)
                {
                    roads[j].Add(graph[ind][i]);
                    RoadTraveler(graph.FindIndex(x => x[0] == graph[ind][i]), j + i - 1);
                    roads.Add(new List<int>());
                    roads[roads.Count-1].Add(graph[ind][0]);
                }
            }
            visited[ind] = false;
        }
    }
}