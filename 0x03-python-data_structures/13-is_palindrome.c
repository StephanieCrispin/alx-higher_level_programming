#include "lists.h"

int is_palindrome(listint_t **head);

/**
 * is_palindrome - Is a singly linked list  a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: not a palindrome - 0.
 *         is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp, *rev, *mid;
    size_t size = 0, i = 0;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    tmp = *head;
    while (tmp != NULL)
    {
        size++;
        tmp = tmp->next;
    }

    tmp = *head;
    for (; i < (size / 2) - 1; ++i)
        tmp = tmp->next;

    if ((size % 2) == 0 && tmp->n != tmp->next->n)
        return (0);

    tmp = tmp->next->next;
    rev = reverse_(&tmp);
    mid = rev;

    tmp = *head;
    while (rev)
    {
        if (tmp->n != rev->n)
            return (0);
        tmp = tmp->next;
        rev = rev->next;
    }
    reverse_(&mid);

    return (1);
}
/**
 * reverse_listint - Reverses linked list.
 * @head: points to the starting node of the list.
 *
 * Return: points to the head of the reversed list.
 */
listint_t *reverse_(listint_t **head)
{
    listint_t *node = *head, *next, *prev = NULL;

    while (node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }
    *head = prev;
    return (*head);
}
