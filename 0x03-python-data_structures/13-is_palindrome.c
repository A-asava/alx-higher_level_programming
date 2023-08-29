/*
 * File: palindrome_checker.c
 * Author: Saidi Abdulaziz
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses listint_t list.
 * @head: Pointer to starting node of linked list to reverse.
 *
 * Returns: Pointer to head of reversed linked list.
 */
listint_t *reverse_listint(listint_t **head)
{
    listint_t *current = *head, *prev = NULL, *next_node;

    while (current)
    {
        next_node = current->next;
        current->next = prev;
        prev = current;
        current = next_node;
    }

    *head = prev;
    return *head;
}

/**
 * is_palindrome - The function Checks if singly linked list is palindrome.
 * @head: Pointer to the head of linked list.
 *
 * Returns: (1) if linked list is a palindrome, (0) otherwise.
 */
int is_palindrome(listint_t **head)
{
    listint_t *temp, *reversed, *mid;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    temp = *head;
    while (temp)
    {
        size++;
        temp = temp->next;
    }

    temp = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        temp = temp->next;

    if ((size % 2) == 0 && temp->n != temp->next->n)
        return 0;

    temp = temp->next->next;
    reversed = reverse_listint(&temp);
    mid = reversed;

    temp = *head;
    while (reversed)
    {
        if (temp->n != reversed->n)
            return 0;
        temp = temp->next;
        reversed = reversed->next;
    }
    reverse_listint(&mid);

    return 1;
}

