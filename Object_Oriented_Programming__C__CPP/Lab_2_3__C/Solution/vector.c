#include <stdio.h>
#include <malloc.h>

#include "repository.h"

// Function that creates a vector (initial capacity = 1)
// @param: none
// @return: a pointer to a vector
Vector *CreateVector()
{
    Vector *v = malloc(sizeof(Vector));
    if (v == NULL)
    {
        return NULL;
    }

    v -> capacity = 1;
    v -> size = 0;
    v -> elem = malloc(sizeof(void*));
    if (v -> elem == NULL)
    {
        return NULL;
    }

    return v;
}

// Function that erases a vector
// @param *v: a pointer to a vector
// @return: none
void EraseVector(Vector *v)
{
    if (v == NULL || v -> elem == NULL)
        return;

    for (int i = 0; i < Size(v); i++)
    {
        free(v -> elem[i]);
    }

    free(v -> elem);
    v -> elem = NULL;

    free(v);
    v = NULL;
}

// Function that resizes a vector (multiplicity factor = 2)
// @param *v: a pointer to a vector
// @return: none
void ResizeVector(Vector *v)
{
    if (v == NULL)
    {
        return;
    }

    v -> capacity *= 2;
    void **aux = realloc(v -> elem, (v -> capacity) * sizeof(void*));
    if (aux == NULL)
    {
        return;
    }

    v -> elem = aux;
}

// Function that pushes an element at the end of a vector
// @param *v: a pointer to a vector
// @param *medicine: a pointer to the element
// @return: none
void PushBack(Vector *v, void *medicine)
{
    if (v == NULL || v -> elem == NULL)
        return;

    if (v -> size == v -> capacity)
        ResizeVector(v);
    if (v == NULL)
        return;

    v -> elem[v -> size] = medicine;
    v -> size++;
}

// Function that deletes an element at a given position
// @param *v: a pointer to a vector
// @param pos: an integer representing the position
// @return: none
void DeleteAtPosition(Vector *v, int pos)
{
    if (v == NULL)
        return;
    if (pos < 0 || pos > Size(v) - 1)
    {
        return;
    }

    free(v -> elem[pos]);
    for (int i = pos; i < Size(v) - 1; i++)
    {
        v -> elem[i] = v -> elem[i + 1];
    }
    v -> size -= 1;
}

// Function that returns the size of a vector
// @param *v: a pointer to a vector
// @return: an integer
int Size(Vector *v)
{
    if (v == NULL)
        return 0;

    return v -> size;
}

// Function that returns the capacity of a vector
// @param *v: a pointer to a vector
// @return: an integer
int Capacity(Vector *v)
{
    if (v == NULL)
        return 0;

    return v -> capacity;
}
