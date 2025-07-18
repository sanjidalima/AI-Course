#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

// Objective function to maximize: f(x) = -x^2 + 4x
double objective_function(double x)
{
    return -pow(x, 2) + 4 * x;
}

// Hill Climbing algorithm
// start: initial point
// step_size: amount to move in each iteration
// max_iter: maximum iterations allowed
double hill_climbing(double start, double step_size, int max_iter)
{
    double current = start;
    double current_val = objective_function(current);

    for (int i = 0; i < max_iter; i++)
    {
        // Explore neighbor in positive step direction
        double neighbor = current + step_size;
        double neighbor_val = objective_function(neighbor);

        if (neighbor_val > current_val)
        {
            // Move to neighbor if it improves objective
            current = neighbor;
            current_val = neighbor_val;
        }
        else
        {
            // Otherwise explore neighbor in negative step direction
            neighbor = current - step_size;
            neighbor_val = objective_function(neighbor);

            if (neighbor_val > current_val)
            {
                current = neighbor;
                current_val = neighbor_val;
            }
            else
            {
                // Neither neighbor improves, so local maximum reached; stop
                break;
            }
        }
    }

    return current;
}

int main()
{
    double start, step_size;
    int max_iter;

    cout << "Enter starting point: ";
    cin >> start;

    cout << "Enter step size: ";
    cin >> step_size;

    cout << "Enter maximum iterations: ";
    cin >> max_iter;

    double solution = hill_climbing(start, step_size, max_iter);

    cout << "Hill Climbing Solution: x = " << solution
         << ", f(x) = " << objective_function(solution) << endl;

    return 0;
}
