import com.github.pambrose.common.util.FileSystemSource
import com.github.pambrose.common.util.GitHubRepo
import com.github.pambrose.common.util.OwnerType
import com.github.readingbat.dsl.ReturnType.*
import com.github.readingbat.dsl.isProduction
import com.github.readingbat.dsl.readingBatContent


val content =
  readingBatContent {
    repo = if (isProduction()) GitHubRepo(OwnerType.User, "maleich", "ReadingBat-content") else FileSystemSource("./")

    python {

      group("Booleans") {
        packageName = "boolean"
        description = "Basic boolean expressions"

        challenge("boolean1") {
          description = "Descriptions support **markdown**"
          returnType = BooleanType
        }

        includeFilesWithType = "boolean*.py" returns BooleanType
        includeFilesWithType = "greater_than*.py" returns BooleanType
        includeFilesWithType = "less_than*.py" returns BooleanType
        includeFilesWithType = "is_equal*.py" returns BooleanType
        includeFilesWithType = "not_equal*.py" returns BooleanType
        includeFilesWithType = "test*.py" returns BooleanType
      }

      group("Strings") {
        packageName = "strings"
        description = "Practicing string operations"
        includeFilesWithType = "strings*.py" returns StringType
      }

      group("Grab Bag") {
        packageName = "grab_bag"
        description = "Miscellaneous practice"
        includeFilesWithType = "slice*.py" returns StringType
        includeFilesWithType = "geometry*.py" returns IntType
        challenge("parameters1") {
          returnType = IntType
        }
        challenge("Fibonacci") {
          returnType = IntType
        }
        challenge("triangle") {
          returnType = BooleanType
        }
        challenge("square_root") {
          returnType = BooleanType
        }
        challenge("leap_year") {
          returnType = IntType
        }
      }

      group("Loops") {
        packageName = "loops"
        description = "While and for loop practice"
        includeFilesWithType = "while*.py" returns IntType

        challenge("for_loop1") {
          returnType = StringType
        }
        challenge("for_loop2") {
          returnType = IntType
        }
        challenge("for_loop3") {
          returnType = IntType
        }
        challenge("for_loop4") {
          returnType = IntType
        }
      }

      group("List Practice") {
        packageName = "list_practice"
        description = "Working with lists"
        includeFilesWithType = "lists*.py" returns IntListType
        includeFilesWithType = "list_indexing*.py" returns StringType

      }

      group("Conditionals") {
        packageName = "conditionals"
        description = "If/elif/else"

        challenge("conditionals1") {
          returnType = IntType
        }
        challenge("conditionals2") {
          returnType = BooleanType
        }
        challenge("conditionals3") {
          returnType = IntType
        }
        challenge("conditionals4") {
          returnType = IntType
        }
        challenge("conditionals5") {
          returnType = BooleanType
        }
        challenge("conditionals6") {
          returnType = StringType
        }
        challenge("conditionals7") {
          returnType = IntType
        }
        challenge("conditionals8") {
          returnType = StringType
        }
        challenge("conditionals9") {
          returnType = StringType
        }
      }

      group("Variables") {
        packageName = "variables"
        description = "Variables & mathematical operations"

        challenge("addition1") {
          //description = *in exercise*
          returnType = IntType
        }
        challenge("addition2") {
          //description = *in exercise*
          returnType = FloatType
        }
        challenge("addition3") {
          //description = *in exercise*
          returnType = IntType
        }
        challenge("addition4") {
          returnType = StringType
        }
        challenge("subtract1") {
          returnType = IntType
        }
        challenge("subtract2") {
          returnType = FloatType
        }
        challenge("subtract3") {
          returnType = IntType
        }
        challenge("mult1") {
          returnType = IntType
        }
        challenge("mult2") {
          returnType = StringType
        }
        challenge("mult3") {
          returnType = IntType
        }
        challenge("divide1") {
          returnType = FloatType
        }
        challenge("mod1") {
          returnType = IntType
        }
        challenge("mod2") {
          returnType = StringType
        }
        challenge("exponent1") {
          returnType = IntType
        }
        challenge("floor_division1") {
          returnType = IntType
        }
        challenge("math1") {
          returnType = FloatType
        }
        includeFilesWithType = "variable_type*.py" returns StringType
      }

    }
  }


