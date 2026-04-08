import com.readingbat.kotest.TestSupport.answerAllWith
import com.readingbat.kotest.TestSupport.answerAllWithCorrectAnswer
import com.readingbat.kotest.TestSupport.answerFor
import com.readingbat.kotest.TestSupport.forEachAnswer
import com.readingbat.kotest.TestSupport.forEachChallenge
import com.readingbat.kotest.TestSupport.forEachGroup
import com.readingbat.kotest.TestSupport.forEachLanguage
import com.readingbat.kotest.TestSupport.initTestProperties
import com.readingbat.kotest.TestSupport.pythonChallenge
import com.readingbat.kotest.TestSupport.shouldHaveAnswer
import com.readingbat.kotest.TestSupport.testModule
import com.readingbat.posts.AnswerStatus.CORRECT
import com.readingbat.posts.AnswerStatus.INCORRECT
import com.readingbat.posts.AnswerStatus.NOT_ANSWERED
import io.kotest.core.spec.style.StringSpec
import io.kotest.matchers.shouldBe
import io.kotest.matchers.string.shouldBeBlank
import io.ktor.server.testing.testApplication

class ContentTests : StringSpec() {
  init {
    beforeEach { initTestProperties() }

    "Test all challenges" {
      testApplication {
        application {
          testModule(content)
        }

        content.forEachLanguage {
          forEachGroup {
            forEachChallenge {
              answerAllWith(this@testApplication, "") {
                answerStatus shouldBe NOT_ANSWERED
                hint.shouldBeBlank()
              }

              answerAllWith(this@testApplication, "wrong answer") {
                answerStatus shouldBe INCORRECT
              }

              answerAllWithCorrectAnswer(this@testApplication) {
                answerStatus shouldBe CORRECT
                hint.shouldBeBlank()
              }
            }
          }
        }
      }
    }

    "Test with correct answers" {
      testApplication {
        application {
          testModule(content)
        }

        content.forEachLanguage {
          forEachGroup {
            forEachChallenge {
              forEachAnswer {
                it shouldHaveAnswer correctAnswers[it.index]
              }
            }
          }
        }
      }
    }

    "Test individual challenges" {
      testApplication {
        application {
          testModule(content)
        }

        content.pythonChallenge("Booleans", "boolean1") {
          answerFor(0) shouldHaveAnswer "False"
          answerFor(1) shouldHaveAnswer "True"
          answerFor(2) shouldHaveAnswer "False"
          answerFor(3) shouldHaveAnswer "True"
          answerFor(4) shouldHaveAnswer "False"
        }
      }
    }
  }
}
