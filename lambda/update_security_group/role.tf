
data "aws_iam_policy_document" "instance-assume-role-policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "logs" {
  statement: [
  {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
    ]
    resources = [
      "${format("arn:aws:logs:eu-west-1:%s:*", var.account)}"
    ]
  },
  {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]
    resources = ["${format("arn:aws:logs:us-east-1:%s:log-group:/aws/lambda/%s:*", var.account, var.function_name)}"]
  },
  {
    effect = "Allow"
    actions = [
       "ec2:DescribeSecurityGroups",
       "ec2:AuthorizeSecurityGroupIngress",
       "ec2:RevokeSecurityGroupIngress"
    ]
    resources = ""arn:aws:ec2:us-east-1:*:security-group/my-vpc-https-sg"
  }
 ]
  

}

resource "aws_iam_role" "lambda_iam_role" {
  name               = var.function_name
  assume_role_policy = data.aws_iam_policy_document.instance-assume-role-policy.json
}

resource "aws_iam_role_policy" "standard-inline-policy" {
  name   = "StandardPolicy"
  role   = aws_iam_role.lambda_iam_role.id
  policy = data.aws_iam_policy_document.logs.json
}

resource "aws_iam_role_policy" "custom-inline-policy" {
  count  = var.custom_policy_document != "" ? 1 : 0
  name   = "CustomPolicy"
  role   = aws_iam_role.lambda_iam_role.id
  policy = var.custom_policy_document
}
