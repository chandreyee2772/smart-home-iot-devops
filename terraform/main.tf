provider "aws" {
  region = "ap-south-1" // Change as needed
}

resource "aws_instance" "iot_app" {
  ami           = "<ami-id>"
  instance_type = "t2.micro"
  tags = { Name = "SmartHomeIoT" }
}
