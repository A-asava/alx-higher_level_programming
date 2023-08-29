#include <stdio.h>
#include <stdlib.h>
#include "custom_lists.h"

/**
 * display_list - prints elements of custom_list_t list
 * @list: A pointer to head of list
 * Return: number of items
 */
size_t display_list(const custom_list_t *list)
{
    const custom_list_t *current;
    unsigned int count;

    current = list;
    count = 0;

    while (current != NULL)
    {
        printf("%i\n", current->value);
        current = current->next;
        count++;
    }

    return count;
}

/**
 * add_item_to_list - adds a new item at the end of a linked list
 * @head: pointer to pointer of first item in custom_list_t list
 * @value: integer value to be included in new item
 * Return: address of new element or NULL if fails
 */
custom_list_t *add_item_to_list(custom_list_t **head, const int value)
{
    custom_list_t *new_item;
    custom_list_t *current_item;

    current_item = *head;

    new_item = malloc(sizeof(custom_list_t));
    if (new_item == NULL)
        return NULL;

    new_item->value = value;
    new_item->next = NULL;

    if (*head == NULL)
        *head = new_item;
    else
    {
        while (current_item->next != NULL)
            current_item = current_item->next;
        current_item->next = new_item;
    }

    return new_item;
}

/**
 * clear_list - frees custom_list_t list
 * @head: A pointer to list that is cleared
 * Return: (0)
 */
void clear_list(custom_list_t *head)
{
    custom_list_t *current_item;

    while (head != NULL)
    {
        current_item = head;
        head = head->next;
        free(current_item);
    }
}

