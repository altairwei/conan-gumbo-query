import sys, os, shutil
from conans import ConanFile, CMake, tools

class GumboqueryConan(ConanFile):
    name = "GumboQuery"
    version = "latest"
    license = "MIT License"
    url = "https://github.com/altairwei/conan-gumbo-query"
    description = "A C++ library that provides jQuery-like selectors for Google's Gumbo-Parser."
    requires = "Gumbo/0.10.1@altairwei/testing"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["CMakeLists.txt", "CMakeLists.src.txt"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake", "cmake_find_package"
    _source_subfolder = "source_subfolder"

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/lazytiger/gumbo-query.git")
        os.rename(os.path.join(self._source_subfolder, "CMakeLists.txt"),
                  os.path.join(self._source_subfolder, "CMakeListsOriginal.txt"))
        shutil.copy("CMakeLists.txt",
                    os.path.join(self._source_subfolder, "CMakeLists.txt"))
        os.rename(os.path.join(self._source_subfolder, "src", "CMakeLists.txt"),
                  os.path.join(self._source_subfolder, "src","CMakeListsOriginal.txt"))
        shutil.copy("CMakeLists.src.txt",
                    os.path.join(self._source_subfolder, "src","CMakeLists.txt"))

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        if self.settings.os == "Windows":
            cmake.definitions["CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS"] = self.options.shared
        cmake.configure(source_folder=self._source_subfolder)
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*.h", dst="include/gumbo-query", 
            src=os.path.join(self._source_subfolder, "src"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        # Add Gumbo include_path to user, which is needed by
        # some GumboQuery header files.
        self.cpp_info.includedirs.append(
            os.path.join(self.deps_cpp_info["Gumbo"].include_paths[0], "gumbo-parser"))
        self.cpp_info.libs = tools.collect_libs(self)

