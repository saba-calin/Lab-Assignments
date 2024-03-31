#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <malloc.h>

#include "user_interface.h"
#include "controller.h"

// Function that creates a user interface
// @param: none
// @return: a user interface
UI CreateUI()
{
    UI userInterface;
    userInterface.controller = CreateController();
    userInterface.undoRedoController = CreateUndoRedoController();
    userInterface.undoRedoCommand = CreateUndoRedoCommand();
    return userInterface;
}

// Function that starts the user interface
// @param *ui: a pointer to a user interface
// @return: none
void Start(UI *ui)
{
    SetUndoPattern(ui);
    Add10Medicines(&ui->controller);

    if (ui->command == false)
        RecordUndoOperation(&ui->undoRedoController, GetMedicinesRepository(&ui->controller.repo));

    while (true)
    {
        PrintMenu();

        char option[10];
        printf(">");
        scanf("%s", option);

        if (strcmp(option, "1") == 0)       PrintMedicines(ui);
        else if (strcmp(option, "2") == 0)  AddMedicine(ui);
        else if (strcmp(option, "3") == 0)  DeleteMedicine(ui);
        else if (strcmp(option, "4") == 0)  UpdateMedicine(ui);
        else if (strcmp(option, "5") == 0)  FilterByName(ui);
        else if (strcmp(option, "6") == 0)  FilterByConcentration(ui);
        else if (strcmp(option, "7") == 0)  FilterBySupply(ui);
        else if (strcmp(option, "8") == 0)  Undo(ui);
        else if (strcmp(option, "9") == 0)  Redo(ui);
        else if (strcmp(option, "exit") == 0)
        {
            printf("Closing the program...\n");
            EraseVector(ui->controller.repo.medicines);

            EraseUndoRedoVector(ui->undoRedoController.undoVector);
            EraseUndoRedoVector(ui->undoRedoController.redoVector);

            EraseUndoRedoCommand(ui->undoRedoCommand.undoVector);
            EraseUndoRedoCommand(ui->undoRedoCommand.redoVector);
            return;
        }
        else
        {
            printf("Error: Invalid input\n");
        }
    }
}

// Function that reads the user's option for the undo pattern
// @param *ui: a pointer to a user interface
// @return: none
void SetUndoPattern(UI *ui)
{
    char option[50];
    printf("Would you like to use the command design pattern for the undo\\redo operations?(y/n)\n");
    scanf("%s", option);
    while (strcmp(option, "y") != 0 && strcmp(option, "n") != 0)
    {
        printf("Invalid option - try again\n");
        scanf("%s", option);
    }

    if (strcmp(option, "y") == 0)  ui->command = true;
    else                           ui->command = false;
}

// Function that undoes the last operation
// @param *ui: a pointer to a user interface
// @return: none
void Undo(UI *ui)
{
    int result;

    if (ui -> command == false)
        result = UndoController(&ui->undoRedoController, &ui->controller.repo);
    else
        result = UndoCommand(&ui->undoRedoCommand, &ui->controller.repo);

    HandleErrors(result);
}

// Function that redoes the last operation
// @param *ui: a pointer to a user interface
// @return: none
void Redo(UI *ui)
{
    int result;

    if (ui -> command == false)
        result = RedoController(&ui->undoRedoController, &ui->controller.repo);
    else
        result = RedoCommand(&ui->undoRedoCommand, &ui->controller.repo);

    HandleErrors(result);
}

// Function that prints the menu
// @param: none
// @return: none
void PrintMenu()
{
    printf("\n");
    printf("Press 1 to display all medicines\n");
    printf("Press 2 to add a medicine\n");
    printf("Press 3 to delete a medicine\n");
    printf("Press 4 to update a medicine\n");
    printf("Press 5 to filter medicines by name\n");
    printf("Press 6 to filter medicines by concentration\n");
    printf("Press 7 to filter medicines by supply\n");
    printf("Press 8 to undo the last operation\n");
    printf("Press 9 to redo the last operation\n");
    printf("Type \"exit\" to close the program\n");
}

// Function that prints all the medicines
// @param *ui: a pointer to a user interface
// @return: none
void PrintMedicines(UI *ui)
{
    Vector *v = GetMedicinesController(&ui->controller);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem *) v->elem[i];
        printf("name: %s, ", elem->name);
        printf("concentration: %d, ", elem->concentration);
        printf("quantity: %d, ", elem->quantity);
        printf("price: %d\n", elem->price);
    }
    EraseVector(v);
}

// Function that adds a medicine
// @param *ui: a pointer to a user interface
// @return: none
void AddMedicine(UI *ui)
{
    char name[50], concentration[50], quantity[50], price[50];

    printf("name=");
    scanf(" %[^\n]", name);

    printf("concentration=");
    scanf("%s", concentration);

    printf("quantity=");
    scanf("%s", quantity);

    printf("price=");
    scanf("%s", price);

    int result = AddMedicineController(&ui->controller, &ui->undoRedoController, &ui->undoRedoCommand, ui->command, name, concentration, quantity, price);
    HandleErrors(result);
}

