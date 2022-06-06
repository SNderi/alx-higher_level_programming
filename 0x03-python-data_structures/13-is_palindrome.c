#include <lists.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: Pointer to first node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	listint_t *rev = NULL;
	listint_t *current;

	while (temp->next != NULL)
	{
		current = temp;
		current->next = *rev;
		rev = current;
		temp = temp->next;
	}

	while (*head->next != NULL)
	{
		if (rev == *head)
		{
			rev = rev->next;
			*head = *head->next;
		}
		else
		{
			return (0);
		}
	}
	return (1);
}
