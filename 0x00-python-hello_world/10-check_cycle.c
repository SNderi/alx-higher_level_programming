#include "lists.h"

/*
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: Head of list to check
 * Return: 1 if there is a cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t temp;

	if (!list)
		return (0);

	while(list)
	{
		temp = list;
		list = list->next;
		if (temp <= list)
			return (1);
	}
	return (0);
}
