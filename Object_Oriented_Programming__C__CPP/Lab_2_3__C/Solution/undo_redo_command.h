#ifndef A2_3_916_SABAILA_CALIN_UNDO_REDO_COMMAND_H
#define A2_3_916_SABAILA_CALIN_UNDO_REDO_COMMAND_H

#include "vector.h"
#include "repository.h"

typedef struct
{
    Vector *undoVector;
    Vector *redoVector;
} UndoRedoCommand;

UndoRedoCommand CreateUndoRedoCommand();

void EraseUndoRedoCommand(Vector *v);
void RecordUndoCommand(UndoRedoCommand *undoRedoCommand, char *operation, TElem elem);
int UndoCommand(UndoRedoCommand *undoRedoCommand, Repository *repo);
int RedoCommand(UndoRedoCommand *undoRedoCommand, Repository *repo);
void InvalidateRedoVectorCommand(UndoRedoCommand *undoRedoCommand);

#endif //A2_3_916_SABAILA_CALIN_UNDO_REDO_COMMAND_H
