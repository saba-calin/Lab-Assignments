#ifndef A2_3_916_SABAILA_CALIN_DOMAIN_H
#define A2_3_916_SABAILA_CALIN_DOMAIN_H

typedef struct
{
    char name[50];
    int concentration, quantity, price;
} Medicine;

typedef Medicine TElem;


char *GetName(TElem *medicine);
int GetConcentration(TElem *medicine);
int GetQuantity(TElem *medicine);
int GetPrice(TElem *medicine);

void SetName(TElem *medicine, char *name);
void SetConcentration(TElem *medicine, int concentration);
void SetQuantity(TElem *medicine, int quantity);
void SetPrice(TElem *medicine, int price);

TElem CreateMedicine(char *name, int concentration, int quantity, int price);

#endif //A2_3_916_SABAILA_CALIN_DOMAIN_H
//