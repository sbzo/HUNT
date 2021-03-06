import re

''' find posible IDOR using Hunt Methodology'''

def scan(ps, msg, src):
  # Test the request and/or response here
  if (True):
    # Change to a test which detects the vulnerability
    # raiseAlert(risk, int reliability, String name, String description, String uri, 
    # String param, String attack, String otherInfo, String solution, String evidence, 
    # int cweId, int wascId, HttpMessage msg)
    # risk: 0: info, 1: low, 2: medium, 3: high
    # reliability: 0: falsePositive, 1: suspicious, 2: warning
	
	words = ['id','user','account','number','order','no','doc','key','email','group','profile','edit','report']
	
	result = []
	
	params = msg.getParamNames()
	params = [element.lower() for element in params]

	for x in words:
		y = re.compile(".*"+x)
		if len(filter(y.match, params))>0:
			result.append(x)
	if result:
		ps.raiseAlert(1, 1, 'Possible IDOR', 'HUNT located the <b>$param$</b> parameter inside of your application traffic. The <b>$param$</b> parameter is most often susceptible to Insecure Direct Object Reference Vulnerabilities. Direct object reference vulnerabilities occur when there are insufficient authorization checks performed against object identifiers used in requests. This could occur when database keys, filenames, or other identifiers are used to directly access resources within an application. These identifiers would likely be predictable (an incrementing counter, the name of a file, etc), making it easy for an attacker to detect this vulnerability class. If further authorization checks are not performed, this could lead to unauthorized access to the underlying data.<br><br>HUNT recommends further manual analysis of the parameter in question.<br><br>For Insecure Direct Object Reference Vulnerabilities HUNT recommends the following resources to aid in manual testing:<br><br>The Web Application Hackers Handbook: Chapter 8<br><a href=https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)>Testing for Insecure Direct Object References (OTG-AUTHZ-004)</a><a href=https://support.portswigger.net/customer/portal/articles/1965691-using-burp-to-test-for-insecure-direct-object-references>Using Burp to Test for Insecure Direct Object References</a><br><a href=https://github.com/ngalongc/bug-bounty-reference#insecure-direct-object-reference-idor>IDOR Examples from ngalongc/bug-bounty-reference</a>', 
     	 msg.getRequestHeader().getURI().toString(), 
     	 ','.join(result), '', msg.getRequestHeader().toString()+'\n'+msg.getRequestBody().toString(), '', '', 0, 0, msg);
