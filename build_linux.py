import os

from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    # ConanPackageTools
    # See: https://github.com/conan-io/conan-package-tools/blob/develop/README.md
    builder = ConanMultiPackager()
    builder.add_common_builds()

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

    builder.run()
