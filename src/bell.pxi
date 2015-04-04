cdef class Bell:

    cdef bell *thisptr

    def __cinit__(self, input=None):
        if input is None:
            self.thisptr = new bell()
        elif isinstance(input, Bell):
            self.thisptr = new bell(int(<Bell>input))
        elif isinstance(input, int):
            if 0 <= input <= MAX_BELL_NUMBER:
                self.thisptr = new bell(<int>input)
            else:
                raise ValueError('Number of bells out of range')
        elif isinstance(input, unicode):
            self.thisptr = new bell(<int>bell.read_char(ord(input.encode())))
        elif isinstance(input, bytes):
            self.thisptr = new bell(<int>bell.read_char(ord(input)))
        else:
            raise TypeError('Cannot convert {type} to ringing.Bell'.format(
                type=type(input).__name__
            ))

    def __dealloc__(self):
        del self.thisptr

    def __richcmp__(x, y, int op):
        cdef int bx
        cdef int by

        try:
            bx = int(Bell(x))
            by = int(Bell(y))
        except TypeError:
            return NotImplemented

        if op == 0:  # <
            return bx < by
        elif op == 1:  # <=
            return bx <= by
        elif op == 2:  # ==
            return bx == by
        elif op == 3:  # !=
            return bx != by
        elif op == 4:  # >
            return bx > by
        elif op == 5:  # >=
            return bx >= by

    def __str__(self):
        if PY_MAJOR_VERSION < 3:
            return self.__bytes__()
        else:
            return self.__unicode__()

    def __bytes__(self):
        return chr(self.thisptr.to_char())

    def __unicode__(self):
        return unichr(self.thisptr.to_char())

    def __repr__(self):
        return "Bell('{bell}')".format(bell=self)

    def __int__(self):
        return <int>deref(self.thisptr)
