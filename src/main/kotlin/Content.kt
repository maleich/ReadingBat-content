import com.pambrose.common.util.FileSystemSource
import com.pambrose.common.util.GitHubRepo
import com.pambrose.common.util.OwnerType
import com.readingbat.dsl.ReturnType
import com.readingbat.dsl.isProduction
import com.readingbat.dsl.readingBatContent

val content =
  readingBatContent {
    repo = if (isProduction()) GitHubRepo(OwnerType.User, "maleich", "ReadingBat-content") else FileSystemSource("./")

    python {

      group("Booleans") {
        packageName = "boolean"
        description = "Basic boolean expressions"

        challenge("boolean1") {
          description = "Descriptions support **markdown**"
          returnType = ReturnType.BooleanType
        }

        includeFilesWithType = "boolean*.py" returns ReturnType.BooleanType
        includeFilesWithType = "greater_than*.py" returns ReturnType.BooleanType
        includeFilesWithType = "less_than*.py" returns ReturnType.BooleanType
        includeFilesWithType = "is_equal*.py" returns ReturnType.BooleanType
        includeFilesWithType = "not_equal*.py" returns ReturnType.BooleanType
        includeFilesWithType = "test*.py" returns ReturnType.BooleanType
        includeFilesWithType = "divisibility*.py" returns ReturnType.BooleanType
      }

      group("Strings") {
        packageName = "strings"
        description = "Practicing string operations"
        includeFilesWithType = "strings*.py" returns ReturnType.StringType

        challenge("str_find") { returnType = ReturnType.IntType }
      }

      group("Grab Bag") {
        packageName = "grab_bag"
        description = "Miscellaneous practice"
        includeFilesWithType = "slice*.py" returns ReturnType.StringType
        includeFilesWithType = "geometry*.py" returns ReturnType.IntType

        challenge("parameters1") { returnType = ReturnType.IntType }
        challenge("Fibonacci") { returnType = ReturnType.IntType }
        challenge("triangle") { returnType = ReturnType.BooleanType }
        challenge("square_root") { returnType = ReturnType.BooleanType }
        challenge("leap_year") { returnType = ReturnType.IntType }
      }

      group("Loops") {
        packageName = "loops"
        description = "While and for loop practice"
        includeFilesWithType = "while*.py" returns ReturnType.IntType

        challenge("for_loop1") { returnType = ReturnType.StringType }
        challenge("for_loop2") { returnType = ReturnType.IntType }
        challenge("for_loop3") { returnType = ReturnType.IntType }
        challenge("for_loop4") { returnType = ReturnType.IntType }
        challenge("num_name") { returnType = ReturnType.IntType }
      }

      group("List Practice") {
        packageName = "list_practice"
        description = "Working with lists"
        includeFilesWithType = "lists*.py" returns ReturnType.IntListType
        includeFilesWithType = "list_indexing*.py" returns ReturnType.StringType
      }

      group("Conditionals") {
        packageName = "conditionals"
        description = "If/elif/else"

        challenge("conditionals1") { returnType = ReturnType.IntType }
        challenge("conditionals2") { returnType = ReturnType.BooleanType }
        challenge("conditionals3") { returnType = ReturnType.IntType }
        challenge("conditionals4") { returnType = ReturnType.IntType }
        challenge("conditionals5") { returnType = ReturnType.BooleanType }
        challenge("conditionals6") { returnType = ReturnType.StringType }
        challenge("conditionals7") { returnType = ReturnType.IntType }
        challenge("conditionals8") { returnType = ReturnType.StringType }
        challenge("conditionals9") { returnType = ReturnType.StringType }
        challenge("calculator") { returnType = ReturnType.IntType }
      }

      group("Variables") {
        packageName = "variables"
        description = "Variables & mathematical operations"

        challenge("addition1") { returnType = ReturnType.IntType }
        challenge("addition2") { returnType = ReturnType.FloatType }
        challenge("addition3") { returnType = ReturnType.IntType }
        challenge("addition4") { returnType = ReturnType.StringType }
        challenge("subtract1") { returnType = ReturnType.IntType }
        challenge("subtract2") { returnType = ReturnType.FloatType }
        challenge("subtract3") { returnType = ReturnType.IntType }
        challenge("mult1") { returnType = ReturnType.IntType }
        challenge("mult2") { returnType = ReturnType.StringType }
        challenge("mult3") { returnType = ReturnType.IntType }
        challenge("divide1") { returnType = ReturnType.FloatType }
        challenge("mod1") { returnType = ReturnType.IntType }
        challenge("mod2") { returnType = ReturnType.StringType }
        challenge("exponent1") { returnType = ReturnType.IntType }
        challenge("floor_division1") { returnType = ReturnType.IntType }
        challenge("math1") { returnType = ReturnType.FloatType }

        includeFilesWithType = "variable_type*.py" returns ReturnType.StringType
        includeFilesWithType = "round*.py" returns ReturnType.FloatType
        includeFilesWithType = "abs_value*.py" returns ReturnType.IntType
      }
    }
  }
