#include <stdio.h>
#include <malloc.h>
#include <string.h>

#include "undo_redo_command.h"
#include "undo_redo_controller.h"
#include "controller.h"

// Function that creates an undo-redo command
// @param: none
// @return: an undo-redo command
UndoRedoCommand CreateUndoRedoCommand()
{
    UndoRedoCommand undoRedoCommand;
    undoRedoCommand.undoVector = CreateVector();
    undoRedoCommand.redoVector = CreateVector();
    return undoRedoCommand;
}

// Function that erases an undo-redo command
// @param *v: a pointer to an undo-redo command
// @return: none
void EraseUndoRedoCommand(Vector *v)
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

// Function that records an undo command
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param *operation: a pointer to a string
// @param elem: a medicine
// @return: none
void RecordUndoCommand(UndoRedoCommand *undoRedoCommand, char *operation, TElem elem)
{
    InvalidateRedoVectorCommand(undoRedoCommand);

    char *c = (char*) malloc(50 * sizeof(char));
    if (strcmp(operation, "add") == 0)
        strcpy(c, operation);
    else if (strcmp(operation, "add_update") == 0)
        strcpy(c, operation);
    else if (strcmp(operation, "delete") == 0)
        strcpy(c, operation);

    TElem *cpy = (TElem*) malloc(sizeof(TElem));
    *cpy = elem;

    Vector *v = CreateVector();
    PushBack(v, c);
    PushBack(v, cpy);
    PushBack(undoRedoCommand->undoVector, v);
}

// Function that undoes the last operation
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param *repo: a pointer to a repository
// @return: none
int UndoCommand(UndoRedoCommand *undoRedoCommand, Repository *repo)
{
    if (Size(undoRedoCommand->undoVector) == 0)
        return -7;

    Vector *temp = undoRedoCommand->undoVector->elem[Size(undoRedoCommand->undoVector) - 1];
    char *operation = (char*) temp -> elem[0];
    TElem *elem = (TElem*) temp -> elem[1];

    Vector *v = CreateVector();
    char *c = (char*) malloc(50 * sizeof(char));

    // creating a copy of the medicine
    TElem *cpy = (TElem*) malloc(sizeof(TElem));
    strcpy(cpy -> name, elem -> name);
    cpy -> concentration = elem -> concentration;
    cpy -> quantity = elem -> quantity;
    cpy-> price = elem -> price;

    // Updating the repository
    if (strcmp(operation, "add") == 0)
    {
        strcpy(c, "delete");
        PushBack(v, c);
        PushBack(v, cpy);

        DeleteMedicineCommand(repo, elem);
    }
    else if (strcmp(operation, "add_update") == 0)
    {
        strcpy(c, "add_update");
        PushBack(v, c);
        cpy -> quantity = (-1) * cpy -> quantity;
        cpy -> price = (-1) * cpy -> price;
        PushBack(v, cpy);

        elem -> quantity = (-1) * elem -> quantity;
        elem -> price = (-1) * elem -> price;
        AddUpdateCommand(repo, elem);
    }
    else if (strcmp(operation, "delete") == 0)
    {
        strcpy(c, "add");
        PushBack(v, c);
        PushBack(v, cpy);

        AddMedicineCommand(repo, elem);
    }

    PushBack(undoRedoCommand->redoVector, v);

    // Deleting the last element of the undo vector and updating its size
    EraseVector(undoRedoCommand->undoVector->elem[Size(undoRedoCommand->undoVector) - 1]);
    undoRedoCommand->undoVector->size -= 1;

    return 5;
}

// Function that redoes the last operation
// @param *undoRedoCommand: a pointer to an undo-redo command
// @param *repo: a pointer to a repository
// @return: none
int RedoCommand(UndoRedoCommand *undoRedoCommand, Repository *repo)
{
    if (Size(undoRedoCommand -> redoVector) == 0)
        return -8;

    Vector *temp = undoRedoCommand->redoVector->elem[Size(undoRedoCommand->redoVector) - 1];
    char *operation = (char*) temp -> elem[0];
    TElem *elem = (TElem*) temp -> elem[1];

    Vector *v = CreateVector();
    char *c = (char*) malloc(50 * sizeof(char));

    // creating a copy of the medicine
    TElem *cpy = (TElem*) malloc(sizeof(TElem));
    strcpy(cpy -> name, elem -> name);
    cpy -> concentration = elem -> concentration;
    cpy -> quantity = elem -> quantity;
    cpy-> price = elem -> price;

    // Updating the repository
    if (strcmp(operation, "delete") == 0)
    {
        strcpy(c, "add");
        PushBack(v, c);
        PushBack(v, cpy);

        AddMedicineCommand(repo, elem);
    }
    else if (strcmp(operation, "add_update") == 0)
    {
        strcpy(c, "add_update");
        PushBack(v, c);

        cpy -> quantity = (-1) * cpy -> quantity;
        cpy -> price = (-1) * cpy -> price;
        PushBack(v, cpy);

        elem -> quantity = (-1) * elem -> quantity;
        elem -> price = (-1) * elem -> price;
        AddUpdateCommand(repo, elem);
    }
    else if (strcmp(operation, "add") == 0)
    {
        strcpy(c, "delete");
        PushBack(v, c);
        PushBack(v, cpy);

        DeleteMedicineCommand(repo, elem);
    }
    PushBack(undoRedoCommand->undoVector, v);

    // Deleting the last element of the undo vector and updating its size
    EraseVector(undoRedoCommand->redoVector->elem[Size(undoRedoCommand->redoVector) - 1]);
    undoRedoCommand->redoVector->size -= 1;

    return 6;
}

// Function that invalidates the redo vector
// @param *undoRedoCommand: a pointer to an undo-redo command
// @return: none
void InvalidateRedoVectorCommand(UndoRedoCommand *undoRedoCommand)
{
    for (int i = 0; i < Size(undoRedoCommand -> redoVector); i++)
    {
        EraseVector(undoRedoCommand -> redoVector -> elem[i]);
    }
    undoRedoCommand->redoVector->size = 0;
}
