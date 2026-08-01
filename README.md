[![Kotlin](https://img.shields.io/badge/%20language-Kotlin-red.svg)](https://kotlinlang.org/)
[![CI](https://github.com/maleich/ReadingBat-content/actions/workflows/ci.yml/badge.svg)](https://github.com/maleich/ReadingBat-content/actions/workflows/ci.yml)

# ReadingBat Template

[ReadingBat.com](https://www.readingbat.com) is an attempt to make learning how to program a little easier.

We are big fans of [CodingBat.com](https://codingbat.com) (so much so, that we
shamelessly copied its look and feel). However, we observed that students often
start using it to write code, prior to being equipped with the skill of reading code.
It is difficult to write code without first learning how to read and follow code!
So we set out to create ReadingBat.com, which attempts to make students comfortable
reading code challenges and learning code idioms. Once a student is comfortable with
reading code, they can head straight for [CodingBat.com](https://codingbat.com)
and move on to authoring their own code!

This template is for teachers who want to author their own ReadingBat content.
Once you create content for your students, send us a note and we will link the
[ReadingBat.com](https://www.readingbat.com) site to it.

## [Quickstart](https://github.com/readingbat/readingbat-template/wiki/Quickstart)

## [Setup](https://github.com/readingbat/readingbat-template/wiki/Setup)

## [Running a Server](https://github.com/readingbat/readingbat-template/wiki/Running-a-Server)

## Build & Run

Current version: **1.1.1** — see [CHANGELOG.md](CHANGELOG.md) and
[RELEASE_NOTES.md](RELEASE_NOTES.md).

Requires JDK 25. Toolchain versions are centralized in
[gradle/libs.versions.toml](gradle/libs.versions.toml): Kotlin 2.4.10,
Ktor 3.5.1, readingbat-core 3.3.1, Kotest 6.2.3, core-utils 3.2.2,
kotlinter 5.6.0, detekt 2.0.0-alpha.5, Gradle 9.6.1.

Lint, detekt, and tests also run in GitHub Actions on every push to `master`
and every pull request (see [.github/workflows/ci.yml](.github/workflows/ci.yml)).

| Task | Command |
| --- | --- |
| List all Make targets | `make help` |
| Run the dev server (port 8080) | `make run` (or `./gradlew run`) |
| Continuous build on file changes | `make cc` |
| Build without tests | `make build` |
| Run all tests | `make tests` |
| Run a single test class | `./gradlew test --tests "ContentTests" --info` |
| Lint Kotlin sources (kotlinter + detekt) | `make lint` |
| Format Kotlin sources | `make format` |
| Run detekt only | `make detekt` |
| Regenerate detekt baseline | `make detekt-baseline` |
| Build the shadow uberjar | `make uberjar` (output: `build/libs/server.jar`) |
| Build uberjar and run it | `make uber` |
| Check for dependency updates | `make versions` |
| Upgrade the Gradle wrapper | `make upgrade-wrapper` |

## Content Specification

Specify ReadingBat content with the ReadingBat-specific Kotlin DSL. Using the DSL does not require in-depth knowledge of
Kotlin.

ReadingBat supports challenges written in 3 languages: Python, Java and Kotlin.

Specify the content in the [src/main/kotlin/Content.kt](./src/main/kotlin/Content.kt) file.

The structure of the DSL is:
```kotlin
val content =
  readingBatContent {
    python {                                    // Creates a LanguageGroup object
      group("Group 1") {                        // Creates a ChallengeGroup named "Group 1"
        packageName = "jgroup"                  // The path of the challenges in this group
        description = "Description of **Python** Group 1" // Descriptions support markdown

        challenge("find_it") {                  // Creates a Challenge for jgroup/find_it.py
          returnType = BooleanType              // Challenge return type
        }

        challenge("boolean2") {                 // Creates a Challenge for jgroup/boolean2.py
          returnType = BooleanType              // Challenge return type
        }

        // Include all challenges matching the "slice*.py" filename pattern
        includeFilesWithType = "slice*.py" returns StringType
      }
    }

    java {
      group("Group 1") {
        packageName = "jgroup"
        description = "Description of **Java** Group 1"

        challenge("JoinEnds") {                 // Java Return types are inferred from the code
          codingBatEquiv = "p141494"            // Will add a link to this codingbat.com challenge
        }

        challenge("ReplaceCheck")               // Creates a Challenge for jgroup/ReplaceCheck.java

        // Include all challenges matching the "Has*.java" filename pattern
        includeFiles = "Has*.java"
      }
    }

    kotlin {
      group("Group 1") {
        packageName = "kgroup"
        description = "Description of **Kotlin** Group 1"

        challenge("StringLambda1") {
          returnType = StringType
        }

        // Include all challenges matching the "lambda*.kt" filename pattern
        includeFilesWithType = "lambda*.kt" returns StringType
      }
    }
  }
```

### DSL Objects

* [ReadingBatContent](https://github.com/readingbat/readingbat-template/wiki/ReadingBatContent-Objects)
* [LanguageGroup](https://github.com/readingbat/readingbat-template/wiki/LanguageGroup-Objects)
* [ChallengeGroup](https://github.com/readingbat/readingbat-template/wiki/ChallengeGroup-Objects)
* [Challenge](https://github.com/readingbat/readingbat-template/wiki/Challenge-Objects)

## Challenge Code

* [Python Code](https://github.com/readingbat/readingbat-template/wiki/Python-Challenges)
* [Java Code](https://github.com/readingbat/readingbat-template/wiki/Java-Challenges)
* [Kotlin Code](https://github.com/readingbat/readingbat-template/wiki/Kotlin-Challenges)

## [Server Configuration](https://github.com/readingbat/readingbat-template/wiki/Server-Configuration)

## Examples

This [repo](https://github.com/readingbat/readingbat-site) describes the
[ReadingBat.com](https://readingbat.com) website.
Its Content.kt combines content from 2 other repos.

### Content.kt Files for ReadingBat.com
* [Top-level Content.kt](https://github.com/readingbat/readingbat-site/blob/master/src/Content.kt)
* [Java and Kotlin Content](https://github.com/readingbat/readingbat-java-content/blob/master/src/main/kotlin/Content.kt)
* [Python Content](https://github.com/readingbat/readingbat-python-content/blob/master/src/Content.kt)

### Code Content for ReadingBat.com
* [Python](https://github.com/readingbat/readingbat-python-content/tree/master/python)
* [Java](https://github.com/readingbat/readingbat-java-content/tree/master/src/main/java)
* [Kotlin](https://github.com/readingbat/readingbat-java-content/tree/master/src/main/kotlin)

## [Kotlin Tips](https://github.com/readingbat/readingbat-template/wiki/Kotlin-Tips)

## [GitHub Tips](https://github.com/readingbat/readingbat-template/wiki/GitHub-Tips)

