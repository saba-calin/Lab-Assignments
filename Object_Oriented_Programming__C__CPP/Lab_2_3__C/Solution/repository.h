#ifndef A2_3_916_SABAILA_CALIN_REPOSITORY_H
#define A2_3_916_SABAILA_CALIN_REPOSITORY_H

#include "domain.h"
#include "vector.h"

typedef struct
{
    Vector *medicines;
} Repository;

Repository CreateRepository();

Vector *GetMedicinesRepository(Repository *repo);
void AddQuantityAtPositionRepository(Repository *repo, int q, int pos);
void AddPriceAtPositionRepository(Repository *repo, int p, int pos);
void SetQuantityAtPositionRepository(Repository *repo, int q, int pos);
void SetPriceAtPosition(Repository *repo, int p, int pos);
void DeleteAtPositionRepository(Repository *repo, int pos);

void UpdateRepository(Repository *repo, Vector *v);

void AddMedicineRepository(Repository *repo, TElem medicine);

#endif //A2_3_916_SABAILA_CALIN_REPOSITORY_H
//