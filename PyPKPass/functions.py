import os
import subprocess

def gather_image_locations(imageLocation):
    if not imageLocation:
        return []

    rootImageLocation = os.path.splitext(imageLocation)[0]
    rootImageExtension = os.path.splitext(imageLocation)[1]
    retinaImageLocation = '%s@2x%s' % (rootImageLocation, rootImageExtension)
    
    imageLocations = []
    if os.path.exists(imageLocation):
        imageLocations.append(imageLocation)
    if os.path.exists(retinaImageLocation):
        imageLocations.append(retinaImageLocation)

    return imageLocations

# provides compatibility with python < 2.7
def check_output(*popenargs, **kwargs):
    r"""Run command with arguments and return its output as a byte string.

    If the exit code was non-zero it raises a CalledProcessError.  The
    CalledProcessError object will have the return code in the returncode
    attribute and output in the output attribute.

    The arguments are the same as for the Popen constructor.  Example:

    >>> check_output(["ls", "-l", "/dev/null"])
    'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'

    The stdout argument is not allowed as it is used internally.
    To capture standard error in the result, use stderr=STDOUT.

    >>> check_output(["/bin/sh", "-c",
    ...               "ls -l non_existent_file ; exit 0"],
    ...              stderr=STDOUT)
    'ls: non_existent_file: No such file or directory\n'
    """
    if hasattr(subprocess, 'check_output'):
        return subprocess.check_output(*popenargs, **kwargs)
    
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(retcode, cmd)
    return output