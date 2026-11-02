BUSINESS = {
    "name": "Rivas Martinez Cleaning Services",
    "short": "Rivas Martinez",
    "phone": "+1 281-908-8284",
    "phone_href": "+12819088284",
    "address": "642 Arvana St, Houston, TX 77034",
    "hours": "Open 24 hours",
    "rating": "4.8",
    "reviews": "207",
}
def business(request):
    return {"biz": BUSINESS}
