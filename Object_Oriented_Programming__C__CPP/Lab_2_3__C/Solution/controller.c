#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#include "controller.h"
#include "repository.h"

// Function that creates a controller
// @param: none
// @return: a controller
Controller CreateController()
{
    Controller controller;
    controller.repo = CreateRepository();
    return controller;
}

// Function that adds 10 medicines to the repository
// @param *controller: a pointer to a controller
// @return: none
void Add10Medicines(Controller *controller)
{
    AddMedicineRepository(&controller->repo, CreateMedicine("paracetamol", 1, 2, 3));
    AddMedicineRepository(&controller->repo, CreateMedicine("ibuprofen", 4, 5, 6));
    AddMedicineRepository(&controller->repo, CreateMedicine("aspirin", 7, 8, 9));
    AddMedicineRepository(&controller->repo, CreateMedicine("naproxen", 10, 11, 12));
    AddMedicineRepository(&controller->repo, CreateMedicine("diclofenac", 13, 14, 15));
    AddMedicineRepository(&controller->repo, CreateMedicine("codeine", 16, 17, 18));
    AddMedicineRepository(&controller->repo, CreateMedicine("meloxicam", 19, 20, 21));
    AddMedicineRepository(&controller->repo, CreateMedicine("methadone", 22, 23, 24));
    AddMedicineRepository(&controller->repo, CreateMedicine("tramadol", 25, 26, 27));
    AddMedicineRepository(&controller->repo, CreateMedicine("pethidine", 28, 29, 30));
}

// Function that returns a copy of the medicines vector from the repository
// @param *controller: a pointer to a controller
// @return: a copy of the medicines vector from the repository
Vector *GetMedicinesController(Controller *controller)
{
    return GetMedicinesRepository(&controller->repo);
}

// Function that checks if a string is a valid integer
// @param *c: a pointer to a string
// @return: true if the string is a valid integer, false otherwise
bool IsValidInt(char *c)
{
    for (int i = 0; i < strlen(c); i++)
    {
        if (c[i] < '0' || c[i] > '9')
        {
            return false;
        }
    }

    int x = atoi(c);
    if (x < 0)
        return false;

    return true;
}

// Function that adds a medicine to the repository if it doesn't exist, or updates its quantity if it does
// @param *controller: a pointer to a controller
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param command: a boolean that represents if the operation is a command or not
// @param *name: a pointer to a string
// @param *concentration: a pointer to a string
// @param *quantity: a pointer to a string
// @param *price: a pointer to a string
// @return: 1 if the quantity was updated, 2 if the medicine was added, -1 if the name is invalid, -2 if the concentration is invalid, -3 if the quantity is invalid, -4 if the price is invalid
int AddMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration, char *quantity, char *price)
{
    if (strlen(name) < 1)                    return -1;
    if (IsValidInt(concentration) == false)  return -2;
    if (IsValidInt(quantity) == false)       return -3;
    if (IsValidInt(price) == false)          return -4;

    int c = atoi(concentration);
    int q = atoi(quantity);
    int p = atoi(price);

    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strcmp(elem -> name, name) == 0 && elem -> concentration == c)
        {
            if (command == false)
                RecordUndoOperation(undoRedoController, GetMedicinesRepository(&controller->repo));
            else
                RecordUndoCommand(undoRedoCommand, "add_update", CreateMedicine(name, c, q, 0));

            AddQuantityAtPositionRepository(&controller->repo, q, i);
            EraseVector(v);
            return 1;  // update quantity
        }
    }
    EraseVector(v);

    if (command == false)
        RecordUndoOperation(undoRedoController, GetMedicinesRepository(&controller->repo));
    else
        RecordUndoCommand(undoRedoCommand, "add", CreateMedicine(name, c, q, p));

    AddMedicineRepository(&controller -> repo, CreateMedicine(name, c, q, p));
    return 2;  // add medicine
}

