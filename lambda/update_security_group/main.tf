resource "aws_lambda_function" "lambda_function" {
  function_name    = var.function_name
  handler          = var.handler
  role             = aws_iam_role.lambda_iam_role.arn
  runtime          = var.runtime
  timeout          = var.timeout
  memory_size      = var.memory_size
  filename         = "${path.module}/${var.function_name}.zip"
  source_code_hash = filebase64sha256("${path.module}/${var.function_name}.zip")
  vpc_config {
    security_group_ids = var.security_group_ids
    subnet_ids         = var.subnet_ids
  }

  dynamic "environment" {
    for_each = length(keys(var.environment_variables)) == 0 ? [] : [true]
    content {
      variables = var.environment_variables
    }
  }
  tags = var.tags
}

############
# OUTPUT
###########

output "lambda_arn" {
  value = aws_lambda_function.lambda_function.arn
}

output "lambda_iam_role_id" {
  value = aws_iam_role.lambda_iam_role.id
}
