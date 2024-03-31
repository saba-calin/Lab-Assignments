#ifndef A2_3_916_SABAILA_CALIN_USER_INTERFACE_H
#define A2_3_916_SABAILA_CALIN_USER_INTERFACE_H

#include <stdbool.h>

#include "controller.h"
#include "undo_redo_controller.h"
#include "undo_redo_command.h"

typedef struct
{
    Controller controller;
    UndoRedoController undoRedoController;
    UndoRedoCommand undoRedoCommand;
    bool command;
} UI;

UI CreateUI();

void Start(UI *ui);
void PrintMenu();
void PrintMedicines(UI *ui);
void AddMedicine(UI *ui);
void DeleteMedicine(UI *ui);
void UpdateMedicine(UI *ui);
void FilterByName(UI *ui);
void FilterByConcentration(UI *ui);
void FilterBySupply(UI *ui);
void Undo(UI *ui);
void Redo(UI *ui);
void SetUndoPattern(UI *ui);

void HandleErrors(int result);

#endif //A2_3_916_SABAILA_CALIN_USER_INTERFACE_H
//