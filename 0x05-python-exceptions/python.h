#ifndef PYTHON_H
#define PYTHON_H
#include "python.h"
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
#endif
