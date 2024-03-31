#include <stdio.h>
#include <malloc.h>
#include <string.h>

#include "undo_redo_controller.h"

// Function that creates an undo-redo controller
// @param: none
// @return: an undo-redo controller
UndoRedoController CreateUndoRedoController()
{
    UndoRedoController undoRedoController;
    undoRedoController.undoVector = CreateVector();
    undoRedoController.redoVector = CreateVector();
    return undoRedoController;
}

// Function that erases an undo-redo controller
// @param *v: a pointer to an undo-redo controller
// @return: none
void EraseUndoRedoVector(Vector *v)
{
    if (v == NULL)
        return;

    for (int i = 0; i < Size(v); i++)
    {
        EraseVector(v -> elem[i]);
    }
    free(v -> elem);
    free(v);
}

// Function that records an undo operation
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *v: a pointer to a vector
// @return: none
void RecordUndoOperation(UndoRedoController *undoRedoController, Vector *v)
{
    PushBack(undoRedoController->undoVector, v);
    InvalidateRedoVector(undoRedoController);
}

// Function that records an undo operation for redo
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *v: a pointer to a vector
// @return: none
void RecordUndoOperationForRedo(UndoRedoController *undoRedoController, Vector *v)
{
    PushBack(undoRedoController->undoVector, v);
}

// Function that records a redo operation
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *v: a pointer to a vector
// @return: none
void RecordRedoOperation(UndoRedoController *undoRedoController, Vector *v)
{
    PushBack(undoRedoController->redoVector, v);
}

// Function that undoes the last operation
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *repo: a pointer to a repository
// @return: 5 if the operation was successful, -7 otherwise
int UndoController(UndoRedoController *undoRedoController, Repository *repo)
{
    if (Size(undoRedoController->undoVector) == 1)
    {
        return -7;
    }

    // Saving the current state of the repository in the redo vector
    RecordRedoOperation(undoRedoController, GetMedicinesRepository(repo));

    // Updating the repository
    UpdateRepository(repo, undoRedoController->undoVector->elem[Size(undoRedoController->undoVector) - 1]);

    // Deleting the last element of the undo vector and updating its size
    EraseVector(undoRedoController->undoVector->elem[Size(undoRedoController->undoVector) - 1]);
    undoRedoController->undoVector->size -= 1;

    return 5;
}

// Function that redoes the last operation
// @param *undoRedoController: a pointer to an undo-redo controller
// @param *repo: a pointer to a repository
// @return: 6 if the operation was successful, -8 otherwise
int RedoController(UndoRedoController *undoRedoController, Repository *repo)
{
    if (Size(undoRedoController->redoVector) == 0)
    {
        return -8;
    }

    // Saving the current state of the repository in the undo vector
    RecordUndoOperationForRedo(undoRedoController, GetMedicinesRepository(repo));

    // Updating the repository
    UpdateRepository(repo, undoRedoController->redoVector->elem[Size(undoRedoController->redoVector) - 1]);

    // Deleting the last element of the redo vector and updating its size
    EraseVector(undoRedoController->redoVector->elem[Size(undoRedoController->redoVector) - 1]);
    undoRedoController->redoVector->size -=1;

    return 6;
}

// Function that invalidates the redo vector
// @param *undoRedoController: a pointer to an undo-redo controller
// @return: none
void InvalidateRedoVector(UndoRedoController *undoRedoController)
{
    for (int i = 0; i < Size(undoRedoController->redoVector); i++)
    {
        EraseVector(undoRedoController->redoVector -> elem[i]);
    }
    undoRedoController->redoVector->size = 0;
}
