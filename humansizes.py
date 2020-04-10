SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    (this is a docstring)

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    
    # if a_kilobyte_is_1024_bytes:
    #     multiple = 1024
    # else:
    #     multiple = 1000
        
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        # size = size/multiple
        print("size", size)
        
        if size < multiple:
            return '{0:.4f} hello there {1}'.format(size, suffix)

    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(16384123213782132, False))
    print(approximate_size(size=5, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(16384))
