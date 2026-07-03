# Release Notes

## Unreleased

This is a tooling, dependency, and cleanup release. No challenge content has changed.

### Highlights

- **Dependencies refreshed across the board.** The JVM toolchain moves to 25,
  the Gradle wrapper to 9.6.1, and `readingbat-core`/`readingbat-kotest`,
  Kotest, Ktor, detekt, and `core-utils` all step forward (see the table below).
- **`build.gradle.kts` refactored into `configure*` functions.** Each concern
  (Kotlin, detekt, kotlinter, ktor, shadow, test, versions) is now its own small
  extension function, making the build easier to scan and extend.
- **Unused-return-value checking.** Production Kotlin compiles with
  `-Xreturn-value-checker=check`. Test sources are exempt, since Kotest's
  assertion DSL returns its receiver and would otherwise flag every assertion.
- **Smarter dependency-update filtering.** `make versions` now ignores
  pre-release candidates for dependencies on a stable version, while still
  surfacing newer pre-releases for deps intentionally tracking a pre-release
  line (e.g. detekt's alpha).
- **Static analysis is wired in.** `make lint` runs both `kotlinter` and
  `detekt` (now scanning main *and* test sources); `make format` applies
  kotlinter's formatter.
- **Self-documenting Makefile.** Every target carries a `## description`
  annotation and `make help` prints a colorized listing.
- **Package rename.** Java challenges moved from `group1` to `jgroup`; Kotlin
  challenges moved from `kgroup1` to `kgroup`. The directory layout, package
  declarations, and `Content.kt` `packageName` values all agree.
- **Heroku-specific cruft removed.** The `heroku`/`logs` `make` targets and the
  `system.properties` JDK pin are gone (`Procfile` and the `stage` task remain).

### Upgrade notes

- Building now requires **JDK 25**.
- The detekt plugin is still on a `2.0.0-alpha` line. If CI behavior drifts,
  pin a stable release and update `gradle/libs.versions.toml` accordingly.
- The detekt baseline is no longer referenced by the build. `make detekt-baseline`
  still regenerates `detekt-baseline.xml`, but you must re-add
  `baseline = file("detekt-baseline.xml")` to `configureDetekt()` for it to be used.
- If you maintain a fork that referenced `group1` or `kgroup1` directly, update
  your `Content.kt` and any tests before pulling.

### Versions

| Component        | Version          |
| ---------------- | ---------------- |
| Kotlin           | 2.4.0            |
| Ktor             | 3.5.1            |
| readingbat-core  | 3.2.1            |
| Kotest           | 6.2.1            |
| Gradle           | 9.6.1            |
| kotlinter        | 5.5.0            |
| detekt           | 2.0.0-alpha.5    |
| JVM toolchain    | 25               |
