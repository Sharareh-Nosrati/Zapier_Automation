actions = (input_data.get("actions") or "").lower()
source = (input_data.get("source") or "").lower()

score = 0

if "menu_viewed" in actions:
    score += 10
if "reservation_started" in actions:
    score += 25
if "reservation_completed" in actions:
    score += 40
if "payment_completed" in actions:
    score += 60

if source in ["meta", "google", "linkedin"]:
    score += 5

if "payment_completed" in actions or "reservation_completed" in actions:
    quality = "high"
elif "reservation_started" in actions:
    quality = "medium"
else:
    quality = "low"

return {
    "score": score,
    "lead_quality": quality
}
