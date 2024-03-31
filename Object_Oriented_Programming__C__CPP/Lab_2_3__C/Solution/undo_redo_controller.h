#ifndef A2_3_916_SABAILA_CALIN_UNDO_REDO_CONTROLLER_H
#define A2_3_916_SABAILA_CALIN_UNDO_REDO_CONTROLLER_H

#include "repository.h"
#include "vector.h"

typedef struct
{
    Vector *undoVector;
    Vector *redoVector;
} UndoRedoController;

UndoRedoController CreateUndoRedoController();

void EraseUndoRedoVector(Vector *v);
void RecordUndoOperation(UndoRedoController *undoRedoController, Vector *v);
void RecordUndoOperationForRedo(UndoRedoController *undoRedoController, Vector *v);
void RecordRedoOperation(UndoRedoController *undoRedoController, Vector *v);
int UndoController(UndoRedoController *undoRedoController, Repository *repo);
int RedoController(UndoRedoController *undoRedoController, Repository *repo);
void InvalidateRedoVector(UndoRedoController *undoRedoController);

#endif //A2_3_916_SABAILA_CALIN_UNDO_REDO_CONTROLLER_H
