.PHONY: default help clean build tests uberjar uber cc run lint detekt detekt-baseline format \
		versions versions-all upgrade-wrapper _require-gradle-version

GRADLE_VERSION := $(shell sed -n 's/^gradle-wrapper = "\(.*\)"/\1/p' gradle/libs.versions.toml)

default: help

help:  ## Show this help (list of targets)
	@awk 'BEGIN {FS = ":.*?## "; printf "Usage: make <target>\n\nTargets:\n"} \
		/^[a-zA-Z0-9_-]+:.*?## / {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

clean: ## Clean build outputs
	./gradlew clean

build: ## Build without running tests
	./gradlew build -x test

lint: ## Run Kotlinter and detekt
	./gradlew lintKotlin detekt

detekt: ## Run detekt static analysis
	./gradlew detekt

detekt-baseline: ## Generate detekt baseline file
	./gradlew detektBaseline

format: ## Format Kotlin sources with kotlinter
	./gradlew formatKotlin

tests: ## Run all tests
	./gradlew --rerun-tasks check

uberjar: ## Build shadow uberjar to build/libs/server.jar
	./gradlew uberjar

uber: uberjar ## Build uberjar and run it
	java -jar build/libs/server.jar

cc: ## Continuous build (no tests)
	./gradlew build --continuous -x test

run: ## Start the dev server on port 8080
	./gradlew run

# dependencyUpdates is marked incompatible with the configuration cache (build.gradle.kts),
# so --no-configuration-cache skips the cache for this run. build.gradle.kts gives the task a
# formatter that lists only what is behind; versions-all names the plugin's own plain report,
# which also lists everything up to date.
versions: ## List the dependencies with newer versions, and any that could not be checked
	./gradlew dependencyUpdates --no-configuration-cache --no-parallel

versions-all: ## The plugin's full dependency report, up-to-date dependencies included
	./gradlew dependencyUpdates --no-configuration-cache --no-parallel --output-formatter=plain

# Gradle's documented upgrade procedure: the first run rewrites
# gradle-wrapper.properties using the *old* wrapper jar; the second run
# regenerates the wrapper itself with the new version.
upgrade-wrapper: _require-gradle-version ## Upgrade Gradle wrapper to version in libs.versions.toml
	./gradlew wrapper --gradle-version=$(GRADLE_VERSION) --distribution-type=bin
	./gradlew wrapper --gradle-version=$(GRADLE_VERSION) --distribution-type=bin

_require-gradle-version:
	@[ -n "$(GRADLE_VERSION)" ] || { echo "ERROR: Could not determine gradle version from gradle/libs.versions.toml" >&2; exit 1; }
