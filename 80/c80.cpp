#pragma GCC optimize("Ofast") // make code go fast stuff
#pragma GCC target("avx,avx2,fma") // make code go fast stuff
#include <bits/stdc++.h>

#define x first
#define y second
using namespace std;

int points; // total number of vertices for each testcase
int intersectCountA; // number of times the ray segment of one point of polygon A intersects polygon B for each testcase
int intersectCountB; // number of times the ray segment of one point of polygon B intersects polygon A for each testcase
string input; // string to temporarily store user input
pair < int, int > pointExtendedA, pointExtendedB; // To store the ending point of ray segment of polygons A and B resp for each testcase

int ccw(pair < int, int > A, pair < int, int > B, pair < int, int > C) {
    return (C.y - A.y) * (B.x - A.x) >= (B.y - A.y) * (C.x - A.x);
    // If slope of line AB is less than the slope of line AC, i.e, if points are in counter clockwise orientation
}

bool isIntersecting(pair < int, int > A, pair < int, int > B, pair < int, int > C, pair < int, int > D) {
    return (ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D));
    /*
    Segment AB intersects segment CD if ACD and BCD have opposite orientation, and ABC and ABD have opposite orientation
    i.e ACD and BCD both can't be clockwise or counter clockwise, similarly for ABC and ABD
    If not, then the lines are not intersecting
    */
}

string testCase() {
    cin >> points;
    vector < pair < int, int >> aVertices(points), bVertices(points);

    // 35-47: Parsing input

    for (int i = 0; i < points; i++) {
        cin >> input;
        const int commaAt = input.find(",");
        aVertices[i].x = stoi(input.substr(0, commaAt));
        aVertices[i].y = stoi(input.substr(commaAt + 1));
    }
    // just finding position of comma and splitting the string at that position to get the x and y values
    for (int i = 0; i < points; i++) {
        cin >> input;
        const int commaAt = input.find(",");
        bVertices[i].x = stoi(input.substr(0, commaAt));
        bVertices[i].y = stoi(input.substr(commaAt + 1));
    }

    // 51-69: Check for intersections and return accordingly

    for (int i = 0; i < points; i++) {
        intersectCountA = 0;
        intersectCountB = 0;
        pointExtendedA = make_pair(aVertices[i].x + 1400, aVertices[i].y);
        pointExtendedB = make_pair(bVertices[i].x + 1400, bVertices[i].y); // 1400 unit long segment
        for (int j = 0; j < points; j++) {
            // Checks if edge of polygon A is intersecting with edge of polygon B
            // this checks for all edges (e*e)
            // as current edge intersection algorithm fails for colinear edges, all points in both polygon are checked if they are inside another polygon
            // this also checks if a polygon is inside another polygon, when no edges intersect
            if (isIntersecting(aVertices[i], aVertices[(i + 1) % points], bVertices[j], bVertices[(j + 1) % points])) return "true";
            if (isIntersecting(aVertices[i], pointExtendedA, bVertices[j], bVertices[(j + 1) % points])) intersectCountA++; // if polygon A point is inside B
            if (isIntersecting(bVertices[i], pointExtendedB, aVertices[j], aVertices[(j + 1) % points])) intersectCountB++; // if polygon B point is inside A
        }
        // If the number of intersections is odd, one of the point of a polygon is inside the other polygon, thus, collision.
        if (intersectCountA % 2 == 1 or intersectCountB % 2 == 1) return "true";
    }

    return "false"; // No edges intersect, and neither of the polygons are inside each other. Thus, no collision.
}

int main() {
    ios_base::sync_with_stdio(false); // make code go fast stuff
    cin.tie(nullptr); // make code go fast stuff
    int t;
    cin >> t;
    while (t--) cout << testCase() << "\n";
    return 0;
}
