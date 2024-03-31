#ifndef A2_3_916_SABAILA_CALIN_CONTROLLER_H
#define A2_3_916_SABAILA_CALIN_CONTROLLER_H

#include <stdbool.h>

#include "repository.h"
#include "undo_redo_controller.h"
#include "undo_redo_command.h"

typedef struct
{
    Repository repo;
} Controller;

Controller CreateController();

void Add10Medicines(Controller *controller);
Vector *GetMedicinesController(Controller *controller);

int AddMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration, char *quantity, char *price);
int DeleteMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration);
int UpdateMedicineController(Controller *controller, UndoRedoController *undoRedoController, UndoRedoCommand *undoRedoCommand, bool command, char *name, char *concentration, char *quantity, char *price);
Vector *FilterByNameController(Controller *controller, char *name);
Vector *FilterByConcentrationController(Controller *controller, char *concentration);
Vector *FilterBySupplyAscendingController(Controller *controller, char *quantity);
Vector *FilterBySupplyDescendingController(Controller *controller, char *quantity);

void DeleteMedicineCommand(Repository *repo, TElem *medicine);
void AddMedicineCommand(Repository *repo, TElem *medicine);
void AddUpdateCommand(Repository *repo, TElem *medicine);

bool IsValidInt(char *c);

#endif //A2_3_916_SABAILA_CALIN_CONTROLLER_H
