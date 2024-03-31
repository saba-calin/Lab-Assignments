#ifndef A2_3_916_SABAILA_CALIN_VECTOR_H
#define A2_3_916_SABAILA_CALIN_VECTOR_H

#include "domain.h"

typedef struct
{
    void **elem;
    int size, capacity;
} Vector;

Vector *CreateVector();
void EraseVector(Vector *v);
void ResizeVector(Vector *v);
void PushBack(Vector *v, void *medicine);
void DeleteAtPosition(Vector *v, int pos);
int Size(Vector *v);
int Capacity(Vector *v);

#endif //A2_3_916_SABAILA_CALIN_VECTOR_H
