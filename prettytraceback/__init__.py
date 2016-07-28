from _version import version

import os
import sys
import site

fname = site.__file__.replace('.pyc', '.py')
fbak = fname + '.bak'

def install(quiet=False):
    if hasattr(site, 'prettytb'):
        if not quiet:
            raise Exception('prettytb is already installed!')
        else:
            return

    try:
        import prettytraceback
    except ImportError:
        raise Exception('Not installing prettytraceback because '
            'it\'s cannot be imported')

    import shutil

    print('backing up %s' % fname)
    shutil.copy2(fname, fbak)

    print('installing to %s' % fname)
    with open(fname, 'a') as f:
        f.write('\n\ntry:\n    import prettytraceback\nexcept: pass\n\n')
    print('success!')


def uninstall():
    import os
    import shutil

    if not os.path.isfile(fbak):
        raise Exception('backup file not found! '
            'either prettytb was not installed, '
            'or manually remove the import at the bottom of %s' % fname)

    print('restoring %s' % fbak)
    shutil.copy2(fbak, fname)

    print('deleting %s' % fbak)
    os.remove(fbak)

    print('success!')


def set_hook():
    pass
    # import cgitb
    # cgitb.enable(format='text')

    import sys
    from IPython.core import ultratb
    sys.excepthook = ultratb.VerboseTB()


def main():
    for arg in sys.argv[1:]:
        if arg == 'install':
            install()
        elif arg == 'uninstall':
            uninstall()
        elif arg == 'site':
            print(site.__file__.replace('.pyc', '.py'))
        else:
            raise Exception('invalid command: %r' % arg)

if __name__ == '__main__':
    main()
else:
    set_hook()
