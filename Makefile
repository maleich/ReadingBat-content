.PHONY: default help clean build tests uberjar uber cc run lint detekt detekt-baseline format \
		versions upgrade-wrapper _require-gradle-version

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

versions: ## Check for dependency updates (default target)
	./gradlew dependencyUpdates --no-configuration-cache --no-parallel

# Gradle's documented upgrade procedure: the first run rewrites
# gradle-wrapper.properties using the *old* wrapper jar; the second run
# regenerates the wrapper itself with the new version.
upgrade-wrapper: _require-gradle-version ## Upgrade Gradle wrapper to version in libs.versions.toml
	./gradlew wrapper --gradle-version=$(GRADLE_VERSION) --distribution-type=bin
	./gradlew wrapper --gradle-version=$(GRADLE_VERSION) --distribution-type=bin

_require-gradle-version:
	@[ -n "$(GRADLE_VERSION)" ] || { echo "ERROR: Could not determine gradle version from gradle/libs.versions.toml" >&2; exit 1; }
