######################  Making HTTP Requests with Python #####################

	- Describe what happens when you type a URL in the URL bar
	- Describe the request/response cycle
	- Explain what a request or response header is, and give examples
	- Explain the different categories of response codes 
	- Compare GET and POST requests
	

	
######## 1 : HTTP Introduction and Crash Course

				DNS Lookup
				Computer makes a REQUEST to a server	|
				Server processes the REQUEST			|>>>> Request/Response cycle
				Server issues a RESPONSE				|

		
		- Request/Response contains the HTTP Headers which contains meta-data about request/response.
			- Sent with both requests and responses
			- Provide additional information about the request or response
			
			
		- Request Headers
			Accept - Acceptable content-types for response (e.g. html, json, xml)
			Cache-Control - Specify caching behavior
			User-Agent - Information about the software used to make the request

		- Response Headers
			Access-Control-Allow-Origin - specify domains that can make requests
			Allowed - HTTP verbs that are allowed in requests
			
		- Response Status Codes
			2xx - Success
			3xx - Redirect
			4xx - Client Error (your fault!)
			5xx - Server Error (not your fault!)
			
			
			
			
######## 2 : HTTP Verbs and APIs


		- HTTP Verbs
			
			- GET
			
				- Useful for retrieving data
				- Data passed in query string
				- Should have no "side-effects", does not make any changes in the database.
				- Can be cached
				- Can be bookmarked
			
			- POST
				- Useful for writing data
				- Data passed in request body
				- Can have "side-effects", could make changes in the database.
				- Not cached
				- Can't be bookmarked
				
			- Most of the GET/POST requests happens through the API's. example : https://www.reddit.com/.json
			
			- APIs
				- API - Application Programming Interface
				- Allows you to get data from another application without needing to understand how the application works
				- Can often send data back in different formats
				- Examples of companies with APIs: GitHub, Spotify, Google			

			- API allows us to send information in the format we understand like JSON, XML.
			
			
			
########  3 : Writing Your First Python Request

		- Using the requests Module
			
			- requests Module
				- Lets us make HTTP requests from our Python code!
				- Installed using pip
					# python3 -m pip install requests
				- Useful for web scraping/crawling, grabbing data from other APIs, etc			

		
				>>> import requests
				>>> res = requests.get("https://news.ycombinator.com/")
				>>> res
				<Response [200]>
				>>> res.ok
				True
				>>> res.headers
					{'Date': 'Sat, 24 Mar 2018 19:47:56 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d1e785576e7349837ab2e43e23357e61b1521920875; expires=Sun, 24-Mar-19 19:47:55 GMT; path=/; domain=.ycombinator.com; HttpOnly', 'Vary': 'Accept-Encoding', 'Cache-Control': 'private; max-age=0', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin', 'Strict-Transport-Security': 'max-age=31556900', 'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.google.com/recaptcha/ https://www.gstatic.com/recaptcha/ https://cdnjs.cloudflare.com/; frame-src 'self' https://www.google.com/recaptcha/; style-src 'self' 'unsafe-inline'", 'Content-Encoding': 'gzip', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '400ba7007cc66fc6-SIN'}		

			- example : please refer to "first-request.py" file.
			
			
	
########  4 : Requesting JSON with Python

		- Making a Request

				import requests
				response = requests.get("http://www.example.com")


		- Request Headers
		
				import requests
				response = requests.get(
					"http://www.example.com",
					headers={
						"header1": "value1",
						"header2": "value2"
					}
				)		
				
		- example : refer to "headers.py" file.




########  5 : Sending Requests with Params

		- What's a Query String?

			- A way to pass data to the server as part of a GET request
			- example : http://www.example.com/?key1=value1&key2=value2
			- Browsers enforce a maximum size on length of the query string
		
			- general format :
				# option 1
				import requests
				response = requests.get(
					"http://www.example.com?key1=value1&key2=value2"
				)
				
				
				# option 2 - preferable!
				import requests
				response = requests.get(
					"http://www.example.com",
					params={
						"key1": "value1",
						"key2": "value2"
					}
				)

		- example : refer to "params.py" file.
		
		
		
######## 6 : API project

		- Make a API query for the dad's joke.
		- Ask User for input.
		- You will have to pull the joke related to that topic and show only one random joke on that.
		
		- code : refer to "dad.py" file.
		
		
		
		
######## 7 : Regarding POST request

		import requests
		import json
		
		response = requests.post(
			"http://www.example.com",
			data=json.dumps({
				"key1": "value1",
				"key2": "value2"
			})
		)

		- A note on API's

			- Some APIs require a key in order for you to use them
			- Especially true of APIs that allow you to send data, rather than just getting data
			- Typically sent as part of URL
			- API keys allow for greater control of how users interact with the API
			- Instructions for obtaining a key vary by API