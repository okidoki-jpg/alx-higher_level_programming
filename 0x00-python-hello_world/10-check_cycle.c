#include "lists.h"

/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: linked list to check.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *node;

	if (!list || !list->next)
		return (0);

	head = list->next;
	node = list->next->next;
	while (head && node && node->next)
	{
		if (head == node)
			return (1);

		head = head->next;
		node = node->next->next;
	}
	return (0);
}
