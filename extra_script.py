Import("env", "projenv")
from SCons.Script import DefaultEnvironment

if env.IsIntegrationDump():
    Return()

print("[pioTFLite] Injecting define: TF_LITE_STATIC_MEMORY")

# Ensure TF_LITE_STATIC_MEMORY is defined globally:
# - `projenv` affects the main project sources
# - `DefaultEnvironment()` propagates to all build environments
# This is required so both the library and its consumers use the same
# TensorFlow Lite ABI.
projenv.Append(CPPDEFINES=["TF_LITE_STATIC_MEMORY"])
DefaultEnvironment().Append(CPPDEFINES=["TF_LITE_STATIC_MEMORY"])
