#include <stdio.h>
#include <malloc.h>
#include <string.h>

#include "repository.h"
#include "vector.h"

// Function that creates a repository
// @param: none
// @return: a repository
Repository CreateRepository()
{
    Repository repo;
    repo.medicines = CreateVector();
    return repo;
}

// Function that adds a medicine to the repository
// @param *repo: a pointer to a repository
// @param medicine: a medicine
// @return: none
void AddMedicineRepository(Repository *repo, TElem medicine)
{
    TElem *temp = (TElem*) malloc(sizeof(TElem));
    *temp = medicine;
    PushBack(repo -> medicines, temp);
}

// Function that adds a quantity to a medicine at a given position
// @param *repo: a pointer to a repository
// @param q: an integer representing the quantity
// @param pos: an integer representing the position
// @return: none
void AddQuantityAtPositionRepository(Repository *repo, int q, int pos)
{
    TElem *elem = (TElem*) repo -> medicines -> elem[pos];
    elem -> quantity += q;
}

// Function that adds a price to a medicine at a given position
// @param *repo: a pointer to a repository
// @param p: an integer representing the price
// @param pos: an integer representing the position
// @return: none
void AddPriceAtPositionRepository(Repository *repo, int p, int pos)
{
    TElem *elem = (TElem*) repo -> medicines -> elem[pos];
    elem -> price += p;
}

// Function that returns a copy of the vector in the domain
// @param *repo: a pointer to a repository
// @return: a vector
Vector *GetMedicinesRepository(Repository *repo)
{
    Vector *v = CreateVector();  // return a copy of the vector in the domain
    for (int i = 0; i < Size(repo -> medicines); i++)
    {
        TElem *newElem = (TElem*) malloc(sizeof(TElem));
        TElem *elem = (TElem*) repo -> medicines -> elem[i];

        strcpy(newElem -> name, elem -> name);
        newElem -> concentration = elem -> concentration;
        newElem->quantity = elem -> quantity;
        newElem -> price = elem -> price;

        PushBack(v, newElem);
    }
    return v;
}

// Function that deletes a medicine at a given position
// @param *repo: a pointer to a repository
// @param pos: an integer representing the position
// @return: none
void DeleteAtPositionRepository(Repository *repo, int pos)
{
    DeleteAtPosition(repo -> medicines, pos);
}

// Function that sets the quantity of a medicine at a given position
// @param *repo: a pointer to a repository
// @param q: an integer representing the quantity
// @param pos: an integer representing the position
// @return: none
void SetQuantityAtPositionRepository(Repository *repo, int q, int pos)
{
    TElem *elem = (TElem*) repo -> medicines -> elem[pos];
    elem -> quantity = q;
}

// Function that sets the price of a medicine at a given position
// @param *repo: a pointer to a repository
// @param p: an integer representing the price
// @param pos: an integer representing the position
// @return: none
void SetPriceAtPosition(Repository *repo, int p, int pos)
{
    TElem *elem = (TElem*) repo -> medicines -> elem[pos];
    elem -> price = p;
}

// Function that updates the repository
// @param *repo: a pointer to a repository
// @param *v: a pointer to a vector
// @return: none
void UpdateRepository(Repository *repo, Vector *v)
{
    for (int i = 0; i < Size(repo -> medicines); i++)
    {
        free(repo -> medicines -> elem[i]);
    }
    repo -> medicines -> size = 0;

    for (int i = 0; i < Size(v); i++)
    {
        TElem *newElem = (TElem*) malloc(sizeof(TElem));
        TElem *elem = v -> elem[i];

        strcpy(newElem -> name, elem -> name);
        newElem -> concentration = elem -> concentration;
        newElem->quantity = elem -> quantity;
        newElem -> price = elem -> price;

        PushBack(repo -> medicines, newElem);
    }
}
