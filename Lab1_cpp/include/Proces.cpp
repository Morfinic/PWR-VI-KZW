#include "Proces.h"

Proces::Proces() {}

Proces::Proces(int R, int P, int Q){
    this->R = R;
    this->P = P;
    this->Q = Q;
}

int Proces::getR() const{
    return this->R;
}

int Proces::getP() const{
    return this->P;
}

int Proces::getQ() const{
    return this->Q;
}

void Proces::setR(int num){
    this->R = num;
}

void Proces::setP(int num){
    this->P = num;
}

void Proces::setQ(int num){
    this->Q = num;
}
