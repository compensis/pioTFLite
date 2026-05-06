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
