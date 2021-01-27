variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "account" {
  default = ""
}

variable "function_name" {
  default = "dummy_function"
}

variable "handler" {
  default = "dummy_function.lambda_handler"
}

variable "runtime" {
  default = "python3.7"
}

variable "timeout" {
  default = ""
}

variable "memory_size" {
  default = ""
}

variable "filename" {
  default = ""
}

variable "source_code_hash" {
  default = ""
}

variable "subnet_ids" {
  type    = list
  default = []
}

variable "security_group_ids" {
  type    = list
  default = []
}

variable "environment_variables" {
  type = map
  default = {

  }
}

variable "custom_policy_document" {
  default     = " "
  description = "Custom IAM Policy for Lambda Role"
}

variable "tags" {
  type        = map(string)
  default     = {}
  description = "Resource tags"
}
