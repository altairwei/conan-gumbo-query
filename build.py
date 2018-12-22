from cpt.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(username="altairwei", build_policy="missing", 
        archs=["x86_64"], visual_versions=["15"], gcc_versions=["7"], 
	    apple_clang_versions=["9.1"], visual_runtimes=["MD", "MDd"])
    builder.add_common_builds(pure_c=False)
    if platform.system() != "Windows":
        builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++")
    builder.run()
