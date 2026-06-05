from services.spam_detector import predict_spam

from services.phishing_detector import predict_phishing

from services.keyword_analyzer import detect_keywords

from services.url_analyzer import extract_urls

from services.risk_scorer import calculate_risk_score


text = """
URGENT

Verify your account now.

Click:

https://fake-bank-login.com

to claim reward.
"""

spam_result = predict_spam(text)

phishing_result = predict_phishing(text)

keywords = detect_keywords(text)

urls = extract_urls(text)

risk_score = calculate_risk_score(
    max(
        spam_result["confidence"],
        phishing_result["confidence"]
    ),
    len(keywords),
    len(urls)
)

print(spam_result)

print(phishing_result)

print(keywords)

print(urls)

print(risk_score)