#include <iostream>
#include <cstdio>
#include <fstream> 
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include "Python.h"
#include <DES_Common.h>
#include <DES_Table.h>
using namespace std;

inline void char2bits(uchar src, uint * bits) {
    bits[7] = (src & 1);
    bits[6] = (src & 2) >> 1;
    bits[5] = (src & 4) >> 2;
    bits[4] = (src & 8) >> 3;
    bits[3] = (src & 16) >> 4;
    bits[2] = (src & 32) >> 5;
    bits[1] = (src & 64) >> 6;
    bits[0] = (src & 128) >> 7;
}

inline void DES_unencrypt(const uchar data[], uchar * res) {
    uint init_data[64];

    GET_BITS

    uint ip_data[64];
    MAP_16(ip_data, init_data, ip, 0, 0)
    MAP_16(ip_data, init_data, ip, 16, 16)
    MAP_16(ip_data, init_data, ip, 32, 32)
    MAP_16(ip_data, init_data, ip, 48, 48)

    uint l[32], r[32];
    MAP_16(l, ip_data, identity, 0, 0)
    MAP_16(l, ip_data, identity, 16, 16)
    MAP_16(r, ip_data, identity, 32, 0)
    MAP_16(r, ip_data, identity, 48, 16)

    uint newr[48], afterf[32], afterp[32], tmp[32];
    int row, col, int2bit;

    for(int i = 15; i >= 0; i --) {

        MAP_16(newr, r, e, 0, 0)
        MAP_16(newr, r, e, 16, 16)
        MAP_16(newr, r, e, 32, 32)

        
        S_BOX(0)
        S_BOX(1)
        S_BOX(2)
        S_BOX(3)
        S_BOX(4)
        S_BOX(5)
        S_BOX(6)
        S_BOX(7)

        MAP_16(afterf, afterp, p, 0, 0)
        MAP_16(afterf, afterp, p, 16, 16)

        XOR_32(tmp, afterf, l)
        
        for(int j = 0; j < 32; j ++) {
            l[j] = r[j];
            r[j] = tmp[j];
        }
    }

    uint befip[64];
    MAP_16(befip, r, identity, 0, 32)
    MAP_16(befip, r, identity, 16, 32)
    MAP_16(befip, l, identity, 0, 32)
    MAP_16(befip, l, identity, 16, 32)

    uint bitres[64];
    MAP_16(bitres, befip, ip1, 0, 0)
    MAP_16(bitres, befip, ip1, 16, 16)
    MAP_16(bitres, befip, ip1, 32, 32)
    MAP_16(bitres, befip, ip1, 48, 48)

    for(int i = 0; i < 8; i ++) {
        uchar ch = 0;
        ch += bitres[i * 8] << 7;
        ch += bitres[i * 8 + 1] << 6;
        ch += bitres[i * 8 + 2] << 5;
        ch += bitres[i * 8 + 3] << 4;
        ch += bitres[i * 8 + 4] << 3;
        ch += bitres[i * 8 + 5] << 2;
        ch += bitres[i * 8 + 6] << 1;
        ch += bitres[i * 8];
        res[i] = ch;
    }

    res[8] = '\0';
}

