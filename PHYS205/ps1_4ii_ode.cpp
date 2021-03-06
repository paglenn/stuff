#include<cmath>
#include<iostream>
#include<iomanip>
#include<string>
#include<fstream>
using namespace std; 

int main() { 

	double t; 
	double x_t = 2.0 ; 
	double y_t = 0.0 ; 

	double dt = 5e-4 ; 
	double _dt = 1./dt ; 
	double eps = 0.5 ; 
	double PI = acos(-1) ; 
	double tmax = 10*PI;

	const int nsteps = ceil( tmax / dt) ; 
	double x[nsteps+1], y[nsteps+1] ; 
	x[0] = x_t; y[0] = y_t ; 

	for(int i = 0 ; i < nsteps ; i++) {
		x[i+1] = x[i] + dt * y[i] ; 
		y[i+1] = y[i] - dt *( (eps/3.) * y[i]*( y[i]*y[i] - 3.) + x[i]) ;
		
	}

	ofstream fout ;
	fout.open("output.dat") ;
	for(int i = 0; i < nsteps; i++ ) {
		t = i * dt ; 
		fout << t ;
		fout << setw(14) << x[i] ; 
		fout << setw(14) << y[i] ; 
		fout << endl ; 


		if (fabs(x[i]-x[0]) < 0.5*dt && i > 0) cout << "period: "<< t << endl ; 
	}
	fout.close(); 



}

