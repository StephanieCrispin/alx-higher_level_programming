#include "lists.h"

int check_cycle(listint_t *list)
{

    if (list == NULL)
        return (0);

    listint_t *slowPtr = list;
    listint_t *fastPtr = list;

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
