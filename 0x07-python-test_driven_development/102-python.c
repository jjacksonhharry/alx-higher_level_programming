#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: A pyObject string
 */
void print_python_string(PyObject *p)
{
	PyUnicodeObject *s = (PyUnicodeObject *)p;
	Py_ssize_t len;

	if (!PyUnicode_Check(s))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	len = PyUnicode_GET_LENGTH(s);

	printf("  [.] %ls\n", PyUnicode_AsWideCharString(s, &len));
}
