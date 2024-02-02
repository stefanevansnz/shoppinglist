# Shopping List App using AWS SAM

This project contains source code and supporting files for a serverless application that can be used to view items on a shopping list and uses AWS SAM.

To use the AWS SAM CLI, you need the following tools:

* AWS SAM CLI - [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html).
* Node.js - [Install Node.js 18](https://nodejs.org/en/), including the npm package management tool.
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community).

## Deploy the sample application

To build and deploy your application for the first time, run the following in your shell:

```bash
cd sam-app
sam build
sam deploy
```

## Unit tests

Tests are defined in the `__tests__` folder in this project. Use `npm` to install the [Jest test framework](https://jestjs.io/) and run unit tests.

```bash
cd sam-app
my-application$ npm install
my-application$ npm run test
```

## Test locally
```bash
 cd react-app
 npm start
```
## Deploy ReactJS to S3

```bash
cd react-app
npm run build
aws s3 sync build/ s3://stefan-sam-app-bucket-915922766016

```

## Test in AWS with:
https://djlfwcpttl0u6.cloudfront.net/index.html

## Test upload using client based on https://docs.aws.amazon.com/textract/latest/dg/lambda.html

```bash
cd .\sam-app\src\client\

python3 textract_client.py stefan-sam-app-extractText-dywsjEgLYEyC s3://stefan-sam-app-imagebuck-915922766016/shopping_list.jpg
```



## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name sam-app
```

## Resources

For an introduction to the AWS SAM specification, the AWS SAM CLI, and serverless application concepts, see the [AWS SAM Developer Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html).

Next, you can use the AWS Serverless Application Repository to deploy ready-to-use apps that go beyond Hello World samples and learn how authors developed their applications. For more information, see the [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/) and the [AWS Serverless Application Repository Developer Guide](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/what-is-serverlessrepo.html).
