# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Kotlinter (`org.jmailen.kotlinter` 5.4.2) and detekt (`dev.detekt` 2.0.0-alpha.3)
  Gradle plugins with explicit configuration blocks
  (`buildUponDefaultConfig`, `parallel`, baseline, reporters).
- Kotlin `compilerOptions` block pinning `jvmTarget` to the catalog version.
- Self-documenting `make help` target driven by awk parsing of `## ` annotations.
- New Make targets: `lint`, `format`, `detekt`, `detekt-baseline`, plus a
  `_require-gradle-version` guard for `upgrade-wrapper`.
- `.editorconfig` at the repository root.

### Changed
- Renamed challenge packages: `group1` → `jgroup` (Java) and `kgroup1` → `kgroup`
  (Kotlin). `Content.kt`, `README.md`, and `CLAUDE.md` updated accordingly.
- `Content.kt` restructured to use qualified `ReturnType.*` references and
  one-line `challenge { }` declarations for readability.
- Bumped `readingbat-core` and `readingbat-kotest` to 3.1.8.
- Test logging now also surfaces `STANDARD_ERROR` events.

### Fixed
- Trimmed trailing whitespace in `README.md`.

## [1.0.0] - Initial template

- Forked from the [ReadingBat template](https://github.com/readingbat/readingbat-template).
- Wires Python, Java, and Kotlin challenge sources into the ReadingBat DSL.
