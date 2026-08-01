# Release Notes

## 1.1.1 — 2026-08-01

A small patch release: dependency refresh, a build cleanup, and a leaner
`CLAUDE.md`. No challenge content has changed, and nothing about authoring or
registering challenges is different.

### Highlights

- **Dependency refresh.** `readingbat-core`/`readingbat-kotest` move to 3.3.1
  and `core-utils` to 3.2.2. Everything else in the catalog is unchanged from
  1.1.0.
- **Versions plugin relocated.** The Gradle Versions plugin moves to 0.57.0,
  and its plugin ID changes from `com.github.ben-manes.versions` to
  `io.github.ben-manes.versions`. `make versions` behaves the same.
- **Build cleanup.** The unused `Tasks` and `Shadow` constant objects and an
  unused `JvmTarget` import are gone from `build.gradle.kts`.
- **`CLAUDE.md` trimmed to 55 lines.** Everything removed was content a
  contributor or agent can reconstruct by reading the repo — the enumerated
  `make` target list, the JVM-toolchain clause, the hand-maintained toolchain
  version list, a restated Kotest convention, the kotlinter/detekt wiring
  description, and the `ci.yml` walkthrough. The gotchas, the release
  checklist, the `Content.kt` registration rules, and the detekt baseline
  caveat all survive intact.

### Upgrade notes

- If you maintain a fork with its own `build.gradle.kts`, the Versions plugin
  ID must change to `io.github.ben-manes.versions` when you move to 0.57.0;
  the old ID no longer resolves.
- No action is needed for the dependency bumps — 3.3.1 and 3.2.2 are drop-in
  patch releases.
- Building still requires **JDK 25**, and detekt is still on a `2.0.0-alpha`
  line.

### Versions

| Component        | Version          |
| ---------------- | ---------------- |
| Kotlin           | 2.4.10           |
| Ktor             | 3.5.1            |
| readingbat-core  | 3.3.1            |
| Kotest           | 6.2.3            |
| core-utils       | 3.2.2            |
| kotlin-logging   | 8.0.4            |
| Gradle           | 9.6.1            |
| kotlinter        | 5.6.0            |
| detekt           | 2.0.0-alpha.5    |
| Versions plugin  | 0.57.0           |
| JVM toolchain    | 25               |

## 1.1.0 — 2026-07-26

This is a tooling, dependency, and cleanup release. No challenge content has changed.

### Highlights

- **Dependencies refreshed across the board.** The JVM toolchain moves to 25,
  the Gradle wrapper to 9.6.1, and `readingbat-core`/`readingbat-kotest`,
  Kotlin, Kotest, Ktor, kotlinter, detekt, and `core-utils` all step forward
  (see the table below).
- **Continuous integration.** A GitHub Actions workflow runs `lintKotlin`,
  `detekt`, and `test` on every push to `master` and every pull request. Steps
  run even after an earlier one fails, so a single run reports every problem;
  stale runs on the same ref are cancelled, and Gradle reports are uploaded as
  an artifact when the job fails.
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
  annotation and `make help` prints a colorized listing. `upgrade-wrapper` now
  runs the wrapper task twice, per Gradle's documented two-step upgrade.
- **Package rename.** Java challenges moved from `group1` to `jgroup`; Kotlin
  challenges moved from `kgroup1` to `kgroup`. The directory layout, package
  declarations, and `Content.kt` `packageName` values all agree.
- **Heroku-specific cruft removed.** The `heroku`/`logs` `make` targets and the
  `system.properties` JDK pin are gone (`Procfile` and the `stage` task remain).
- **Documentation set added.** `CHANGELOG.md`, `RELEASE_NOTES.md`, and
  `llms.txt` join the refreshed `README.md` and `CLAUDE.md`.

### Upgrade notes

- Building now requires **JDK 25**.
- The detekt plugin is still on a `2.0.0-alpha` line. If CI behavior drifts,
  pin a stable release and update `gradle/libs.versions.toml` accordingly.
- The detekt baseline is no longer referenced by the build. `make detekt-baseline`
  still regenerates `detekt-baseline.xml`, but you must re-add
  `baseline = file("detekt-baseline.xml")` to `configureDetekt()` for it to be used.
- If you maintain a fork that referenced `group1` or `kgroup1` directly, update
  your `Content.kt` and any tests before pulling.
- The `versioncheck` Make target is now `versions`, and the `gradle`
  version-catalog key is now `gradle-wrapper`. Update any scripts that referenced
  the old names.

### Versions

| Component        | Version          |
| ---------------- | ---------------- |
| Kotlin           | 2.4.10           |
| Ktor             | 3.5.1            |
| readingbat-core  | 3.3.0            |
| Kotest           | 6.2.3            |
| core-utils       | 3.2.1            |
| kotlin-logging   | 8.0.4            |
| Gradle           | 9.6.1            |
| kotlinter        | 5.6.0            |
| detekt           | 2.0.0-alpha.5    |
| JVM toolchain    | 25               |
