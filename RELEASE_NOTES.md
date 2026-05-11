# Release Notes

## Unreleased

This is a tooling and cleanup release. No challenge content has changed.

### Highlights

- **Static analysis is now wired in.** `make lint` runs both `kotlinter` and
  `detekt`; `make format` applies kotlinter's formatter. Detekt is configured
  with `buildUponDefaultConfig = true` and supports an optional baseline file
  (`detekt-baseline.xml`) generated via `make detekt-baseline`.
- **Self-documenting Makefile.** Every target now carries a `## description`
  annotation and `make help` prints a colorized listing.
- **Kotlin compiler options pinned via the catalog.** `jvmTarget` is now
  derived from the `jvm` version in `gradle/libs.versions.toml` rather than
  inferred from the toolchain alone.
- **Package rename.** Java challenges moved from `group1` to `jgroup`; Kotlin
  challenges moved from `kgroup1` to `kgroup`. The directory layout, package
  declarations, and `Content.kt` `packageName` values all agree.

### Upgrade notes

- The detekt plugin is still on a `2.0.0-alpha` line. If CI behavior drifts,
  pin a stable 1.x detekt and update `gradle/libs.versions.toml` accordingly.
- If you maintain a fork that referenced `group1` or `kgroup1` directly, update
  your `Content.kt` and any tests before pulling.

### Versions

| Component        | Version          |
| ---------------- | ---------------- |
| Kotlin           | 2.3.21           |
| Ktor             | 3.4.3            |
| readingbat-core  | 3.1.8            |
| Gradle           | 9.5.0            |
| kotlinter        | 5.4.2            |
| detekt           | 2.0.0-alpha.3    |
| JVM toolchain    | 17               |
