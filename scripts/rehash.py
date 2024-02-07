import requests

def text_rehash_ua(input_text):
	url = "https://paraphrasing-and-rewriter-api.p.rapidapi.com/rewrite-light"

	payload = {
		"from": "ua",
		"text": input_text
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "529db806d7mshf647499ca507ea4p1413edjsnd8e908396cc2",
		"X-RapidAPI-Host": "paraphrasing-and-rewriter-api.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.content.decode('utf-8')