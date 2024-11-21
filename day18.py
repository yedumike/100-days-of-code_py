import random


data = [
    {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    },
     {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }, {
        "name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"
    }
]

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)