inline void DES_encrypt(const uchar data[], uchar * res) {
    uint init_data[64];

    GET_BITS

    uint ip_data[64];
    MAP_16(ip_data, init_data, ip, 0, 0)
    MAP_16(ip_data, init_data, ip, 16, 16)
    MAP_16(ip_data, init_data, ip, 32, 32)
    MAP_16(ip_data, init_data, ip, 48, 48)

    uint l[32], r[32];
    MAP_16(l, ip_data, identity, 0, 0)
    MAP_16(l, ip_data, identity, 16, 16)
    MAP_16(r, ip_data, identity, 32, 0)
    MAP_16(r, ip_data, identity, 48, 16)

    uint newr[48], afterf[32], afterp[32], tmp[32];
    int row, col, int2bit;

    for(int i = 0; i < 16; i ++) {

        MAP_16(newr, r, e, 0, 0)
        MAP_16(newr, r, e, 16, 16)
        MAP_16(newr, r, e, 32, 32)

        
        S_BOX(0)
        S_BOX(1)
        S_BOX(2)
        S_BOX(3)
        S_BOX(4)
        S_BOX(5)
        S_BOX(6)
        S_BOX(7)

        MAP_16(afterf, afterp, p, 0, 0)
        MAP_16(afterf, afterp, p, 16, 16)

        XOR_32(tmp, afterf, l)
        
        for(int j = 0; j < 32; j ++) {
            l[j] = r[j];
            r[j] = tmp[j];
        }
    }

    uint befip[64];
    MAP_16(befip, r, identity, 0, 32)
    MAP_16(befip, r, identity, 16, 32)
    MAP_16(befip, l, identity, 0, 32)
    MAP_16(befip, l, identity, 16, 32)

    uint bitres[64];
    MAP_16(bitres, befip, ip1, 0, 0)
    MAP_16(bitres, befip, ip1, 16, 16)
    MAP_16(bitres, befip, ip1, 32, 32)
    MAP_16(bitres, befip, ip1, 48, 48)

    for(int i = 0; i < 8; i ++) {
        uchar ch = 0;
        ch += bitres[i * 8] << 7;
        ch += bitres[i * 8 + 1] << 6;
        ch += bitres[i * 8 + 2] << 5;
        ch += bitres[i * 8 + 3] << 4;
        ch += bitres[i * 8 + 4] << 3;
        ch += bitres[i * 8 + 5] << 2;
        ch += bitres[i * 8 + 6] << 1;
        ch += bitres[i * 8];
        res[i] = ch;
    }

    res[8] = '\0';
}

static PyObject * DES_ready_encrypt(PyObject *self, PyObject *args) {
    PyObject* ret;
    int length = 0;
    uchar * entry_data;
    uchar return_data[1024 * 1024 + 2];
    PyArg_ParseTuple(args, "s#", &entry_data, &length);
    for(int i = 0; i < length / 8; i ++) {
        uchar res[9];
        DES_encrypt(&entry_data[i * 8], res);

        MAP_8(return_data, res, 0, i * 8)
    
    }
    return_data[length] = '\0';
    ret = Py_BuildValue("s#", &return_data, length);
    return ret;
}

static PyObject * DES_ready_unencrypt(PyObject *self, PyObject *args) {
    PyObject* ret;
    int length = 0;
    uchar * entry_data;
    uchar return_data[1024 * 1024 + 2];
    PyArg_ParseTuple(args, "s#", &entry_data, &length);
    for(int i = 0; i < length / 8; i ++) {
        uchar res[9];
        DES_unencrypt(&entry_data[i * 8], res);

        MAP_8(return_data, res, 0, i * 8)

    }
    return_data[length] = '\0';
    ret = Py_BuildValue("s#", &return_data, length);
    return ret;
}

static PyObject * DES_ready_check(PyObject *self, PyObject *args) {
    PyObject* ret;
    int length = 0;
    uint flag = 1;
    uchar * entry_data1, * entry_data2;
    PyArg_ParseTuple(args, "ssl", &entry_data1, &entry_data2, &length);
    for(int i = 0; i < length; i ++) {
        if(entry_data1[i] != entry_data2[i]) {
            flag = 0;
            break;
        }
    }
    ret = Py_BuildValue("i", flag);
    return ret;
}

static PyMethodDef des_methods[] = {
    {"Encrypt", (PyCFunction) DES_ready_encrypt, METH_VARARGS, "Use DES to encrypt data"},
    {"Unencrypt", (PyCFunction) DES_ready_unencrypt, METH_VARARGS, "Use DES to unencrypt data"},
    {"Check", (PyCFunction) DES_ready_check, METH_VARARGS, "Use simple method to compare two files"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initDES_IN_CPP(void)
{
    Py_InitModule("DES_IN_CPP", des_methods);
}