// Function that deletes a medicine from the repository
// @param *controller: a pointer to a controller
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param command: a boolean that represents if the operation is a command or not
// @param *name: a pointer to a string
// @param *concentration: a pointer to a string
// @return: 3 if the medicine was successfully deleted, -1 if the name is invalid, -2 if the concentration is invalid, -5 if the vector is empty, -6 if the medicine was not found
int DeleteMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration)
{
    if (strlen(name) < 1)  return -1;
    if (IsValidInt(concentration) == false)  return -2;

    Vector *v = GetMedicinesRepository(&controller->repo);
    if (Size(v) == 0)
        return -5;  // vector is empty

    int c = atoi(concentration);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strcmp(elem -> name, name) == 0 && elem -> concentration == c)
        {
            if (command == false)
                RecordUndoOperation(undoRedoController, GetMedicinesRepository(&controller->repo));
            else
                RecordUndoCommand(undoRedoCommand, "delete", CreateMedicine(elem -> name, elem -> concentration, elem -> quantity, elem -> price));

            DeleteAtPositionRepository(&controller->repo, i);
            EraseVector(v);
            return 3;  // successfully deleted the medicine
        }
    }
    EraseVector(v);

    return -6;  // medicine not found
}

// Function that updates the quantity and price of a medicine
// @param *controller: a pointer to a controller
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param command: a boolean that represents if the operation is a command or not
// @param *name: a pointer to a string
// @param *concentration: a pointer to a string
// @param *quantity: a pointer to a string
// @param *price: a pointer to a string
// @return: 4 if the medicine was successfully updated, -1 if the name is invalid, -2 if the concentration is invalid, -3 if the quantity is invalid, -4 if the price is invalid, -6 if the medicine was not found
int UpdateMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration, char *quantity, char *price)
{
    if (strlen(name) < 1)                    return -1;
    if (IsValidInt(concentration) == false)  return -2;
    if (IsValidInt(quantity) == false)       return -3;
    if (IsValidInt(price) == false)          return -4;

    int c = atoi(concentration);
    int q = atoi(quantity);
    int p = atoi(price);

    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strcmp(elem -> name, name) == 0 && elem -> concentration == c)
        {
            if (command == false)
                RecordUndoOperation(undoRedoController, GetMedicinesRepository(&controller->repo));
            else
                RecordUndoCommand(undoRedoCommand, "add_update", CreateMedicine(name, c, q - elem->quantity, p - elem->price));

            SetQuantityAtPositionRepository(&controller->repo, q, i);
            SetPriceAtPosition(&controller->repo, p, i);
            EraseVector(v);
            return 4;  // successfully updated the medicine
        }
    }
    EraseVector(v);

    return -6;  // medicine not found
}

// Function that filters the medicines by name
// @param *controller: a pointer to a controller
// @param *name: a pointer to a string
// @return: a vector of medicines that contain the given name, sorted in ascending order by name
Vector *FilterByNameController(Controller *controller, char *name)
{
    Vector *vect = CreateVector();
    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strstr(elem -> name, name) != NULL)
        {
            TElem *newElem = (TElem*) malloc(sizeof(TElem));
            strcpy(newElem -> name, elem -> name);
            newElem -> concentration = elem -> concentration;
            newElem -> quantity = elem -> quantity;
            newElem -> price = elem -> price;

            PushBack(vect, newElem);
        }
    }

    for (int i = 0; i < Size(vect) - 1; i++)
    {
        TElem *elem_i = (TElem*) v -> elem[i];
        for (int j = i + 1; j < Size(vect); j++)
        {
            TElem *elem_j = (TElem*) v -> elem[j];
            if (strcmp(elem_i -> name, elem_j -> name) > 0)
            {
                TElem *temp = vect -> elem[i];
                vect -> elem[i] = vect -> elem[j];
                vect -> elem[j] = temp;
            }
        }
    }

    EraseVector(v);
    return vect;
}

// Function that filters the medicines by concentration
// @param *controller: a pointer to a controller
// @param *concentration: a pointer to a string
// @return: a vector of medicines that have a concentration greater than or equal to the given concentration
Vector *FilterByConcentrationController(Controller *controller, char *concentration)
{
    if (IsValidInt(concentration) == false)
        return NULL;  // invalid concentration
    int c = atoi(concentration);

    Vector *vect = CreateVector();
    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (elem -> concentration >= c)
        {
            TElem *newElem = (TElem*) malloc(sizeof(TElem));
            strcpy(newElem -> name, elem -> name);
            newElem -> concentration = elem -> concentration;
            newElem -> quantity = elem -> quantity;
            newElem -> price = elem -> price;

            PushBack(vect, newElem);
        }
    }

    for (int i = 0; i < Size(vect) - 1; i++)
    {
        TElem *elem_i = (TElem*) v -> elem[i];
        for (int j = i + 1; j < Size(vect); j++)
        {
            TElem *elem_j = (TElem*) v -> elem[j];
            if (strcmp(elem_i -> name, elem_j -> name) < 0)
            {
                TElem *temp = vect -> elem[i];
                vect -> elem[i] = vect -> elem[j];
                vect -> elem[j] = temp;
            }
        }
    }

    EraseVector(v);
    return vect;
}

