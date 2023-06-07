#include "lists.h"
/**
 * check_cycle - Function that checks if a slingly list has cycle
 * @list: pointer to head of  list
 * Return: 0 on failure else 1 on success
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL || list->next == NULL)
		return (0);
	first = list;
	second = list->next;

	while (second != NULL && second->next != NULL)
	{
		if (first == second)
			return (1);
		first = first->next;
		second = second->next->next;
	}
	return (0);
}