// Function that deletes a medicine
// @param *ui: a pointer to a user interface
// @return: none
void DeleteMedicine(UI *ui)
{
    char name[50], concentration[50];

    printf("name=");
    scanf(" %[^\n]", name);

    printf("concentration=");
    scanf("%s", concentration);

    int result = DeleteMedicineController(&ui->controller, &ui->undoRedoController, &ui->undoRedoCommand, ui->command, name, concentration);
    HandleErrors(result);
}

// Function that updates a medicine
// @param *ui: a pointer to a user interface
// @return: none
void UpdateMedicine(UI *ui)
{
    char name[50], concentration[50], quantity[50], price[50];

    printf("name=");
    scanf(" %[^\n]", name);

    printf("concentration=");
    scanf("%s", concentration);

    printf("quantity=");
    scanf("%s", quantity);

    printf("price=");
    scanf("%s", price);

    int result = UpdateMedicineController(&ui->controller, &ui->undoRedoController, &ui->undoRedoCommand, ui->command, name, concentration, quantity, price);
    HandleErrors(result);
}

// Function that interprets the result of an operation
// @param result: an integer representing the result of the operation
// @return: none
void HandleErrors(int result)
{
    switch (result)
    {
        case 1:   printf("Successfully updated the quantity of the medicine\n");   break;
        case 2:   printf("Successfully added the medicine\n");   break;
        case 3:   printf("Successfully deleted the medicine\n");   break;
        case 4:   printf("Successfully updated the medicine\n");   break;
        case 5:   printf("Successfully undone the last operation\n");   break;
        case 6:   printf("Successfully redone the last operation\n");   break;

        case -1:   printf("Error: The name is not valid\n");   break;
        case -2:   printf("Error: The concentration is not valid\n");   break;
        case -3:   printf("Error: The quantity is not valid\n");   break;
        case -4:   printf("Error: The price is not valid\n");   break;
        case -5:   printf("Error: Cannot delete any more elements\n");   break;
        case -6:   printf("Error: The medicine was not found\n");   break;
        case -7:   printf("Error: Cannot undo any more operations\n");   break;
        case -8:   printf("Error: Cannot redo any more operations\n");   break;
    }
}

// Function that filters the medicines by name
// @param *ui: a pointer to a user interface
// @return: none
void FilterByName(UI *ui)
{
    char name[50];
    printf("name=");
    scanf(" %[^\n]", name);

    Vector (*(*ptr)(Controller *, char *)) = &FilterByNameController;
    Vector *v = ptr(&ui->controller, name);
    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem *) v->elem[i];
        printf("name: %s, ", elem->name);
        printf("concentration: %d, ", elem->concentration);
        printf("quantity: %d, ", elem->quantity);
        printf("price: %d\n", elem->price);
    }
    EraseVector(v);
}

// Function that filters the medicines by concentration
// @param *ui: a pointer to a user interface
// @return: none
void FilterByConcentration(UI *ui)
{
    char concentration[50];
    printf("concentration=");
    scanf("%s", concentration);

    Vector (*(*ptr)(Controller *, char *)) = &FilterByConcentrationController;
    Vector *v = ptr(&ui->controller, concentration);
    if (v == NULL)
        HandleErrors(-2);  // invalid concentration

    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem *) v->elem[i];
        printf("name: %s, ", elem->name);
        printf("concentration: %d, ", elem->concentration);
        printf("quantity: %d, ", elem->quantity);
        printf("price: %d\n", elem->price);
    }
    EraseVector(v);
}

// Function that filters the medicines by supply
// @param *ui: a pointer to a user interface
// @return: none
void FilterBySupply(UI *ui)
{
    char quantity[50];
    printf("quantity=");
    scanf("%s", quantity);

    char option[50];
    printf("Would you like to have the medicines sorted in ascending order?(y/n)\n");
    scanf("%s", option);
    while (strcmp(option, "y") != 0 && strcmp(option, "n") != 0)
    {
        printf("Invalid option - try again\n");
        scanf("%s", option);
    }

    Vector *v;
    Vector (*(*ptr[])(Controller *, char *)) = { FilterBySupplyAscendingController, FilterBySupplyDescendingController };
    if (strcmp(option, "y") == 0)  v = ptr[0](&ui->controller, quantity);
    else                           v = ptr[1](&ui->controller, quantity);
    if (v == NULL)
        HandleErrors(-3);  // invalid quantity

    for (int i = 0; i < Size(v); i++)
    {
        TElem *elem = (TElem *) v->elem[i];
        printf("name: %s, ", elem->name);
        printf("concentration: %d, ", elem->concentration);
        printf("quantity: %d, ", elem->quantity);
        printf("price: %d\n", elem->price);
    }
    EraseVector(v);
}
