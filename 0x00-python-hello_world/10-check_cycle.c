#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *slowPtr;
    listint_t *fastPtr;

    if (list == NULL)
        return (0);

    slowPtr = list;
    fastPtr = list;

    if (slowPtr == fastPtr)
        return (1);
    while (list)
    {
        slowPtr = slowPtr->next;
        fastPtr = fastPtr->next->next;

        if (slowPtr == fastPtr)
            return (1);
    }
    return (0);
}
