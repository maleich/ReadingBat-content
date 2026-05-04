# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **content repository** built on the [ReadingBat template](https://github.com/readingbat/readingbat-template). It does not implement the ReadingBat web framework — it depends on `com.readingbat:readingbat-core` (see `gradle/libs.versions.toml`) and supplies:

1. Challenge source files (`python/`, `src/main/java/group1/`, `src/main/kotlin/kgroup1/`)
2. A Kotlin DSL declaration in `src/main/kotlin/Content.kt` that wires those files into language groups, return types, and descriptions
3. A thin `ContentServer.kt` entry point that delegates to `ReadingBatServer.start(args)`

When the user asks to "add a challenge," it almost always means: add the source file under the appropriate language directory **and** register it in `Content.kt`. A file on disk is invisible to the site until the DSL references it (either by `challenge("name")` or by an `includeFilesWithType = "pattern*.py" returns SomeType` glob).

## Commands

- `make build` / `./gradlew build -xtest` — build without running tests
- `make tests` / `./gradlew --rerun-tasks check` — run all tests
- `make run` / `./gradlew run` — start the dev server on port 8080 (entry: `ContentServerKt`)
- `make cc` — continuous build (`./gradlew build --continuous -xtest`)
- `make uber` — build shadow uberjar to `build/libs/server.jar` and run it
- `make versioncheck` — `./gradlew dependencyUpdates` (default `make` target)
- Run a single Kotest test: `./gradlew test --tests "ContentTests" --info`

JVM toolchain is 17 (`kotlin { jvmToolchain(17) }`).

## Content / source pairing

The DSL in `Content.kt` is the single source of truth for what challenges exist. Two ways to register challenges in a group:

- Explicit: `challenge("for_loop1") { returnType = StringType }` — file must exist at `<langdir>/<packageName>/for_loop1.py` (or `.java`/`.kt`)
- Glob: `includeFilesWithType = "while*.py" returns IntType` — every matching file in the group's `packageName` directory is auto-registered with that return type

Java return types are inferred from code; Python and Kotlin must be declared.

`Content.kt` line 10 toggles the content source: `GitHubRepo` in production, `FileSystemSource("./")` in development. The local filesystem source is what makes `make run` pick up edits to files under `python/` etc.

## Testing

Tests use **Kotest** (`StringSpec`) plus `com.readingbat:readingbat-kotest` test helpers (`testModule`, `forEachLanguage`, `forEachChallenge`, `pythonChallenge`, `answerFor`, `shouldHaveAnswer`). `ContentTests.kt` is the canonical example: it boots `testApplication { application { testModule(content) } }` and walks every challenge to verify blank/wrong/correct answer behavior.

When the user asks for new tests, follow the existing `ContentTests.kt` shape and the global rule: `StringSpec()` with `init {}`, MockK where appropriate.

## Gotchas

- `application.conf` line 12 references `watch = ["readingbat-template"]` — this is dev-only; production deployments should not watch.
- `Procfile` runs the uberjar with `-Dagent.config=src/main/resources/application.conf`. The config path is relative to the working directory, so don't move that file without updating the Procfile.
- `settings.gradle.kts` sets `RepositoriesMode.FAIL_ON_PROJECT_REPOS` — repositories must be declared in `settings.gradle.kts`, not in `build.gradle.kts`.
- `org.gradle.configuration-cache=false` is intentional (some plugin in the chain isn't CC-compatible); don't flip it without verifying the build still works.
