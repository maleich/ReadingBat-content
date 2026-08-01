# CLAUDE.md

## What this repo is

A **content repository** built on the [ReadingBat template](https://github.com/readingbat/readingbat-template). It does not implement the ReadingBat web framework — it depends on `com.readingbat:readingbat-core` (see `gradle/libs.versions.toml`) and supplies:

1. Challenge source files (`python/`, `src/main/java/jgroup/`, `src/main/kotlin/kgroup/`)
2. A Kotlin DSL declaration in `src/main/kotlin/Content.kt` that wires those files into language groups, return types, and descriptions
3. A thin `ContentServer.kt` entry point that delegates to `ReadingBatServer.start(args)`

When the user asks to "add a challenge," it almost always means: add the source file under the appropriate language directory **and** register it in `Content.kt`. A file on disk is invisible to the site until the DSL references it (either by `challenge("name")` or by an `includeFilesWithType = "pattern*.py" returns SomeType` glob).

## Commands

- `make help` — list every target with a one-line description (the Makefile is self-documenting via `## ` annotations; bare `make` prints `help`)
- Run a single Kotest test: `./gradlew test --tests "ContentTests" --info`

The production `compileKotlin` task enables Kotlin's unused-return-value checker (`-Xreturn-value-checker=check`); it is intentionally **not** applied to test sources, since Kotest's assertion DSL returns its receiver and would emit only false positives there.

## Version

The project version lives in `gradle.properties` (`group=com.readingbat`) — not in `build.gradle.kts` and not in the version catalog. A release bump means editing that line and updating `CHANGELOG.md`, `RELEASE_NOTES.md`, `llms.txt`, and the version table in `README.md`, all of which restate the current version and dependency set.

## Content / source pairing

The DSL in `Content.kt` is the single source of truth for what challenges exist. Two ways to register challenges in a group:

- Explicit: `challenge("for_loop1") { returnType = StringType }` — file must exist at `<langdir>/<packageName>/for_loop1.py` (or `.java`/`.kt`)
- Glob: `includeFilesWithType = "while*.py" returns IntType` — every matching file in the group's `packageName` directory is auto-registered with that return type

Java return types are inferred from code; Python and Kotlin must be declared.

`Content.kt` line 10 toggles the content source: `GitHubRepo` in production, `FileSystemSource("./")` in development. The local filesystem source is what makes `make run` pick up edits to files under `python/` etc.

## Testing

`ContentTests.kt` is the canonical example: it boots `testApplication { application { testModule(content) } }` and walks every challenge to verify blank/wrong/correct answer behavior. Follow its shape when adding tests.

## Static analysis

- The build no longer references a detekt baseline file; `make detekt-baseline` can still generate `detekt-baseline.xml`, but you must re-add `baseline = file("detekt-baseline.xml")` to `configureDetekt()` for detekt to consume it.

## Continuous integration

Before pushing, `make lint && make tests` reproduces CI locally.

## Gotchas

- `application.conf` line 12 references `watch = ["readingbat-template"]` — this is dev-only; production deployments should not watch.
- `Procfile` runs the uberjar with `-Dagent.config=src/main/resources/application.conf`. The config path is relative to the working directory, so don't move that file without updating the Procfile.
- `settings.gradle.kts` sets `RepositoriesMode.FAIL_ON_PROJECT_REPOS` — repositories must be declared in `settings.gradle.kts`, not in `build.gradle.kts`.
- `org.gradle.configuration-cache=false` is intentional (some plugin in the chain isn't CC-compatible); don't flip it without verifying the build still works.
- The `gradle-wrapper = "..."` entry in `gradle/libs.versions.toml` is consumed by the `Makefile` (`make upgrade-wrapper`) via `sed`, not by Gradle itself. Don't remove it thinking it's dead.
- `make versions` (dependencyUpdates) filters out pre-release candidates (alpha/beta/RC/milestone/snapshot) for any dependency currently on a stable version, but still surfaces newer pre-releases for deps already tracking a pre-release line (e.g. detekt's alpha). See `configureVersions()` in `build.gradle.kts`.
- Java challenge package is `jgroup` and Kotlin challenge package is `kgroup` (not `group1` / `kgroup1`). The directory name must match the `packageName` in `Content.kt`.
