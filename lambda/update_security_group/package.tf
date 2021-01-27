data "archive_file" "lambda_package_step" {
  source_dir  = "./src/"
  output_path = var.filename
  type        = "zip"
  depends_on  = [null_resource.lambda_build_step]
}

resource "null_resource" "lambda_build_step" {
  triggers = {
      main         = "${base64sha256(file("src/update_sg.py"))}"
      requirements = "${base64sha256(file("requirements.txt"))}"
     }

  provisioner "local-exec" {
       command = "sh build.sh"
     }
}
