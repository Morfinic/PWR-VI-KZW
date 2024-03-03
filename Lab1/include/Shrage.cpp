#include <iostream>
#include <vector>
#include "Proces.h"

int findSmallestR(const std::vector<Proces>& tab){
    Proces tmp(99999, 0, 0);

    for(auto proces: tab){
        if(proces.getR() < tmp.getR())
            tmp = proces;
    }

    return tmp.getR();
}

int findSmallestRidx(const std::vector<Proces>& tab){
    Proces tmp(99999, 0, 0);
    int i{0}, tmpIdx{0};

    for(auto proces: tab){
        if(proces.getR() < tmp.getR())
            tmpIdx = i;
        i++;
    }

    return tmpIdx;
}

int findBiggestQidx(const std::vector<Proces>& tab){
    Proces tmp(0, 0, 0);
    int i{0}, tmpIdx{0};

    for(auto proces: tab){
        if(proces.getQ() > tmp.getQ())
            tmpIdx = i;
        i++;
    }

    return tmpIdx;
}

int Shrage(std::vector<Proces> tab){
    std::vector<Proces> schrageNieuszeregowany = tab;
    std::vector<Proces> schrageGotowe;
    int t{0}, cmax{0};

    while(!schrageGotowe.empty() || !schrageNieuszeregowany.empty()){
        while(!schrageNieuszeregowany.empty() && findSmallestR(schrageNieuszeregowany) <= t){
            int i = findSmallestRidx(schrageNieuszeregowany);
            schrageGotowe.emplace_back(schrageNieuszeregowany[i]);
            schrageNieuszeregowany.erase(schrageNieuszeregowany.begin() + i);
        }
        if(schrageGotowe.empty())
            t = findSmallestR(schrageNieuszeregowany);
        else{
            int i = findBiggestQidx(schrageGotowe);
            auto j = schrageGotowe[i];
            schrageGotowe.erase(schrageGotowe.begin() + i);
            t += j.getP();
            cmax = std::max(cmax, t + j.getQ());
        }
    }

    std::cout<<"\nCmax: "<<cmax;
    return cmax;
}
