#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // Инициализация Python
    Py_Initialize();

    // Проверяем, инициализация успешна
    if (!Py_IsInitialized()) {
        fprintf(stderr, "Не удалось инициализировать Python!\n");
        return 1;
    }

    // Путь к файлу bocce.py
    const char *scriptName = "./bocce.py";
    
    // Установка пути к директории, где находится bocce.py
    PyObject *sysPath = PySys_GetObject("path");
    PyObject *path = PyUnicode_FromString(".");
    PyList_Append(sysPath, path);
    Py_DECREF(path);

    // Импортируем скрипт
    FILE* file = fopen(scriptName, "r");
    if (file) {
        PyRun_SimpleFile(file, scriptName);
        fclose(file);
    } else {
        fprintf(stderr, "Не удалось открыть файл %s\n", scriptName);
    }

    // Завершение работы Python
    Py_Finalize();
    return 0;
}
