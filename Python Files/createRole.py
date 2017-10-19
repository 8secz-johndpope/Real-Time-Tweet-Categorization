import boto3
import simplejson as json
import urllib2

def create_role(roleName, policyDoc):
	iam = boto3.resource('iam')
	with open(policyDoc) as policyD:
		policyData = json.load(policyD)
		print urllib2.quote(json.dumps(policyData))
	role = iam.create_role(
		RoleName = roleName,
		AssumeRolePolicyDocument = urllib2.quote(str(policyData))

	)
	return role
