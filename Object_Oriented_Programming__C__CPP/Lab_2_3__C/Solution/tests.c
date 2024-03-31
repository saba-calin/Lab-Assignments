#include <stdio.h>
#include <assert.h>
#include <malloc.h>
#include <string.h>
#include <stdbool.h>

#include "tests.h"
#include "vector.h"
#include "controller.h"
#include "undo_redo_controller.h"
#include "undo_redo_command.h"
#include "repository.h"
#include "domain.h"

// This function tests the vector
// @param: none
// @return: none
void TestVector()
{
    Vector *v = CreateVector();
    assert(Size(v) == 0);
    assert(Capacity(v) == 1);

    char *c = (char*) malloc(50 * sizeof(char));
    strcpy(c, "test");
    PushBack(v, c);
    assert(Size(v) == 1);

    char *temp = (char*) v -> elem[0];
    assert(strcmp(temp, "test") == 0);

    DeleteAtPosition(v, 0);
    assert(Size(v) == 0);

    EraseVector(v);
}

// This function tests the add function
// @param: none
// @return: none
void TestAdd()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");

    Vector *v = GetMedicinesRepository(&controller.repo);
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "test") == 0);
    assert(elem -> concentration == 1);
    assert(elem -> quantity == 1);
    assert(elem -> price == 1);

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    Vector *vect = GetMedicinesRepository(&controller.repo);
    elem = (TElem*) vect -> elem[0];
    assert(elem -> quantity == 2);

    EraseVector(v);
    EraseVector(vect);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the update function
// @param: none
// @return: none
void TestUpdate()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");

    Vector *v = GetMedicinesRepository(&controller.repo);
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "test") == 0);
    assert(elem -> concentration == 1);
    assert(elem -> quantity == 1);
    assert(elem -> price == 1);

    UpdateMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "5", "5");
    Vector *vect = GetMedicinesRepository(&controller.repo);
    elem = (TElem*) vect -> elem[0];
    assert(elem -> quantity == 5);
    assert(elem -> price == 5);

    EraseVector(v);
    EraseVector(vect);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the delete function
// @param: none
// @return: none
void TestDelete()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");

    Vector *v = GetMedicinesRepository(&controller.repo);
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "test") == 0);
    assert(elem -> concentration == 1);
    assert(elem -> quantity == 1);
    assert(elem -> price == 1);

    DeleteMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1");
    Vector *vect = GetMedicinesRepository(&controller.repo);
    assert(Size(vect) == 0);

    EraseVector(v);
    EraseVector(vect);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the filter by name function
// @param: none
// @return: none
void TestFilterByName()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    Vector *v = FilterByNameController(&controller, "m");
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "mmm") == 0);
    assert(elem -> concentration == 2);
    assert(elem -> quantity == 2);
    assert(elem -> price == 2);

    EraseVector(v);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the filter by concentration function
// @param: none
// @return: none
void TestFilterByConcentration()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    Vector *v = FilterByConcentrationController(&controller, "2");
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "mmm") == 0);
    assert(elem -> concentration == 2);
    assert(elem -> quantity == 2);
    assert(elem -> price == 2);

    EraseVector(v);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the filter by supply ascending function
// @param: none
// @return: none
void TestFilterBySupplyAscending()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    Vector *v = FilterBySupplyAscendingController(&controller, "3");
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "test") == 0);
    assert(elem -> concentration == 1);
    assert(elem -> quantity == 1);
    assert(elem -> price == 1);

    EraseVector(v);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}


// This function tests the filter by supply descending function
// @param: none
// @return: none
void TestFilterBySupplyDescending()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    Vector *v = FilterBySupplyDescendingController(&controller, "3");
    TElem *elem = (TElem*) v -> elem[0];
    assert(strcmp(elem -> name, "mmm") == 0);
    assert(elem -> concentration == 2);
    assert(elem -> quantity == 2);
    assert(elem -> price == 2);

    EraseVector(v);
    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the undo function
// @param: none
// @return: none
void TestUndo()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    assert(Size(controller.repo.medicines) == 2);
    UndoController(&undoRedoController, &controller.repo);
    assert(Size(controller.repo.medicines) == 1);

    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the redo function
// @param: none
// @return: none
void TestRedo()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, false, "mmm", "2", "2", "2");

    assert(Size(controller.repo.medicines) == 2);
    UndoController(&undoRedoController, &controller.repo);
    assert(Size(controller.repo.medicines) == 1);
    RedoController(&undoRedoController, &controller.repo);
    assert(Size(controller.repo.medicines) == 2);

    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the undo command function
// @param: none
// @return: none
void TestUndoCommand()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, true, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, true, "mmm", "2", "2", "2");

    assert(Size(controller.repo.medicines) == 2);
    UndoCommand(&undoRedoCommand, &controller.repo);
    assert(Size(controller.repo.medicines) == 1);

    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}

// This function tests the redo command function
// @param: none
// @return: none
void TestRedoCommand()
{
    Controller controller = CreateController();
    UndoRedoController undoRedoController = CreateUndoRedoController();
    UndoRedoCommand undoRedoCommand = CreateUndoRedoCommand();

    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, true, "test", "1", "1", "1");
    AddMedicineController(&controller, &undoRedoController, &undoRedoCommand, true, "mmm", "2", "2", "2");

    assert(Size(controller.repo.medicines) == 2);
    UndoCommand(&undoRedoCommand, &controller.repo);
    assert(Size(controller.repo.medicines) == 1);
    RedoCommand(&undoRedoCommand, &controller.repo);
    assert(Size(controller.repo.medicines) == 2);

    EraseVector(controller.repo.medicines);
    EraseUndoRedoVector(undoRedoController.undoVector);
    EraseUndoRedoVector(undoRedoController.redoVector);
    EraseUndoRedoCommand(undoRedoCommand.undoVector);
    EraseUndoRedoCommand(undoRedoCommand.redoVector);
}


// This function tests all functions
// @param: none
// @return: none
void TestAll()
{
    TestVector();
    TestAdd();
    TestUpdate();
    TestDelete();
    TestFilterByName();
    TestFilterByConcentration();
    TestFilterBySupplyAscending();
    TestFilterBySupplyDescending();
    TestUndo();
    TestRedo();
    TestUndoCommand();
    TestRedoCommand();
}
