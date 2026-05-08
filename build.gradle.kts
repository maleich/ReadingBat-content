import org.gradle.api.tasks.testing.logging.TestExceptionFormat
import org.gradle.api.tasks.testing.logging.TestLogEvent

private object Tasks {
  const val CLEAN = "clean"
  const val BUILD = "build"
  const val STAGE = "stage"
}

private object Shadow {
  const val ARCHIVE_NAME = "server.jar"
  val EXCLUDES = listOf("META-INF/*.SF", "META-INF/*.DSA", "META-INF/*.RSA", "LICENSE*")
}

plugins {
  application
  alias(libs.plugins.kotlin.jvm)
  alias(libs.plugins.versions)
  alias(libs.plugins.ktor.plugin)
}

// This is for ./gradlew run
application {
  mainClass = "ContentServerKt"
}

description = "ReadingBat Site"

dependencies {
  implementation(libs.readingbat.core)
  implementation(libs.core.utils)
  implementation(libs.kotlin.logging)

  testImplementation(libs.bundles.testing)
}

kotlin {
  jvmToolchain(libs.versions.jvm.get().toInt())
}

tasks.register(Tasks.STAGE) {
  dependsOn(Tasks.CLEAN, Tasks.BUILD)
}

tasks.named(Tasks.BUILD) {
  mustRunAfter(Tasks.CLEAN)
}

tasks.shadowJar {
  archiveFileName.set(Shadow.ARCHIVE_NAME)
  isZip64 = true
  duplicatesStrategy = DuplicatesStrategy.EXCLUDE
  Shadow.EXCLUDES.forEach { exclude(it) }
}

tasks.test {
  useJUnitPlatform()

  testLogging {
    events = setOf(TestLogEvent.PASSED, TestLogEvent.SKIPPED, TestLogEvent.FAILED)
    exceptionFormat = TestExceptionFormat.FULL
    showStandardStreams = false
  }
}
