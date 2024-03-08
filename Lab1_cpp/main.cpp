#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include "include/Proces.h"
#include "include/Shrage.h"
using namespace std;

vector<Proces> readFile(const string& fileName){
    ifstream inputFile(fileName, ios::in);
    string tmp;
    int i{0};

    getline(inputFile, tmp);
    vector<Proces> tmpTab;

    if(inputFile.is_open()){
        cout<<"\nOtwarto plik: "<<fileName;
        while(getline(inputFile, tmp)){
            tmpTab.emplace_back();
            tmpTab[i].setR(stoi(tmp.substr(0, tmp.find(' '))));
            tmpTab[i].setP(stoi(tmp.substr(tmp.find(' '), tmp.find_last_of(' '))));
            tmpTab[i].setQ(stoi(tmp.substr(tmp.find_last_of(' '), tmp.length())));
            i++;
        }
    } else{
        cout<<"Plik nieotwarty\n";
    }

    inputFile.close();

    return tmpTab;
}

int main(){
    auto start = chrono::high_resolution_clock::now();
    int cMaxSum{0};

    string pathToData{"../Dane/SubDane/"};
//    string dataTab[1] = {"data.1"};
    string dataTab[4] = {"data.1", "data.2", "data.3", "data.4"};

    for(const string& file: dataTab){
        auto procesTab = readFile(pathToData + file);
        cMaxSum += Shrage(procesTab);
    }

    auto end = chrono::high_resolution_clock::now();
    auto elapsed = chrono::duration_cast<chrono::nanoseconds>(end - start);
    cout<<"\n\nCmax sum: "<<cMaxSum<<"\n";
    cout<<"Czas dzialania: "<<elapsed.count() / 1e6<<"ms\n";

    return 0;
}