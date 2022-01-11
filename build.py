import os

from cpt.packager import ConanMultiPackager

def update_items_linux(builder):
    for settings, options, env_vars, build_requires, reference in builder.items:
        # Require c++11 compatibility
        if settings['compiler'] == 'gcc':
            settings.update({
                'compiler.libcxx': 'libstdc++11'
            })
            compiler_version = int(settings['compiler.version'])
            if compiler_version == 6:
                settings.update({'cppstd': '14'})
            elif compiler_version in [7, 8]:
                settings.update({'cppstd': '17'})
            else:
                raise RuntimeError('Compiler must be GCC 6, 7, or 8')
        else:
            raise RuntimeError('Compiler must be GCC 6, 7, or 8')


def update_items_mac(builder):
   pass


def update_items_windows(builder):
    pass


if __name__ == "__main__":
    # ConanPackageTools
    # See: https://github.com/conan-io/conan-package-tools/blob/develop/README.md
    builder = ConanMultiPackager()
    builder.add_common_builds()

    if os.environ['AQUA_OS'] == 'linux':
        update_items_linux(builder)
    elif os.environ['AQUA_OS'] == 'mac':
        update_items_mac(builder)
    elif os.environ['AQUA_OS'] == 'windows':
        update_items_windows(builder)
    else:
        raise RuntimeError("Unknown operating system: " + str(os.environ['AQUA_OS']))

    builder.run()
