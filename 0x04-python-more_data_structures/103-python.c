#include <stdio.h>
#include <Python.h>

/**
 * display_bytes_info - Displays info about python bytes
 *
 * @obj: Python object
 * Return: (Nothing)
 */
void display_bytes_info(PyObject *obj)
{
    char *data;
    Py_ssize_t size, i, limit;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(obj);
    data = PyBytes_AsString(obj);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", data);

    limit = (size >= 10) ? 10 : size;

    printf("  first %zd bytes:", limit);

    for (i = 0; i < limit; i++)
    {
        unsigned char byte = data[i];
        printf(" %02x", byte);
    }

    printf("\n");
}

/**
 * display_list_info - Displays info about python lists
 *
 * @obj: Python objec
 * Return: (nothing)
 */
void display_list_info(PyObject *obj)
{
    Py_ssize_t size, i;
    PyListObject *list;

    size = PyList_Size(obj);
    list = (PyListObject *)obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *element = PyList_GetItem(obj, i);
        const char *type_name = Py_TYPE(element)->tp_name;

        printf("Element %zd: %s\n", i, type_name);

        if (PyBytes_Check(element))
        {
            display_bytes_info(element);
        }
    }
}

