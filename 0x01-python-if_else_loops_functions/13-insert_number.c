#include "lists.h"

listint_t *createNewNode(listint_t *newNode, int number)
{
    newNode = malloc(sizeof(listint_t));
    if (!newNode)
        return NULL;

    newNode->n = number;
    newNode->next = NULL;
    return (newNode);
}

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newNode = NULL;
    listint_t *currentNode = NULL;

    listint_t *MynewNode = createNewNode(newNode, number);
    /*If node is the smalles number set it to the first node*/
    if (*head == NULL || (number < (*head)->n))
    {
        newNode->next = *head;
        *head = MynewNode;
        return (MynewNode);
    }

    while (currentNode->next != NULL && currentNode->next->n > MynewNode->n)
        return (currentNode->next);

    MynewNode->next = currentNode->next;
    currentNode->next = MynewNode;

    return (currentNode);
}