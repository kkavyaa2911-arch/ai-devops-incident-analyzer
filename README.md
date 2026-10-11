# AI DevOps Incident Analyzer

An AWS project that uses Amazon Bedrock Nova Lite to analyze DevOps incidents and Amazon DynamoDB to store incident analysis.

## Tech Stack
- AWS Lambda
- Amazon Bedrock (Nova Lite)
- Amazon DynamoDB
- Amazon CloudWatch
- Python
- Boto3

## Current Features
- Generates sample application logs.
- Uses AI to analyze incident logs.
- Identifies incident type and severity.
- Suggests probable root causes and remediation actions.
- Saves analysis results in DynamoDB.

## Architecture
Application Logs -> CloudWatch -> Lambda -> Amazon Bedrock -> DynamoDB

Note: Automated CloudWatch-to-Lambda triggering is still being configured.

## Sample Incidents
- Database connection timeout
- High CPU utilization

## Security
AWS credentials and secrets should never be committed to this repository.
