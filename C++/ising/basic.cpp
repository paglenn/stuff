#include<iostream>
#include"TProfile.h"
#include"TFile.h"
#include"methods.h"
#include "Lattice.h"


using namespace std; 

double T = 1.0; 
//double T = 2.269; 
//double T = 4.0; 
int L = 20; 
double h = 1.0; 
double J = 1.0; 

int numSweeps = 1e4; 
int numSteps = L*L*numSweeps; 
int sampleRate = L*L;// numSteps/1000; 

// ROOT histograms (for collecting statistics) 
TProfile * en_ts ; 
TProfile * mag_ts ; 
TProfile * corr; 
TH1 * en; 
TH1 * mag; 
TFile * dataFile = new TFile("basic_data.root", "update"); 

// these functions vary depend on what you are trying to measure! 
void createHistograms();
void WriteEventData(Lattice * system, int step) ;  
void WriteHistograms(); 
int close(); 

int main() { 
	double num_acc = 0; 
	int acc; 

	createHistograms();
	
	// usage: Lattice ( box length, temp, coupling = 1., field = 0.0)  
	Lattice * system = new Lattice(L,T,J,h) ; 
	//cout << "m: "<< system->GetM() << endl ; 
	//exit(1); 

	for(int step = 0; step < numSteps; step ++)  { 

		acc = mc_step(system);
		num_acc += acc/numSteps; 
		//cout<<system->GetM() << endl; 
		if ( step%sampleRate == 0 ) WriteEventData(system,step);
	}
	WriteHistograms(); 
	
	cout << " final magnetization: " << system->GetM() << endl ; 
	return close(); // close() returns 0  
}

void createHistograms() {
	// initialization of histograms 
	double beta = 1./T; 
	char name[15];
	sprintf(name,"en_ts_%.3f",T); 
	en_ts = new TProfile(name,name, numSweeps, 0, numSweeps);
	en_ts->SetBit(TH1::kCanRebin); 

	en = new TH1D("en", "en", L*L, -beta, beta); 
	en ->SetBit(TH1::kCanRebin); 
	
	sprintf(name,"mag_ts_%.3f",T); 
	mag_ts = new TProfile(name,name, numSweeps, 0, numSweeps, -1, 1);
	mag_ts->SetBit(TH1::kCanRebin); 

	sprintf(name,"corr_%.3f",T); 
	corr = new TProfile(name,name, L/2, 0, L/2) ;
	corr->SetBit(TH1::kCanRebin); 
	
	mag = new TH1D("mag", "mag", L*L/2, -1, 1); 
	//mag ->SetBit(TH1::kCanRebin); 
}

	
void WriteEventData(Lattice * system, int step) { 
	//cout<< system->GetE() << endl;
	en->Fill(system->GetE()) ; 
	en_ts->Fill(step/(L*L) , en->GetMean() ) ; 
	mag->Fill(system->GetM()); 
	mag_ts->Fill(step/(L*L) , mag->GetMean() ) ;
	double m = mag->GetMean(); 

	int r_max = L/2; 
	for(int i = 0; i < L*L ; i++) { 
		
		int s_i = system->GetSite(i) ; 

		for (int j = 0; j < r_max; j++) { 

			
			// walk down row 
			int s_j = system->GetSite((i+j)%L); 
			corr->Fill(j, (s_i - m) * (s_j - m) ) ; 
			
			// walk down column
			int s_k = system->GetSite((i+j*L)%(L*L)); 
			corr->Fill(j, (s_i - m) * (s_k - m) ) ; 

		}
	}

	//cout<<step/sampleRate<<endl;
	//cout<<energy->GetEntries() << endl; 
}

void WriteHistograms() {
	en->Write(); 
	en_ts->Write();
	mag_ts->Write();
	mag->Write(); 
	corr->Write(); 
}

int close() {
	dataFile->Close();
	return 0; 
}







//int RunSimulation(int numsteps); 
