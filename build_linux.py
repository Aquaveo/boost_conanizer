import os

from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    # ConanPackageTools
    # See: https://github.com/conan-io/conan-package-tools/blob/develop/README.md
    builder = ConanMultiPackager(username='aquaveo', password='wrong!', upload='https://conan.aquaveo.com')
    builder.add_common_builds()

    for settings, options, env_vars, build_requires, reference in builder.items:
        # Require c++11 compatibility
        if settings['compiler'] == 'gcc':
            settings.update({
                'compiler.libcxx': 'libstdc++11'
            })
            compiler_version = int(settings['compiler.version'])
            if compiler_version in [5, 6]:
                settings.update({'cppstd': '14'})
            elif compiler_version == 7:
                settings.update({'cppstd': '17'})
            else:
                raise RuntimeError('Compiler must be GCC 5, 6, or 7')
        else:
            raise RuntimeError('Compiler must be GCC 5, 6, or 7')

    print(f'os.getenv("CONAN_USERNAME", "NONE") = {os.getenv("CONAN_USERNAME", "NONE").replace("v", "z")}')
    print(f'os.getenv("CONAN_PASSWORD", "NONE") = {os.getenv("CONAN_PASSWORD", "NONE").replace("v", "z")}')
    print(f'os.getenv("CONAN_UPLOAD", "NONE") = {os.getenv("CONAN_UPLOAD", "NONE").replace("v", "z")}')
    print(f'os.getenv("CONAN_REFERENCE", "NONE") = {os.getenv("CONAN_REFERENCE", "NONE").replace("v", "z")}')
    print(f'self.remotes_manager.upload_remote_name = {builder.remotes_manager.upload_remote_name.replace("v", "z")}')
    builder.run()
