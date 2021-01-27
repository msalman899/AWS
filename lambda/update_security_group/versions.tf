provider "aws" {
  region  = var.aws_region
  version = "~> 2.52"
}

terraform {
  required_version = "~> 0.12.0"
}
