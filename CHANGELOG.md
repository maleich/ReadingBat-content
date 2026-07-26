# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-07-26

Tooling, dependency, and documentation release. No challenge content changed.

### Added
- Kotlinter (`org.jmailen.kotlinter` 5.6.0) and detekt (`dev.detekt` 2.0.0-alpha.5)
  Gradle plugins with explicit configuration
  (`buildUponDefaultConfig`, `parallel`, reporters); detekt now scans both
  `src/main/kotlin` and `src/test/kotlin`.
- GitHub Actions CI workflow (`.github/workflows/ci.yml`) that runs `lintKotlin`,
  `detekt`, and `test` on pushes to `master` and on every pull request. Each step
  is guarded with `if: success() || failure()` so one run reports every failure,
  stale runs on the same ref are cancelled via a concurrency group, and Gradle
  reports are uploaded as an artifact on failure.
- Kotlin's unused-return-value checker (`-Xreturn-value-checker=check`) on the
  production `compileKotlin` task only (test sources are exempt because Kotest's
  assertion DSL returns its receiver).
- Ktor fat-jar configuration (`archiveFileName = "server.jar"`) and a `stage`
  task that clean-builds the project for deployment.
- Pre-release-aware `rejectVersionIf` for the dependency-updates task, so
  `make versions` ignores alpha/beta/RC/milestone/snapshot candidates for
  dependencies currently on a stable version while still surfacing newer
  pre-releases for deps already on a pre-release line.
- Self-documenting `make help` target driven by awk parsing of `## ` annotations,
  with a usage header and a broadened target-name regex.
- Make targets: `lint`, `format`, `detekt`, `detekt-baseline`, plus a
  `_require-gradle-version` guard for `upgrade-wrapper`.
- `.editorconfig` at the repository root.
- Project documentation set: `CHANGELOG.md`, `RELEASE_NOTES.md`, and `llms.txt`.

### Changed
- Renamed challenge packages: `group1` → `jgroup` (Java) and `kgroup1` → `kgroup`
  (Kotlin). `Content.kt`, `README.md`, and `CLAUDE.md` updated accordingly.
- `Content.kt` restructured to use qualified `ReturnType.*` references and
  one-line `challenge { }` declarations for readability.
- Refactored `build.gradle.kts` into focused `configure*` extension functions
  (Kotlin, detekt, kotlinter, ktor, shadow, test, versions).
- Bumped the JVM toolchain to 25, the Gradle wrapper to 9.6.1,
  `readingbat-core`/`readingbat-kotest` to 3.3.0, Kotlin to 2.4.10, Kotest to
  6.2.3, Ktor to 3.5.1, kotlin-logging to 8.0.4, and `core-utils` to 3.2.1.
- `make upgrade-wrapper` now invokes the wrapper task twice, following Gradle's
  documented two-step upgrade (the first pass rewrites
  `gradle-wrapper.properties`, the second regenerates the wrapper itself).
- Renamed the `gradle` version-catalog key to `gradle-wrapper` and switched the
  Makefile's version extraction from `awk` to `sed`.
- Renamed the `versioncheck` Make target to `versions`, which now passes
  `--no-configuration-cache --no-parallel` to `dependencyUpdates`; the default
  Make target is `help`.
- `ContentTests` updated for the suspending answer API
  (`runBlocking { … correctAnswers()[it.index] }`).
- Relaxed the shadow uberjar duplicate-handling strategy to `WARN`.
- Test logging now also surfaces `STANDARD_ERROR` events.

### Removed
- Heroku-only `make` targets (`heroku`, `logs`) and the `system.properties`
  JDK pin.
- detekt baseline wiring — `detekt-baseline.xml` is no longer referenced by the
  build (`make detekt-baseline` can still regenerate it on demand).

### Fixed
- Trimmed trailing whitespace in `README.md`.

## [1.0.0] - Initial template

- Forked from the [ReadingBat template](https://github.com/readingbat/readingbat-template).
- Wires Python, Java, and Kotlin challenge sources into the ReadingBat DSL.