// Function that filters the medicines by supply in ascending order
// @param *controller: a pointer to a controller
// @param *quantity: a pointer to a string
// @return: a vector of medicines that have a quantity less than the given quantity, sorted in ascending order by quantity
Vector *FilterBySupplyAscendingController(Controller *controller, char *quantity)
{
    if (IsValidInt(quantity) == false)
        return NULL;  // invalid concentration
    int q = atoi(quantity);

    Vector *vect = CreateVector();
    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (elem -> quantity < q)
        {
            TElem *newElem = (TElem*) malloc(sizeof(TElem));
            strcpy(newElem -> name, elem -> name);
            newElem -> concentration = elem -> concentration;
            newElem -> quantity = elem -> quantity;
            newElem -> price = elem -> price;

            PushBack(vect, newElem);
        }
    }

    for (int i = 0; i < Size(vect) - 1; i++)
    {
        TElem *elem_i = (TElem*) v -> elem[i];
        for (int j = i + 1; j < Size(vect); j++)
        {
            TElem *elem_j = (TElem*) v -> elem[j];
            if (elem_i -> quantity > elem_j -> quantity)
            {
                TElem *temp = vect -> elem[i];
                vect -> elem[i] = vect -> elem[j];
                vect -> elem[j] = temp;
            }
        }
    }

    EraseVector(v);
    return vect;
}

// Function that filters the medicines by supply in descending order
// @param *controller: a pointer to a controller
// @param *quantity: a pointer to a string
// @return: a vector of medicines that have a quantity less than the given quantity, sorted in descending order by quantity
Vector *FilterBySupplyDescendingController(Controller *controller, char *quantity)
{
    if (IsValidInt(quantity) == false)
        return NULL;  // invalid quantity
    int q = atoi(quantity);

    Vector *vect = CreateVector();
    Vector *v = GetMedicinesRepository(&controller->repo);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (elem -> quantity < q)
        {
            TElem *newElem = (TElem*) malloc(sizeof(TElem));
            strcpy(newElem -> name, elem -> name);
            newElem -> concentration = elem -> concentration;
            newElem -> quantity = elem -> quantity;
            newElem -> price = elem -> price;

            PushBack(vect, newElem);
        }
    }

    for (int i = 0; i < Size(vect) - 1; i++)
    {
        TElem *elem_i = (TElem*) v -> elem[i];
        for (int j = i + 1; j < Size(vect); j++)
        {
            TElem *elem_j = (TElem*) v -> elem[j];
            if (elem_i -> quantity < elem_j -> quantity)
            {
                TElem *temp = vect -> elem[i];
                vect -> elem[i] = vect -> elem[j];
                vect -> elem[j] = temp;
            }
        }
    }

    EraseVector(v);
    return vect;
}

// Function that deletes a medicine from the repository
// @param *repo: a pointer to a repository
// @param *medicine: a pointer to a medicine
// @return: none
void DeleteMedicineCommand(Repository *repo, TElem *medicine)
{
    Vector *v = GetMedicinesRepository(repo);

    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strcmp(elem -> name, medicine -> name) == 0 && elem -> concentration == medicine -> concentration)
        {
            DeleteAtPositionRepository(repo, i);
        }
    }

    EraseVector(v);
}

// Function that adds a medicine to the repository
// @param *repo: a pointer to a repository
// @param *medicine: a pointer to a medicine
// @return: none
void AddMedicineCommand(Repository *repo, TElem *medicine)
{
    AddMedicineRepository(repo, CreateMedicine(medicine -> name, medicine -> concentration, medicine -> quantity, medicine -> price));
}

// Function that adds a medicine to the repository
// @param *repo: a pointer to a repository
// @param *medicine: a pointer to a medicine
// @return: none
void AddUpdateCommand(Repository *repo, TElem *medicine)
{
    Vector *v = GetMedicinesRepository(repo);

    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem*) v -> elem[i];
        if (strcmp(elem -> name, medicine -> name) == 0 && elem -> concentration == medicine -> concentration)
        {
            AddQuantityAtPositionRepository(repo, medicine->quantity, i);
            AddPriceAtPositionRepository(repo, medicine->price, i);
        }
    }

    EraseVector(v);
}
