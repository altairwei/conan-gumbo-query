from conans import ConanFile, CMake, tools


class GumboqueryConan(ConanFile):
    name = "GumboQuery"
    version = "latest"
    license = "MIT License"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "A C++ library that provides jQuery-like selectors for Google's Gumbo-Parser."
    requires = "GumboParser/0.10.1@altairwei/testing"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["CMakeLists.txt"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    _source_subfolder = "source_subfolder"

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/lazytiger/gumbo-query.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*.h", dst="include", src="hello")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

