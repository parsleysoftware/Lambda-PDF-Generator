# README.md

This repository hosts the code and content for an article I wrote about creating a PDF generator with AWS Lambda and WKHTMLtoPDF.

## How to get this running

1. Have AWS Cli installed and configured (You must have access keys that can use Lambda and S3)
1. `cd project_root`
1. Change the name of `config.sample.yml` to `config.yml`
1. Set the name of your S3 bucket in the `config.yml`
1. `serverless deploy`

## Serverless IAM access

Use minimum-serverless-permissions.json for serverless IAM user access

## Integration

Just use generated endpoint from sls deploy command in your html 2 pdf conversion app


## Links

[Medium](https://medium.com/@_rich/richard-keller-61d9cb0f430)
[Dev.to](https://dev.to/_rich/building-a-pdf-generator-on-aws-lambda-with-python3-and-wkhtmltopdf-50kl)
[My Blog](https://blog.richardkeller.net/building-a-pdf-generator-on-aws-lambda-with-python3-and-wkhtmltopdf/)

***Copyright 06/23/2019. Richard Keller.***