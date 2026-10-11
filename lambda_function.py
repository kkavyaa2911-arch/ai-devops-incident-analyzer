import json
import boto3
from datetime import datetime, timezone

bedrock = boto3.client("bedrock-runtime", region_name="ap-south-1")
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("IncidentAnalysis")

MODEL_ID = "apac.amazon.nova-lite-v1:0"


def lambda_handler(event, context):
    incident_log = event.get(
        "log",
        "ERROR: Database connection failed: connection timeout"
    )

    prompt = f"""
Analyze this DevOps incident log:
{incident_log}

Return only valid JSON with these keys:
incident_type, severity, probable_root_cause, recommended_actions.
recommended_actions must be a list of actionable steps.
"""

    try:
        response = bedrock.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            inferenceConfig={
                "maxTokens": 500,
                "temperature": 0.2
            }
        )

        answer = response["output"]["message"]["content"][0]["text"]
        answer = answer.strip()

        if answer.startswith("```"):
            answer = answer.replace("```json", "").replace("```", "").strip()

        analysis = json.loads(answer)

        incident_id = datetime.now(timezone.utc).isoformat()

        item = {
            "incident_id": incident_id,
            "incident_log": incident_log,
            "incident_type": analysis["incident_type"],
            "severity": analysis["severity"],
            "probable_root_cause": analysis["probable_root_cause"],
            "recommended_actions": analysis["recommended_actions"]
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                **item,
                "message": "Incident analyzed and saved to DynamoDB"
            })
        }

    except Exception as e:
        print(f"Incident analysis failed: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Incident analysis failed",
                "details": str(e)
            })
        }import json
import boto3
from datetime import datetime, timezone

bedrock = boto3.client("bedrock-runtime", region_name="ap-south-1")
dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")
table = dynamodb.Table("IncidentAnalysis")

MODEL_ID = "apac.amazon.nova-lite-v1:0"


def lambda_handler(event, context):
    incident_log = event.get(
        "log",
        "ERROR: Database connection failed: connection timeout"
    )

    prompt = f"""
Analyze this DevOps incident log:
{incident_log}

Return only valid JSON with these keys:
incident_type, severity, probable_root_cause, recommended_actions.
recommended_actions must be a list of actionable steps.
"""

    try:
        response = bedrock.converse(
            modelId=MODEL_ID,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": prompt}]
                }
            ],
            inferenceConfig={
                "maxTokens": 500,
                "temperature": 0.2
            }
        )

        answer = response["output"]["message"]["content"][0]["text"]
        answer = answer.strip()

        if answer.startswith("```"):
            answer = answer.replace("```json", "").replace("```", "").strip()

        analysis = json.loads(answer)

        incident_id = datetime.now(timezone.utc).isoformat()

        item = {
            "incident_id": incident_id,
            "incident_log": incident_log,
            "incident_type": analysis["incident_type"],
            "severity": analysis["severity"],
            "probable_root_cause": analysis["probable_root_cause"],
            "recommended_actions": analysis["recommended_actions"]
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                **item,
                "message": "Incident analyzed and saved to DynamoDB"
            })
        }

    except Exception as e:
        print(f"Incident analysis failed: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Incident analysis failed",
                "details": str(e)
            })
        }
