import re

''' find posible File Inclusion using Hunt Methodology'''

def scan(ps, msg, src):
  # Test the request and/or response here
  if (True):
    # Change to a test which detects the vulnerability
    # raiseAlert(risk, int reliability, String name, String description, String uri, 
    # String param, String attack, String otherInfo, String solution, String evidence, 
    # int cweId, int wascId, HttpMessage msg)
    # risk: 0: info, 1: low, 2: medium, 3: high
    # reliability: 0: falsePositive, 1: suspicious, 2: warning
	
	words = ['file','document','folder','root','path','pg','style','pdf','template','php_path','doc']
	
	result = []

	params = msg.getParamNames()
	params = [element.lower() for element in params]

	for x in words:
		y = re.compile(".*"+x)
		if len(filter(y.match, params))>0:
			result.append(x)

	if result:
		ps.raiseAlert(1, 1, 'Possible File Inclusion or Path Traversal', 'HUNT located the <b>$param$</b> parameter inside of your application traffic. The <b>$param$</b> parameter is most often susceptible to File Inclusion or Path Traversal. HUNT recommends further manual analysis of the parameter in question. Also note that several parameters from this section and SSRF might overlap or need testing for both vulnerability categories.<br><br>For File Inclusion or Path Traversal HUNT recommends the following resources to aid in manual testing:<br><br>The Web Application Hackers Handbook: Chapter 10<br><a href=https://highon.coffee/blog/lfi-cheat-sheet/>Arr0way LFI Cheat Sheet</a><br><a href=https://www.gracefulsecurity.com/path-traversal-cheat-sheet-windows/>Gracefuls Path Traversal Cheat Sheet: Windows</a><br><a href=https://www.gracefulsecurity.com/path-traversal-cheat-sheet-linux/>Gracefuls Path Traversal Cheat Sheet: Linux</a><br>', 
     	 msg.getRequestHeader().getURI().toString(), 
     	 ','.join(result), '', msg.getRequestHeader().toString()+'\n'+msg.getRequestBody().toString(), '', '', 0, 0, msg);
