from cpt.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager(username="altairwei", build_policy="missing", 
        archs=["x86_64"], visual_versions=["15"], gcc_versions=["7"], 
	    apple_clang_versions=["9.1"])
    builder.add_common_builds(pure_c=False)
    builder.run()