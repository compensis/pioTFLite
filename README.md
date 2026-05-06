# TensorFlow Lite Micro (PlatformIO)

This library packages the official TensorFlow Lite Micro sources for use with PlatformIO.

It lets you use TensorFlow Lite Micro in PlatformIO without manually copying and integrating upstream sources.

## Usage

Add this library to your `platformio.ini`:

```ini
lib_deps =
    https://github.com/compensis/pioTFLite.git
```

No additional configuration is required.

## Upstream Project

This package is based on the official TensorFlow Lite Micro project.

For documentation, examples, and updates, refer to the upstream repository:
https://github.com/tensorflow/tflite-micro

## Notes

* This library aims to stay as close as possible to upstream sources
* Only minimal build-related adjustments are applied
* No functional changes to TensorFlow Lite Micro are intended

## License

This package is based on TensorFlow Lite Micro and includes the upstream license text in [LICENSE](LICENSE).

Additional third-party license texts are included in:

* [third_party/flatbuffers/LICENSE](third_party/flatbuffers/LICENSE)
* [third_party/gemmlowp/LICENSE](third_party/gemmlowp/LICENSE)
* [third_party/kissfft/COPYING](third_party/kissfft/COPYING)

For additional licensing details and notices, please also refer to the upstream TensorFlow Lite Micro project.

## Required Build Flag: TF_LITE_STATIC_MEMORY

This library automatically defines the following macro during the build:

```c
TF_LITE_STATIC_MEMORY
```

### Why this matters

`TF_LITE_STATIC_MEMORY` affects TensorFlow Lite Micro types and memory-related behavior at compile time.
Because this configuration is also referenced from header files, the macro must be defined consistently for both:

* the library itself
* any application code including TensorFlow Lite Micro headers

If TF_LITE_STATIC_MEMORY is not set consistently:

* ABI mismatches can occur
* compilation may still succeed
* behavior may be incorrect or fail at runtime

### How this library handles it

This library uses a PlatformIO `extraScript` to define `TF_LITE_STATIC_MEMORY` globally for the entire build.

This ensures that both the library sources and all consuming application code are compiled with the same configuration.
