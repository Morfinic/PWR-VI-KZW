#ifndef LAB1_PROCES_H
#define LAB1_PROCES_H


class Proces {
    int R{}, P{}, Q{};
public:
    Proces();
    Proces(int R, int P, int Q);
    [[nodiscard]] int getR() const, getP() const, getQ() const;
    void setR(int num);
    void setP(int num);
    void setQ(int num);

};


#endif //LAB1_PROCES_H
