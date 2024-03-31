#include <stdio.h>
#include <string.h>

#include "domain.h"

// Function that returns the name of a medicine
// @param *medicine: a pointer to a medicine
// @return: a string
char *GetName(TElem *medicine)
{
    return medicine -> name;
}

// Function that returns the concentration of a medicine
// @param *medicine: a pointer to a medicine
// @return: an integer
int GetConcentration(TElem *medicine)
{
    return medicine -> concentration;
}

// Function that returns the quantity of a medicine
// @param *medicine: a pointer to a medicine
// @return: an integer
int GetQuantity(TElem *medicine)
{
    return medicine -> quantity;
}

// Function that returns the price of a medicine
// @param *medicine: a pointer to a medicine
// @return: an integer
int GetPrice(TElem *medicine)
{
    return medicine -> price;
}

// Function that sets the name of a medicine
// @param *medicine: a pointer to a medicine
// @param *name: a string
// @return: none
void SetName(TElem *medicine, char *name)
{
    strcpy(medicine -> name, name);
}

// Function that sets the concentration of a medicine
// @param *medicine: a pointer to a medicine
// @param concentration: an integer
// @return: none
void SetConcentration(TElem *medicine, int concentration)
{
    medicine -> concentration = concentration;
}

// Function that sets the quantity of a medicine
// @param *medicine: a pointer to a medicine
// @param quantity: an integer
// @return: none
void SetQuantity(TElem *medicine, int quantity)
{
    medicine -> quantity = quantity;
}

// Function that sets the price of a medicine
// @param *medicine: a pointer to a medicine
// @param price: an integer
// @return: none
void SetPrice(TElem *medicine, int price)
{
    medicine -> price = price;
}

// Function that creates a medicine
// @param *name: a string
// @param concentration: an integer
// @param quantity: an integer
// @param price: an integer
// @return: a medicine
TElem CreateMedicine(char *name, int concentration, int quantity, int price)
{
    TElem elem;
    strcpy(elem.name, name);
    elem.concentration = concentration;
    elem.quantity = quantity;
    elem.price = price;
    return elem;
}
